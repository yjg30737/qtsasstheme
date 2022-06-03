from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='qt-sass-theme-getter',
    version='0.0.30',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'qt_sass_theme_getter.sass': ['theme.scss',
                                               'icon_button.scss',
                                               'icon_text_button.scss',
                                               'menu_bar.scss',
                                               'main_widget.scss'],
                  'qt_sass_theme_getter.var': ['_variables.scss'],
                  'qt_sass_theme_getter.var.dark': ['_variables.scss'],
                  'qt_sass_theme_getter.var.light': ['_variables.scss'],
                  'qt_sass_theme_getter.ico': ['_icons.scss', 'check.svg', 'close.svg'],
                  'qt_sass_theme_getter.ico.dark': ['_icons.scss', 'check.svg', 'close.svg'],
                  'qt_sass_theme_getter.ico.light': ['_icons.scss', 'check.svg', 'close.svg']
                  },
    description='Qt sass theme getter',
    url='https://github.com/yjg30737/qt-sass-theme-getter.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'qtsass',
        'pyqt-svg-button>=0.0.1'
    ]
)