import numpy as np
import pandas as pd
from random import random
from math import log
from scipy.stats import expon
import matplotlib.pyplot as plt

def getArrivalTime(p, _lambda):
  return - log(1 - p) / _lambda

# Makes tables
_lambda = 5

time = 0
times = []
patient = 1
for i in range(1, 501):
  p = random()
  arrivalTime = getArrivalTime(p, _lambda)
  time += arrivalTime
  times.append(
    [patient, p, arrivalTime, time]
  )
  patient += 1
df = pd.DataFrame(times, columns = ['Paciente', 'Random', 'Tiempo de llegada', 'Tiempo acumulado'])
print(df.head(10).to_string(index=False))

x = np.arange(0, 2.5, 0.1)
# pmf
plt.plot(x, expon.cdf(x, scale=1/_lambda))

# cdf
x = np.arange(0, 500)
plt.plot(x, df['Tiempo acumulado'])

plt.show()