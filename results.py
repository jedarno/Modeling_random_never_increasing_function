import numpy as np
import matplotlib.pyplot as plt

from markov_model import never_increase

bounds = np.array([10,50,100,150,200,400,600,800,1000,1200,1400,1600,1800,2000,2400,2800,3200,3600,4000])
expected_steps = np.empty_like(bounds, dtype='float32')

for i in range(len(bounds)):
  expected_steps[i] = np.exp(never_increase(bounds[i]))

print(bounds)
print(expected_steps)
plt.plot(bounds, expected_steps)
plt.xlabel("Initial upper bound x_0")
plt.ylabel("Expected number of steps to reach 1")
plt.show()
  
