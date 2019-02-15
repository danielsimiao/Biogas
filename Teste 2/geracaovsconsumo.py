# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 23:18:29 2019

@author: Daniel
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tempo = np.array([1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001])
consumo = np.array([201474,205310,214429,218425,227121,235627,249120,260111,276186,287392,291858,307449,283798])
geracao = np.array([210635,211044,221912,228711,237933,245863,260659,273301,288845,301160,308508,322899,296237])

d = {'Geração(MW)': geracao, 'Consumo(MW)': consumo}

dataset = pd.DataFrame(d,index=tempo)
print(dataset)

dataset.plot(y=['Geração(MW)', 'Consumo(MW)'],title='Consumo e geração de Energia no Brasil',kind='bar', legend=True, grid=True, color=['b','r'], width=1)
plt.savefig('comparacao.png')
plt.show()
plt.close()