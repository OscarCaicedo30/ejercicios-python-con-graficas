# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:20:57 2022

@author: USUARIO
"""

import matplotlib.pyplot as plt

eje_x = ['Blue','Blue-Gray','Brown','Dark','Hazel','Yellow']

eje_y = [12,2,17,2,3,3]

plt.barh(eje_x, eje_y, color="blue")
plt.ylabel('Eye_color')
plt.xlabel('Count')
plt.title('Color vs Count')
plt.show()

