import numpy as np
from math import exp
from scipy.stats import gamma
import matplotlib.pyplot as plt
x = [x_dot for x_dot in range(0, 5)]
params = [2, 1, 0.5]

for _lambda in params:
  plt.title('lambda = ' + str(_lambda))
  plt.plot(x, gamma.pdf(x, a = 3, scale=1/_lambda), 'r', lw=5, alpha=1, label='gamma pdf')
  plt.show()