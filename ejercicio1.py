import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(1, 1)
fig, ax2 = plt.subplots(1, 1)

mu = 7
rv = poisson(mu)
x = [x_dot for x_dot in range(0, 17)]

# pmf
ax1.plot(x, poisson.pmf(x, mu), 'b', ms=8, label='poisson pmf')
ax1.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)

# cdf
ax2.plot(x, poisson.cdf(x, mu), 'b', ms=8, label='poisson cdf')
ax2.vlines(x, 0, poisson.cdf(x, mu), colors='b', lw=5, alpha=0.5)
plt.show()