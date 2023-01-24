from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='qtsasstheme',
    version='0.0.65',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    # package_data = {package_name: ['*.scss'] for package_name in find_packages()},
    package_data={'qt_sass_theme.sass': ['theme.scss',
                                         'icon_button.scss',
                                         'icon_text_button.scss',
                                         'menu_bar.scss'],
                  'qt_sass_theme.var': ['_variables.scss'],
                  'qt_sass_theme.var.dark.dark_gray': ['_variables.scss'],
                  'qt_sass_theme.var.dark.dark_blue': ['_variables.scss'],
                  'qt_sass_theme.var.light.light_gray': ['_variables.scss'],
                  'qt_sass_theme.var.light.light_blue': ['_variables.scss'],
                  'qt_sass_theme.ico': ['_icons.scss', 'check.svg', 'close.svg', 'down.svg', 'left.svg', 'right.svg', 'up.svg', 'circle-solid.svg'],
                  'qt_sass_theme.ico.dark': ['_icons.scss', 'check.svg', 'close.svg', 'down.svg', 'left.svg', 'right.svg', 'up.svg', 'circle-solid.svg'],
                  'qt_sass_theme.ico.light': ['_icons.scss', 'check.svg', 'close.svg', 'down.svg', 'left.svg', 'right.svg', 'up.svg', 'circle-solid.svg']
                  },
    description='Set the Qt theme (e.g. darkgray/lightgray/darkblue/lightblue) easily',
    url='https://github.com/yjg30737/qtsasstheme.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'qtpy',
        'qtsass',
    ]
)