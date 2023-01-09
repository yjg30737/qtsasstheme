from qtpy.QtGui import QColor, QFont, qGray, QGuiApplication
from qtpy.QtCore import Qt, QCoreApplication
from qtpy.QtWidgets import QWidget, QMainWindow, QDialog, QAbstractButton, QApplication
from pyqt_svg_button import SvgButton

import os, tempfile, posixpath, re
import shutil

import qtsass


class QtSassTheme:

    def __init__(self):
        # set the icons
        cur_dir = os.path.dirname(__file__)
        ico_filename = os.path.join(cur_dir, 'ico/_icons.scss')
        icon_path = cur_dir.replace(os.path.sep, posixpath.sep)
        self.__setIcoPath(ico_filename, icon_path)
        self.__prepareFineLookingGUI()

    def __prepareFineLookingGUI(self):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support
        QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

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

    def __setFontSize(self, var_filename, font_size):
        QApplication.setFont(QFont('Arial', font_size))
        # with open(var_filename, 'r') as f:
        #     lines = f.readlines()
        #
        # new_line_for_font_size = f'$fontsize: {font_size}pt;'
        #
        # idx_to_replace = 0
        #
        # for i, line in enumerate(lines):
        #     if 'fontsize' in line:
        #         idx_to_replace = i
        #         break
        #
        # lines[idx_to_replace] = new_line_for_font_size
        #
        # with open(var_filename, 'w') as f:
        #     f.writelines(lines)


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
        self.__setFontSize(var_filename, font_size)

    def setThemeFiles(self, main_window: QWidget, input_path='res', exclude_type_lst: list = []):
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
            f_lst = ['theme.css', 'main_widget.css', 'icon_button.css', 'icon_text_button.css', 'menu_bar.css']
            f_lst = [os.path.join(input_path, f) for f in f_lst]

            with open(f_lst[0], 'r') as f:
                theme_style = f.read()
            with open(f_lst[1], 'r') as f:
                main_widget_style = f.read()
            with open(f_lst[2], 'r') as f:
                icon_button_style = f.read()
            with open(f_lst[3], 'r') as f:
                icon_text_button_style = f.read()
            with open(f_lst[4], 'r') as f:
                menu_bar_style = f.read()

            if isinstance(main_window, QMainWindow) or isinstance(main_window, QDialog):
                main_window.setStyleSheet(theme_style)
            else:
                main_window.setObjectName('mainWidget')
                main_window.setStyleSheet(theme_style + main_widget_style)

            # button
            def setButtonStyle(main_window):
                btns = main_window.findChildren(QAbstractButton)
                for btn in btns:
                    # check if text exists
                    if btn.text().strip() == '':
                        # if button type is SvgButton, let it keep its own style
                        if isinstance(btn, SvgButton):
                            pass
                        else:
                            btn.setStyleSheet(icon_button_style)  # no text - icon button style
                    else:
                        # if button type is SvgButton, let it maintain its own style
                        if isinstance(btn, SvgButton):
                            pass
                        else:
                            btn.setStyleSheet(icon_text_button_style)  # text - icon-text button style

            # check exclusion of QAbstractButton
            if QAbstractButton in exclude_type_lst:
                pass
            else:
                setButtonStyle(main_window)

            # todo check exclusion of other types
            if len(exclude_type_lst) > 0:
                for _type in exclude_type_lst:
                    widgets = main_window.findChildren(_type)
                    if isinstance(_type, QAbstractButton):
                        print(_type)

            if isinstance(main_window, QMainWindow):
                menu_bar = main_window.menuBar()  # menu bar
                menu_bar.setStyleSheet(menu_bar_style)

        # modrenize the font - for pyqt5/pyside2
        if os.environ['QT_API'] == 'pyqt5' or os.environ['QT_API'] == 'pyside2':
            def modernizeAppFont():
                from qtpy.QtWidgets import qApp
                # modernize the font
                appFont = qApp.font()
                # font family: arial
                appFont.setFamily('Arial')
                # font size: 9~12
                appFont.setPointSize(min(12, max(9, appFont.pointSize() * qApp.desktop().logicalDpiX() / 96.0)))
                # font style strategy: antialiasing
                appFont.setStyleStrategy(QFont.PreferAntialias)
                qApp.setFont(appFont)
                # fade menu and tooltip
                qApp.setEffectEnabled(Qt.UI_FadeMenu, True)
                qApp.setEffectEnabled(Qt.UI_FadeTooltip, True)

            modernizeAppFont()

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

    def getMainWidgetStyle(self):
        css = self.__getStyle('main_widget.scss')
        return css

