from setuptools import setup, find_packages

setup(
    name='qt-sass-theme-getter',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'qt_sass_theme_getter.sass': ['theme.scss',
                                               'icon_button.scss',
                                               'icon_text_button.scss',
                                               'menu_bar.scss',
                                               'main_widget.scss'],
                  'qt_sass_theme_getter.var': ['variables.scss']
                  },
    description='Qt sass theme files',
    url='https://github.com/yjg30737/qt-sass-theme-getter.git',
    install_requires=[
        'qtsass'
    ]
)