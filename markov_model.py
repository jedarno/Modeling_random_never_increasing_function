import numpy as np

"""
Function to return expected number of steps before reaching 1. Paramater b
is the upper bound. Returns a float.
"""
def never_increase(b):
  #Construct transition matrix P
  P = np.empty([b,b])

  for j in range(b):
    P[:,j] = 1/(b - j)

  P = np.tril(P)
  P = P.T
  Q = P[:-1, :-1] #Construct Q, the transition matrix for moving between transient states

  #Calculate N, the matrix of the average number of visits between two transient nodes
  I = np.identity(Q.shape[0])
  N = I - Q
  N = np.linalg.inv(N)

  return(sum(N[0,:]))


