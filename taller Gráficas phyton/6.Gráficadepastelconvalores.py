# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:23:44 2022

@author: USUARIO
"""

import matplotlib.pyplot as plt

etiquetas = ['Juan','Diana','Catalina','Ana']
valores = [11.8,29.4,35.3,23.5]
colores = ['orange','green','red','blue']

plt.pie(x=valores, labels=etiquetas, colors=colores, autopct='%1.2f%%')

plt.title('Ejercicio propuesto')

plt.show()