import random
import math
import matplotlib.pyplot as plt

# EJERCICIO 4
# Used https://timeseriesreasoning.com/contents/poisson-process/ as reference
# Constants
MU = 5
REPS = 100

# Variables
times_events = 0
event_list = []
intervals = []
times_array = []

# Cycle for all the 100 patients
for i in range(REPS):
	event_list.append(i)
	rand_val = random.random()
	time_e = -math.log(1.0 - rand_val) / MU
	intervals.append(time_e)
	times_events = times_events + time_e
	times_array.append(times_events)

# Plot
fig = plt.figure()
plot, = plt.plot(event_list, intervals, label='Number of the event')
plt.legend(handles=[plot])
plt.xlabel('Number of the event')
plt.ylabel('Time')
plt.show()
