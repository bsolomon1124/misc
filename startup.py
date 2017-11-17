"""IPython startup file.  Place in .ipython/profile_default/startup/"""

import os

import matplotlib.pyplot as plt  # NOQA
import numpy as np
import pandas as pd
import scipy.stats as scs  # NOQA

# Just a convenience msg on startup: "Namespace: os, plt, np, pd, scs"
excl = ('In', 'Out', 'get_ipython', 'exit', 'quit', 'excl')
imports = [key for key in globals().copy() if not key.startswith('_')
           and key not in excl]
print('Namespace:', ', '.join(imports))

# Make sure network drive exists.
# If it does, map to it and try cd'ing to it.
if not os.path.exists('Z:'):
    print(r'Mapping \\na2prod\userdocs\bsolomon to Z:.')
    if not os.path.exists(r'\\na2prod\userdocs'):
        print("Cannot map; directory doesn't exist.")
    else:
        os.system(r'net use Z: \\na2prod\userdocs\bsolomon')
try:
    os.chdir('Z:/_python')
except FileNotFoundError:
    pass
print('Current directory:', os.getcwd())

# pandas options -------------------------------------------------------
# For full list and defaults:
# https://pandas.pydata.org/pandas-docs/stable/options.html#available-options
# Reference by full path here to avoid regex conflict with options
#     added in the future.
# Skipped here: 'html', 'io', & 'compute'.

options = {
    'display': {
        'max_columns': None,
        'max_rows': 25,
        'max_seq_items': 50,
        'precision': 3,
        'show_dimensions': False
        },
    'mode': {
        'chained_assignment': None
        }
    }

for category, option in options.items():
    for op, value in option.items():
        pd.set_option('{0}.{1}'.format(category, op), value)

# NumPy print options --------------------------------------------------
# `suppress`:
# - False: x**2 - (x + eps)**2 --> array([ -4.930e-32,  -4.440e-16, ...
# - True: x**2 - (x + eps)**2 --> array([-0., -0.,  0.,  0.])
# Defaults:
# np.set_printoptions(edgeitems=3, infstr='inf',
#     linewidth=75, nanstr='nan', precision=8,
#     suppress=False, threshold=1000, formatter=None)

np.set_printoptions(
    precision=3,
    threshold=625,
    edgeitems=10,
    )
