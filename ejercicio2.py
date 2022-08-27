# EJERCICIO 2
# ¿Puede ser este evento modelado por una distribución de Poisson? ¿Por qué
# El evento si puede ser modelado por una distribución de Poisson, ya que 
# cumple con el requisito de ser que los eventos ocurren en un cierto periodo de tiempo
# siendo estos eventos independientes unos de otros.

from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

# Constant variables
MU = 2

# Created array with numbers from 0 to 100
range_array = np.arange(101)

# Used poisson to get the data
data = poisson.pmf(range_array, MU)

# Plot the data
plt.plot(data)
plt.show()

# EJERCICIO 4
patients = np.arange(101)