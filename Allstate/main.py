# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:27:40 2016

@author: chzelada
"""

import pandas as pd
import numpy as np


from __future__ import division

iris=pd.read_csv("Iris.csv")
iris.head()


byspecies=iris.groupby("Species")   

byspecies.Species.count()

##¿Del total de carros que porcentaje tiene menos de k años?

iris.SepalLengthCm.describe()


filtro5 =  iris.SepalLengthCm<=5
filtro6 =  iris.SepalLengthCm<=6
filtro7 =  iris.SepalLengthCm<=7
filtro8 =  iris.SepalLengthCm<=8

#CDF
iris.SepalLengthCm[filtro5].count()/150
iris.SepalLengthCm[filtro6].count()/150
iris.SepalLengthCm[filtro7].count()/150
iris.SepalLengthCm[filtro8].count()/150

def CDF( k, data ):
   filtrok =  data.SepalLengthCm<=k
   out=data.SepalLengthCm[filtrok].count()/len(data)
   return out


vcdf = np.vectorize(CDF)

k = np.arange(3., 8., 0.1)


b

