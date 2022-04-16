import os

import qtsass


def get_theme(output_dir = os.getcwd()):
    dirname = os.path.dirname(os.path.join(__file__, 'sass'))
    qtsass.compile_dirname(dirname, output_dir)