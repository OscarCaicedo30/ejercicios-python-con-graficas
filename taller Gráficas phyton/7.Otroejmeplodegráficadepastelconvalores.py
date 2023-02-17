# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:29:16 2022

@author: USUARIO
"""

import matplotlib.pyplot as plt

librerias_python = ['Francia','Tailandia','Alemania','Turquía','Reino Unido','México','Italia','China','EEUU','España']
valores = [15.8,6.4,6.8,6.8,6.8,7.1,10.6,11.0,13.8,14.8]
colores = ['blue','coral','yellow','grey','pink','brown','purple','red','green','orange']
explode_vals = [0,0,0,0,0,0.23,0,0,0,0.23]

plt.pie(x=valores, labels=librerias_python, colors = colores, autopct='%1.2f%%', shadow=True,
explode = explode_vals)

plt.title('TOP 10 DESTINOS TURÍSTICOS EN 2017')

plt.show()