import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set some pandas options.  For full list and defaults:
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

for option in options:
    for category, value in options[option].items():
        pd.set_option('{0}.{1}'.format(option, category), value)

for category, option in options.items():
    for op, value in option.items():
        pd.set_option('{0}.{1}'.format(category, op), value)
