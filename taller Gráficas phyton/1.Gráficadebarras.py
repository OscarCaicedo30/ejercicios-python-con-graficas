# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:13:21 2022

@author: USUARIO
"""

import matplotlib.pyplot as plt

eje_x = ['Baloncesto','Fútbol','Balonmano','Tenis','Atletismo','Voleibol','Natación']

eje_y = [12,8,10,6,3,5,6]

plt.bar(eje_x, eje_y)

plt.ylabel('Frecuencia Absoluta')

plt.xlabel('Deporte preferido')

plt.title('Deportes vs Frecuencia')

plt.show()