# qt-sass-theme-getter
Qt sass theme getter. 

Default theme is dark-gray theme, my favorite.

## Setup
`python -m pip install qt-sass-theme-getter`

## Included Packages
* <a href="https://github.com/spyder-ide/qtsass">qtsass</a> - for converting sass into css
* <a href="https://github.com/yjg30737/pyqt-svg-button">pyqt-svg-button</a> - for supporting svg button

## Method Overview
* `getThemeFiles(theme: str = 'dark', output_path=os.getcwd())`
* `setThemeFiles(main_window: QWidget, input_path='res', exclude_type_lst: list = [])`

Theme files will be saved in 'res' subdirectory of `output_path` after you called `getThemeFiles`.

## Example
### Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_timer.settingsDialog import SettingsDialog
from qt_sass_theme_getter import QtSassThemeGetter


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = SettingsDialog()
    g = QtSassThemeGetter()
    g.getThemeFiles(theme='light') # theme='dark'
    g.setThemeFiles(main_window=widget)
    widget.show()
    app.exec_()
```

### Result
Light theme

![image](https://user-images.githubusercontent.com/55078043/171834443-45fd1c72-2a67-4569-a47f-62d197a40610.png)


Dark theme

![image](https://user-images.githubusercontent.com/55078043/171834481-c28c8c1c-dcf7-4d29-8a8a-163d446be2af.png)


*
*
*
*
*
*
*
*
*
*
*
*


#### Old Functions (potentially deprecated)
* `getThemeStyle() -> str` - use it to `QMainWindow`, `QDialog`.
* `getIconButtonStyle() -> str` - use it to `QPushButton/QToolButton` which has icon.
* `getIconTextButtonStyle() -> str` - use it to `QPushButton/QToolButton`.
* `getMenuBarStyle() -> str` - use it to `QMenuBar`.
* `getMainWidgetStyle() -> str` - use it to "top level" `QWidget`.

#### Old Example
Here's basic usage - get the style code and modify it(such as getThemeStyle() + QLineEdit { ... }), and set it to desired widget.

<a href="https://github.com/yjg30737/pyqt-dark-gray-theme/blob/main/pyqt_dark_gray_theme/darkGrayTheme.py">pyqt-dark-gray-theme/darkGrayTheme.py</a> - return the dark-gray styles using qt-sass-theme-getter pacakge, even though dark-gray is default.

<a href="https://github.com/yjg30737/pyqt-style-setter/blob/main/pyqt_style_setter/styleSetter.py">pyqt-style-setter/styleSetter.py</a> - set the style of some widgets
