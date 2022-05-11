# qt-sass-theme-getter
Qt sass theme getter. 

Default theme is dark-gray theme, my favorite.

## Setup
`python -m pip install qt-sass-theme-getter`

## Included Packages
* <a href="https://github.com/spyder-ide/qtsass">qtsass</a> - For convert sass into css

## Method Overview
* `setThemeColor(bg_color, widget_color, text_color, hover_color, border_color,
                       select_color, disabled_color, text_widget_color)` - you can set the theme color by yourself. <b>Give 6-digit hex color string such as #FF0000.</b>
  * bg_color - background color
  * widget_color - widget color
  * text_color - text color
  * hover_color - certain widgets' color when mouse cursor is hovering
  * border_color - color of widgets' border
  * select_color - selected widgets' color
  * disabled_color - disabled widgets' color
  * text_widget_color - background color of text widget such as `QTextEdit/QTextBrowser`
* `getThemeFiles(output_dir = os.getcwd())` - you can save css files in `output_dir` which were converted from .scss files included in this package.
* `getThemeStyle() -> str` - use it to `QMainWindow`, `QDialog`.
* `getIconButtonStyle() -> str` - use it to `QPushButton/QToolButton` which has icon.
* `getIconTextButtonStyle() -> str` - use it to `QPushButton/QToolButton`.
* `getMenuBarStyle() -> str` - use it to `QMenuBar`.
* `getMainWidgetStyle() -> str` - "top level" `QWidget`.

## Example
<a href="https://github.com/yjg30737/pyqt-dark-gray-theme/blob/main/pyqt_dark_gray_theme/darkGrayTheme.py">pyqt-dark-gray-theme</a> - return the sass styles after modification
<a href="https://github.com/yjg30737/pyqt-style-setter/blob/main/pyqt_style_setter/styleSetter.py">pyqt-style-setter</a> - set the style of some widgets
