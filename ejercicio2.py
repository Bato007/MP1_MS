from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

# EJERCICIO 2
# Constant variables
MU = 2

# Created array with numbers from 0 to 100
range_array = np.arange(101)

# Used poisson to get the data
data = poisson.pmf(range_array, MU)
print(data)

# Plot the data
plt.plot(data)
plt.show()
