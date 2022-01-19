# -*- coding: utf-8 -*-
"""
Desc : How to use Numba to speed up pandas dataframes
Ref : https://pandas.pydata.org/pandas-docs/stable/user_guide/enhancingperf.html
Ref : https://medium.com/swlh/6-ways-to-significantly-speed-up-pandas-with-a-couple-lines-of-code-part-1-2c2dfb0de230

Created on Thu Feb 11 08:41:21 2021
@author: chris.cirelli
"""


###############################################################################
# Import Libraries
###############################################################################
import pandas as pd
import numpy as np
import numba
from datetime import datetime

###############################################################################
# Functions
###############################################################################

# Example 1 : Create DataFrame w/ 100,000 rows and 4 columns filled w/ ran nums

seq = [x for x in range(0, 110, 10)]
vals = np.random.randint(0, 100, size=(100000))

@numba.jit
def test_iter_list(vals):
    for i in vals:
        pass

start = datetime.now()
result = test_iter_list(vals)
duration = (datetime.now() - start).total_seconds()
print(f'duration => {duration}')