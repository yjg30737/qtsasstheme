# qt-sass-theme-getter
Qt sass theme getter. 

This is using SCSS to set the light/dark theme to PyQt GUI, which is quite efficient.

## Setup
`python -m pip install qt-sass-theme-getter`

## Included Packages
* <a href="https://github.com/spyder-ide/qtsass">qtsass</a> - for converting sass into css
* <a href="https://github.com/yjg30737/pyqt-svg-button">pyqt-svg-button</a> - for supporting svg button

## Method Overview
### `getThemeFiles(theme: str = 'dark', output_path=os.getcwd())`
This supported only two theme currently. 
* dark
* light
Theme files will be saved in 'res' subdirectory of `output_path` after you called `getThemeFiles`.

### `setThemeFiles(main_window: QWidget, input_path='res', exclude_type_lst: list = [])`
Right after calling `getThemeFiles`, you can set the style with calling `setThemeFiles`.

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

![image](https://user-images.githubusercontent.com/55078043/171988935-676ea36c-657a-403c-be7a-93c89cb60d6b.png)

Dark theme

![image](https://user-images.githubusercontent.com/55078043/171988919-d3d4148f-02fa-4322-9d8e-a52e2b2a0a55.png)
