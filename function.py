import numpy as np

def func(x):

  if x == 1:
    return 0
  
  frac = 1/(x - 1)
  sum = frac

  for i in range(1, x):
    sum += frac * (1 + func(i))

  return sum


