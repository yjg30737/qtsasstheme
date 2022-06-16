# qtsasstheme
Set the Qt theme (e.g. darkgray/lightgray/darkblue/lightblue) easily

This is using SCSS to set the light/dark theme to PyQt GUI, which is quite efficient.

Old name of this is `qt-sass-theme-getter`.

## Setup
`python -m pip install qtsasstheme`

## Included Packages
* <a href="https://github.com/spyder-ide/qtsass">qtsass</a> - for converting sass into css
* <a href="https://github.com/yjg30737/pyqt-svg-button">pyqt-svg-button</a> - for supporting svg button

## Detailed Description 
### Method Overview
#### `getThemeFiles(theme: str = 'dark_gray', background_darker=False, output_path=os.getcwd())`
Available value of theme argument:
* dark_gray
* dark_blue
* light_gray
* light_blue

You can also make your own theme with [customizing theme](#customizing-theme).

`background_darker` decides whether the background color is going to be darker than general widget color or not.

If that is set to `True`, background color is darker than general widget color. See image below.

![image](https://user-images.githubusercontent.com/55078043/174045178-0bccbf7d-1141-4a6b-90b6-3ad9ee4e8281.png)

If that is set to `False`(which is set by default), background color is lighter than general widget color. See image below.

![image](https://user-images.githubusercontent.com/55078043/174045272-7e92594f-abc0-44e4-b2ea-c0fb9d3f520c.png)

`output_path` is the path that 'res' directory will be made which is holding a bunch of theme files after you called `getThemeFiles`.

'res' directory looks like this:

![image](https://user-images.githubusercontent.com/55078043/172268659-860a5633-7b73-4848-92c4-b946b035b75a.png)

`ico` directory holds icon files which will be being used in theme. For example, light icons will be being used in dark theme, dark icons will be being used in light theme. `_icons.scss` makes sass files in `sass` directory refer to icons in this directory.

`sass` directory holds the scss files which will be converted into css files.

`var` directory holds the `_variables.scss` which contains the color(e.g. color of background/widget/border...) variables. 

<hr>

#### `setThemeFiles(main_window: QWidget, input_path='res', exclude_type_lst: list = [])`
Right after calling `getThemeFiles`, you can set the style with calling `setThemeFiles`.

After calling it, 'res' directory looks like this:

![image](https://user-images.githubusercontent.com/55078043/172270071-d49a246a-7efb-463b-b0f8-bb70179a75f6.png)

scss files successfully convert into css files.

Note: Don't change the current directory with function such as `os.chdir` after calling `getThemeFiles` and before calling `setThemeFiles`. `FileNotFoundError` will be most likely occurred.

### Customizing Theme

If you want to set customized theme, do it with changing the `_variables.scss`'s variables.

This is the way how to do it:

1. Calling `getThemeFiles`
```python
g = QtSassTheme()
g.getThemeFiles() 
```

![image](https://user-images.githubusercontent.com/55078043/172735025-7bf78c88-3f42-4bfc-8c00-726bdef764a5.png)

'res' directory like above will be generated.

2. Change the variables

open the `_variables.scss` and change the `$bgcolor`'s value.

This is `_variables.scss`'s contents(dark-gray theme).

```scss
$bgcolor: #444444;
$widgetcolor: darken($bgcolor, 10);
$altwidgetcolor: lighten($widgetcolor, 18);
$textcolor: #DDDDDD;
$hovercolor: lighten($widgetcolor, 3);
$bordercolor: lighten($widgetcolor, 20);
$selectcolor: darken($widgetcolor, 3);
$disabledcolor: #AAAAAA;
$textwidgetcolor: darken($widgetcolor, 15);
$scrollhandlecolor: lighten($widgetcolor, 20);
$splitterhandlecolor: darken($widgetcolor, 10);
```

You can change any colors.

In this example i will change the $bgcolor from #444444 to #006600(dark-green).

3. Calling `setThemeFiles`
```python
app = QApplication(sys.argv)
w = SampleWidget()
g.setThemeFiles(w)
app.exec_()
```

![image](https://user-images.githubusercontent.com/55078043/172736296-a78a32fa-1a1a-403a-a11c-1de29b372316.png)


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

![image](https://user-images.githubusercontent.com/55078043/174045367-a1f53224-9ca0-40f0-bfa0-c41c6f3956e9.png)

Dark blue theme

![image](https://user-images.githubusercontent.com/55078043/172755432-c3d552a8-4d93-43b8-a5d6-fd0ed6ff7d2d.png)

Light gray theme

![image](https://user-images.githubusercontent.com/55078043/172755465-be037efa-87df-4d38-b8e8-de9b47015fba.png)

Light blue theme

![image](https://user-images.githubusercontent.com/55078043/172755492-519c485b-54b9-4d87-aede-b64986c2ae90.png)
