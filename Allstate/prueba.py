# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:47:37 2016

@author: chzelada
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

allstate=pd.read_csv("allstate.csv")
filtro=allstate.record_type==1
bystate=allstate[filtro].groupby("state")

bystate.shopping_pt.agg([np.sum,np.mean,np.std,len,np.max,np.min])
