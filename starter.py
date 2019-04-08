
"""
The following python module has important libraries that I use in my analysis
"""


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import os
import re
import matplotlib.pyplot as plt
import math
import datetime as dt
import pandas_profiling as pp
import uszipcode as usz
from uszipcode import SearchEngine
search = SearchEngine(simple_zipcode=True) 
# Code to display all columns for the dataset
pd.set_option('display.max_columns',False)
# Date on which the analysis is performed, will be used for version control
dt_now = dt.datetime.today().strftime('%Y-%m-%d %H.%M')
