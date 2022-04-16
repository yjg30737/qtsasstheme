import os

import qtsass


def get_theme():
    dirname = os.path.dirname(__file__)
    qtsass.compile_dirname(dirname, os.getcwd())