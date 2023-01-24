from qtpy.QtGui import QColor, QFont, qGray, QGuiApplication
from qtpy.QtCore import Qt, QCoreApplication
from qtpy.QtWidgets import QWidget, QMainWindow, QDialog, QAbstractButton, QApplication

import os, tempfile, posixpath, re
import shutil

import qtsass

# Set attribute Qt::AA_EnableHighDpiScaling before QCoreApplication is created
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support
QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

class QtSassTheme:

    def __init__(self):
        # set the icons
        cur_dir = os.path.dirname(__file__)
        icon_path = cur_dir.replace(os.path.sep, posixpath.sep)
        ico_filename = os.path.join(icon_path, 'ico/_icons.scss').replace(os.path.sep, posixpath.sep)
        self.__setIcoPath(ico_filename, icon_path)

    def __setIcoPath(self, ico_filename: str, icon_path: str):
        import_abspath_str = f'$icopath: \'{icon_path}/\';'
        with open(ico_filename, 'r+') as f:
            fdata = f.read()
            # if the path is still same
            if fdata.find(import_abspath_str) != -1:
                pass
            else:
                m = re.search(r'\$icopath:\s(\"|\')(.+)(\"|\')', fdata)
                # if the path was changed
                if m:
                    f.truncate(0)
                    f.seek(0, 0)
                    f.write(import_abspath_str + '\n' + '\n'.join(fdata.splitlines(True)[1:]))

                # if the path is nowhere (which means it is the first time to set the path)
                else:
                    f.seek(0, 0)
                    f.write(import_abspath_str + '\n' + fdata)

    def __setCustomThemeColor(self, var_filename: str, theme_color: str):
        with open(var_filename, 'r+') as f:
            fdata = f.read()
            m = re.search(r'\$bgcolor:(.+\n)', fdata)
            if m:
                custom_theme_code = f'$bgcolor: {theme_color};\n'
                f.truncate(0)
                f.seek(0, 0)
                f.write(custom_theme_code + ''.join(fdata.splitlines(True)[1:]))

    def __setBackgroundPolicy(self, var_filename: str, background_darker=False):
        if background_darker:
             with open(var_filename, 'r+') as f:
                fdata = f.read()
                m1 = re.search(r'\$bgcolor:(.+\n)', fdata)
                m2 = re.search(r'\$widgetcolor:(.+\n)', fdata)
                if m1 and m2:
                    w_color_v = m1.group(1)
                    bg_color_v = m2.group(1).replace('bgcolor', 'widgetcolor')
                    background_darker_code = f'$widgetcolor:{w_color_v}' \
                                             f'$bgcolor:{bg_color_v}'
                    background_darker_code += ''.join(fdata.splitlines(True)[2:])
                    f.truncate(0)
                    f.seek(0, 0)
                    f.write(background_darker_code)
        else:
            pass

    def __setFontSize(self, font_size):
        font = QApplication.font()
        family_name = QApplication.font().family()
        font.setFamily(family_name)
        font.setPointSize(font_size)
        font.setStyleStrategy(QFont.PreferAntialias)
        QApplication.setFont(font)


    def __getStyle(self, filename):
        cur_dir = os.path.dirname(__file__)
        sass_dirname = os.path.join(cur_dir, 'sass')
        # make temporary file
        temp_file = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
        css = qtsass.compile_filename(os.path.join(sass_dirname, filename), temp_file)
        return css

    def getThemeFiles(self, theme: str = 'dark_gray', font_size=9, background_darker=False, output_path=os.getcwd()):
        theme_lst = ['dark_gray', 'dark_blue', 'light_gray', 'light_blue']
        cur_dir = os.path.dirname(__file__)
        official_theme_flag = theme in theme_lst
        if official_theme_flag:
            theme_prefix = theme.split('_')[0]
            ico_dirname = os.path.join(cur_dir, os.path.join('ico', theme_prefix))
            var_dirname = os.path.join(cur_dir, os.path.join(os.path.join('var', theme_prefix), theme))

        # check whether theme value is 6-digit hex color
        else:
            m = re.match(r'#[a-fA-F0-9]{6}', theme)
            if m:
                theme_color = m.group(0)
                theme_color = QColor(theme_color)

                # 'if it is, check 6-digit hex color is lighter than usual or darker')
                r, g, b = theme_color.red(), theme_color.green(), theme_color.blue()
                theme_lightness = ''
                if qGray(r, g, b) > 255 // 2:
                    theme_lightness = 'light'
                else:
                    theme_lightness = 'dark'

                # get the ico_dirname
                ico_dirname = os.path.join(cur_dir, os.path.join('ico', theme_lightness))

                # get the dark_gray/light_gray theme
                var_dirname = os.path.join(cur_dir, os.path.join(os.path.join('var', theme_lightness),
                                                                 theme_lightness+'_gray'))
            else:
                raise Exception('Invalid theme')

        sass_dirname = os.path.join(cur_dir, 'sass')
        os.chdir(output_path)
        output_dirname = 'res'
        if os.path.exists(output_dirname):
            pass
        else:
            os.mkdir(output_dirname)
        os.chdir(output_dirname)
        if os.path.exists('ico'):
            shutil.rmtree('ico')
        if os.path.exists('sass'):
            shutil.rmtree('sass')
        if os.path.exists('var'):
            shutil.rmtree('var')
        shutil.copytree(ico_dirname, 'ico')
        shutil.copytree(sass_dirname, 'sass')
        shutil.copytree(var_dirname, 'var')

        ico_filename = 'ico/_icons.scss'
        self.__setIcoPath(ico_filename, output_dirname)

        var_filename = 'var/_variables.scss'
        if official_theme_flag:
            pass
        else:
            self.__setCustomThemeColor(var_filename, theme)
        self.__setBackgroundPolicy(var_filename, background_darker)
        self.__setFontSize(font_size)

        # fade menu and tooltip
        QApplication.setEffectEnabled(Qt.UI_FadeMenu, True)
        QApplication.setEffectEnabled(Qt.UI_FadeTooltip, True)

    def setThemeFiles(self, main_window: QWidget, input_path='res'):
        if os.path.basename(os.getcwd()) != input_path:
            input_path = os.path.join(os.getcwd(), input_path)
            os.chdir(input_path)
        qtsass.compile_dirname('sass', '.')
        ico_filename = 'ico/_icons.scss'
        sass_dirname = 'sass'
        var_dirname = 'var'
        if os.path.exists(ico_filename):
            os.remove(ico_filename)
        if os.path.exists(sass_dirname):
            shutil.rmtree(sass_dirname)
        if os.path.exists(var_dirname):
            shutil.rmtree(var_dirname)

        os.chdir('../')
        if os.path.isdir(input_path):
            f_lst = ['theme.css', 'icon_button.css', 'icon_text_button.css', 'menu_bar.css']
            f_lst = [os.path.join(input_path, f) for f in f_lst]

            with open(f_lst[0], 'r') as f:
                theme_style = f.read()
            with open(f_lst[1], 'r') as f:
                icon_button_style = f.read()
            with open(f_lst[2], 'r') as f:
                icon_text_button_style = f.read()
            with open(f_lst[3], 'r') as f:
                menu_bar_style = f.read()

            main_window.setStyleSheet(theme_style)

            # button
            def setButtonStyle(main_window):
                btns = main_window.findChildren(QAbstractButton)
                for btn in btns:
                    # check if text exists
                    if btn.text().strip() == '':
                        btn.setStyleSheet(icon_button_style)  # no text - icon button style
                    else:
                        btn.setStyleSheet(icon_text_button_style)  # text - icon-text button style

            setButtonStyle(main_window)

            if isinstance(main_window, QMainWindow):
                menu_bar = main_window.menuBar()  # menu bar
                menu_bar.setStyleSheet(menu_bar_style)

    def getThemeStyle(self):
        css = self.__getStyle('theme.scss')
        return css

    def getIconButtonStyle(self):
        css = self.__getStyle('icon_button.scss')
        return css

    def getIconTextButtonStyle(self):
        css = self.__getStyle('icon_text_button.scss')
        return css

    def getMenuBarStyle(self):
        css = self.__getStyle('menu_bar.scss')
        return css

