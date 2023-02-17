# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:49:04 2022

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt

serie_1 = [6,14,4]
serie_2 = [8,4,10]

numero_de_grupos = len(serie_1)
indice_barras = np.arange(numero_de_grupos)
ancho_barras = 0.35

plt.bar(indice_barras, serie_2, width=ancho_barras, label='Masculino')
plt.bar(indice_barras + ancho_barras, serie_2, width=ancho_barras, label='Femenino')
plt.legend(loc='best')

plt.xticks(indice_barras + ancho_barras, ('Lengua Extranjeras','Licenciatura en matemáticas','Enfermería'))

plt.ylabel('Cantidad de Estudiantes')
plt.xlabel('Profesion')
plt.title('Diagrama de barras para las variables inclinación profresional y género')
plt.show()


