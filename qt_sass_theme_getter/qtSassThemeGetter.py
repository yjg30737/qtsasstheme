import os, tempfile

import qtsass


class QtSassThemeGetter:

    def __init__(self):
        pass

    def setThemeColor(self, bg_color, widget_color, text_color, hover_color, border_color,
                       select_color, disabled_color, text_widget_color, scroll_handle_color):
        variables = f'''$bgcolor: {bg_color};
        $widgetcolor: {widget_color};
        $textcolor: {text_color};
        $hovercolor: {hover_color};
        $bordercolor: {border_color};
        $selectcolor: {select_color};
        $disabledcolor: {disabled_color};
        $textwidgetcolor: {text_widget_color};
        $scrollhandlecolor: {scroll_handle_color};
'''
        cur_dir = os.path.dirname(__file__)
        var_filename = os.path.join(cur_dir, 'var/variables.scss')
        with open(var_filename, 'w') as f:
            f.write(variables)

    def __getStyle(self, filename):
        cur_dir = os.path.dirname(__file__)
        sass_dirname = os.path.join(cur_dir, 'sass')
        # make temporary file
        temp_file = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
        css = qtsass.compile_filename(os.path.join(sass_dirname, filename), temp_file)
        return css

    def getThemeFiles(self, output_dir = os.getcwd()):
        cur_dir = os.path.dirname(__file__)
        sass_dirname = os.path.join(cur_dir, 'sass')
        qtsass.compile_dirname(sass_dirname, output_dir)

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

