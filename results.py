import numpy as np
import matplotlib.pyplot as plt

from markov_model import never_increase
from function import func

bounds = np.array([5,10,15,20])
expected_steps = np.empty_like(bounds, dtype='float32')

for i in range(len(bounds)):
  expected_steps[i] = never_increase(bounds[i])

print(bounds)
print(expected_steps)
  
recursive_method = np.empty_like(bounds, dtype='float32')

for i in range(len(bounds)):
  recursive_method[i] = func(bounds[i])

print(recursive_method)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(bounds, expected_steps)
ax1.set_title("Absorbing Markov Model")

ax2.plot(bounds, recursive_method)
ax2.set_title("Recursive Method")
plt.show()


