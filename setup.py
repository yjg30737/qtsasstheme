from setuptools import setup, find_packages

setup(
    name='qt-sass-theme-files',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'qt_sass_theme_files': ['theme.scss',
                                          'icon_button.scss',
                                          'icon_text_button.scss',
                                          'menu_bar.scss',
                                          'main_widget.scss',
                                          'variables.scss'],
                  'qt_sass_theme_files.var': ['variables.scss']
                  },
    description='Qt sass theme files',
    url='https://github.com/yjg30737/qt-sass-theme-files.git',
    install_requires=[
        'qtsass'
    ]
)