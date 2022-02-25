import numpy as np

#Recursive function, takes upper bound as p[aremeter. Returns expectred number of stps as a float
def func(x):

  if x == 1:
    return 0
  
  frac = 1/(x - 1)
  sum = frac

  for i in range(1, x):
    sum += frac * (1 + func(i))

  return sum


