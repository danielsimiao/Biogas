# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:53:09 2019

@author: Daniel
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Estados Brasileiros
uf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
      'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
      'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

#Populão por Estado
pop = np.array([872.722,3327.015,833.361, 4096.924, 14829.478, 9090.771, 
                 2982.237, 3984.102, 6947.696, 7046.266, 341.969, 2755.677,
                 21074.409, 8537.906, 4001.064, 11369.379, 9513.918, 3226.285, 
                 17185.354, 3486.617, 11339.993, 1762.505, 583.578, 7097.02, 
                 45632.459, 2283.893, 156.179])

#função interpolada - qtd de energia de biogas propocional ao numero de habitantes
def energia(x):
    a = 0.5*(x-270)/(135-270) + 1*(x-135)/(270-135)
    return a

pot = energia(pop)

dataset = pd.DataFrame(
        {'População(Mil)': pop, 'Potência(MW)': pot}
        ,index=uf)

print(dataset)

dataset.plot(y='Potência(MW)',kind='bar', legend=False, grid=True)
plt.show()