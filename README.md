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
Currently there are 4 official theme being supported:
* dark_gray
* dark_blue
* light_gray
* light_blue

You can also make your own theme with [customizing theme](#customizing-theme).

`background_darker` decides whether the background color is going to be darker than general widget color or not.

If that is set to `True`, background color is darker than general widget color. See image below.

![image](https://user-images.githubusercontent.com/55078043/174504700-64b16154-5e99-48bd-ac92-24a13f90db86.png)

If that is set to `False`(which is set by default), background color is lighter than general widget color. See image below.

![image](https://user-images.githubusercontent.com/55078043/174504676-7281bbc9-7abf-49ce-99c7-68cdb9c2badf.png)

`output_path` is the path that 'res' directory will be made which is holding a bunch of theme files after you called `getThemeFiles`.

'res' directory looks like below.

![image](https://user-images.githubusercontent.com/55078043/174504918-43e66f7f-21cb-4555-a446-7a476b69d62e.png)

`ico` directory holds icon files which will be being used in theme. For example, light icons will be being used in dark theme, dark icons will be being used in light theme. `_icons.scss` makes sass files in `sass` directory refer to icons in this directory.

`sass` directory holds the scss files which will be converted into css files.

`var` directory holds the `_variables.scss` which contains the color(e.g. color of background/widget/border...) variables. 

<hr>

#### `setThemeFiles(main_window: QWidget, input_path='res', exclude_type_lst: list = [])`
Right after calling `getThemeFiles`, you can set the style with calling `setThemeFiles`.

After calling it, 'res' directory looks like this:

![image](https://user-images.githubusercontent.com/55078043/174504820-b6262c1e-e1b8-4c56-8c98-1f8c93d87175.png)

scss files successfully convert into css files.

Note: Don't change the current directory with function such as `os.chdir` after calling `getThemeFiles` and before calling `setThemeFiles`. `FileNotFoundError` will be most likely occurred.

### Customizing Theme

There are two ways to customize theme.

#### 1. Giving color string to <a href="https://github.com/yjg30737/qtsasstheme#getthemefilestheme-str--dark_gray-background_darkerfalse-output_pathosgetcwd">`getThemeFiles`</a>

You can give the 6-digit hex string(e.g. #FF0000) to `getThemeFiles`'s `theme` argument.

In this case, widget's color will be set based on the hex color you given.

This is the way how to do it:

```python
//..
app = QApplication(sys.argv)
w = SampleWidget()
g = QtSassTheme()
g.getThemeFiles(theme='#6f495f')
g.setThemeFiles(w)
w.show()
app.exec_()
```

![image](https://user-images.githubusercontent.com/55078043/174504721-ae3f905c-831f-42c2-82a6-d2e966ec38a3.png)

#### 2. Modify `_variables.scss`'s color directly

This is the way how to do it:

1. Calling `getThemeFiles`
```python
g = QtSassTheme()
g.getThemeFiles() 
```

![image](https://user-images.githubusercontent.com/55078043/174504918-43e66f7f-21cb-4555-a446-7a476b69d62e.png)

'res' directory like above will be generated. You can see `_variables.scss`.

2. Change the variables

open the `_variables.scss` and change the `$bgcolor`'s value.

This is `_variables.scss`'s contents(dark-gray theme).

```scss
$bgcolor: #555555;
$widgetcolor: darken($bgcolor, 10);
$altwidgetcolor: lighten($widgetcolor, 18);
$textcolor: #DDDDDD;
$hovercolor: lighten($widgetcolor, 6);
$bordercolor: lighten($widgetcolor, 20);
$selectcolor: darken($widgetcolor, 6);
$disabledcolor: #AAAAAA;
$textwidgetcolor: darken($widgetcolor, 12);
$scrollhandlecolor: lighten($widgetcolor, 30);
$splitterhandlecolor: darken($widgetcolor, 10);
```

You can change any colors.

In this example i will change the $bgcolor from #555555 to #006600(dark-green).

3. Calling `setThemeFiles`
```python
//..
app = QApplication(sys.argv)
w = SampleWidget()
g = QtSassTheme()
g.setThemeFiles(w)
w.show()
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

![image](https://user-images.githubusercontent.com/55078043/174504676-7281bbc9-7abf-49ce-99c7-68cdb9c2badf.png)

Dark blue theme

![image](https://user-images.githubusercontent.com/55078043/172755432-c3d552a8-4d93-43b8-a5d6-fd0ed6ff7d2d.png)

Light gray theme

![image](https://user-images.githubusercontent.com/55078043/172755465-be037efa-87df-4d38-b8e8-de9b47015fba.png)

Light blue theme

![image](https://user-images.githubusercontent.com/55078043/172755492-519c485b-54b9-4d87-aede-b64986c2ae90.png)
