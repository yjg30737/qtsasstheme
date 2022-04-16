import os

import qtsass


def get_theme(output_dir = os.getcwd()):
    dirname = os.path.dirname(__file__)
    qtsass.compile_dirname(dirname, output_dir)