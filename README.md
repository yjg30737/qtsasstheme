# qt-sass-theme-getter
Qt sass theme getter. Default theme is <a href="https://github.com/yjg30737/pyqt-dark-gray-theme.git">pyqt-dark-gray-theme</a>, my favorite.

## Install
`python -m pip install qt-sass-theme-getter`

## Included Packages
* <a href="https://github.com/spyder-ide/qtsass">qtsass</a> - For convert sass into css

## Method Overview
* `setThemeColor(bg_color, widget_color, text_color, hover_color, border_color,
                       select_color, disabled_color, text_widget_color)`
* `getThemeFiles(output_dir = os.getcwd())`
* `getThemeStyle()`
* `getIconButtonStyle()`
* `getIconTextButtonStyle()`
* `getMenuBarStyle()`
* `getMainWidgetStyle()`

I firmly believe that is self-explanatory.
