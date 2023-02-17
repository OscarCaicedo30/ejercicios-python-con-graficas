# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:09:20 2022

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt 
grupos = ['Primaria','Secundaria','Terciaria']
mujeres = [85,62,38]
hombres = [15,38,62]

indice = np.arange(len(grupos))

plt.bar(indice,mujeres,label='Mujeres')

plt.bar(indice,hombres,label='Hombres',bottom=mujeres)

plt.xticks(indice,grupos)
plt.ylabel("Genero")
plt.xlabel("Tipos de instituciones de educación")
plt.title('Brecha de género en el profesorado en Irlanda,2005-2006')

plt.show()