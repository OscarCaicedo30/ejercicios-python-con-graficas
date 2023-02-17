# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:18:41 2022

@author: USUARIO
"""

import matplotlib.pyplot as plt

etiquetas = ['Juan','Diana','Catalina','Ana']
valores = [45,80,165,70]
colores = ['orange','green','red','blue']

plt.pie(x=valores, labels=etiquetas,colors=colores)
plt.title('Ejercicio Propuesto')
plt.show()