from PyQt5.QtWidgets import QWidget, QMainWindow, QDialog, QAbstractButton
from pyqt_svg_button import SvgButton

import os, tempfile, posixpath, re
import shutil

import qtsass


class QtSassThemeGetter:

    def __init__(self):
        # set the icons
        cur_dir = os.path.dirname(__file__)
        ico_filename = os.path.join(cur_dir, 'ico/_icons.scss')
        icon_path = cur_dir.replace(os.path.sep, posixpath.sep)
        self.__setIconPath(ico_filename, icon_path)

    def __setIconPath(self, ico_filename: str, icon_path: str):
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

    def __getStyle(self, filename):
        cur_dir = os.path.dirname(__file__)
        sass_dirname = os.path.join(cur_dir, 'sass')
        # make temporary file
        temp_file = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
        css = qtsass.compile_filename(os.path.join(sass_dirname, filename), temp_file)
        return css

    def getThemeFiles(self, theme: str = 'dark', output_path=os.getcwd()):
        cur_dir = os.path.dirname(__file__)
        theme_prefix = theme.split('_')[0]
        ico_dirname = os.path.join(cur_dir, os.path.join('ico', theme_prefix))
        sass_dirname = os.path.join(cur_dir, 'sass')
        var_dirname = os.path.join(cur_dir, os.path.join('var', theme))
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
        self.__setIconPath(ico_filename, output_dirname)

    def setThemeFiles(self, main_window: QWidget, input_path='res', exclude_type_lst: list = []):
        qtsass.compile_dirname('sass', '.')

        ico_filename = 'ico/_icons.scss'
        os.remove(ico_filename)
        shutil.rmtree('sass')
        shutil.rmtree('var')

        os.chdir('../')
        if os.path.isdir(input_path):
            f_lst = ['theme.css', 'main_widget.css', 'icon_button.css', 'icon_text_button.css', 'menu_bar.css']
            input_path = os.path.join(os.getcwd(), input_path)
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

