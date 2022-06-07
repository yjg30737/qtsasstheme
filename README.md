# qtsasstheme
Set the Qt theme (e.g. darkgray/lightgray/darkblue/lightblue) easily

This is using SCSS to set the light/dark theme to PyQt GUI, which is quite efficient.

Old name of this is `qt-sass-theme-getter`.

## Setup
`python -m pip install qtsasstheme`

## Included Packages
* <a href="https://github.com/spyder-ide/qtsass">qtsass</a> - for converting sass into css
* <a href="https://github.com/yjg30737/pyqt-svg-button">pyqt-svg-button</a> - for supporting svg button

## Method Overview
#### `getThemeFiles(theme: str = 'dark_gray', output_path=os.getcwd())`
Supporting theme: 
* dark_gray
* dark_blue
* light_gray
* light_blue

Theme files will be saved in 'res' directory of `output_path` after you called `getThemeFiles`.

'res' directory looks like this:

![image](https://user-images.githubusercontent.com/55078043/172268659-860a5633-7b73-4848-92c4-b946b035b75a.png)

`ico` directory holds icon files which will be being used in theme. For example, light icons will be being used in dark theme, dark icons will be being used in light theme. `_icons.scss` makes sass files in `sass` directory refer to icons in this directory.

`sass` directory holds the scss files which will be converted into css files.

`var` directory holds the `_variables.scss` which contains the color(e.g. color of background/widget/border...) variables. You can change the `_variables.scss`'s variables whatever you want, if you want to set custom variables.

<hr>

#### `setThemeFiles(main_window: QWidget, input_path='res', exclude_type_lst: list = [])`
Right after calling `getThemeFiles`, you can set the style with calling `setThemeFiles`.

After calling it, 'res' directory looks like this:

![image](https://user-images.githubusercontent.com/55078043/172270071-d49a246a-7efb-463b-b0f8-bb70179a75f6.png)

scss files successfully convert into css files.

Note: Don't change the current directory with function such as `os.chdir` after calling `getThemeFiles` and before calling `setThemeFiles`. `FileNotFoundError` will be most likely occurred. 

## Example
### Code Sample

```python
from PyQt5.QtWidgets import QApplication
from pyqt_timer.settingsDialog import SettingsDialog
from qt_sass_theme import QtSassTheme

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = SettingsDialog()
    g = QtSassTheme()
    g.getThemeFiles(theme='dark_gray')
    # g.getThemeFiles(theme='dark_blue') - if you want to set dark blue theme
    g.setThemeFiles(main_window=widget)
    widget.show()
    app.exec_()
```

### Result
Dark gray theme

![image](https://user-images.githubusercontent.com/55078043/172339386-e7306141-af73-41db-a27d-e7145ba474f6.png)

Dark blue theme

![image](https://user-images.githubusercontent.com/55078043/172339085-a4236c09-bff5-4087-ad48-6548ebbe469a.png)

Light gray theme

![image](https://user-images.githubusercontent.com/55078043/172339438-6c290c9d-7d37-42f4-9005-c947593edf5e.png)

Light blue theme

![image](https://user-images.githubusercontent.com/55078043/172339501-0a584c5a-7b50-4517-a8ff-fc3307d5b733.png)
