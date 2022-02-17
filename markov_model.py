import numpy as np

b = 1000 #The intitial upper bound for X_1

def never_increase(b):
  #Construct transition matrix P
  P = np.empty([b,b])

  for i in range(b):
    for j in range(b):

      if i < j:
        P[i,j] = 0

      else:
        P[i,j] = 1/(b-j)

  P = P.T
  
  #Construct Q, the transition state for moving from one transient state to an other
  Q = P[:-1, :-1]

  #Calculate N, the matrix of the average number of visits between two transient nodes
  I = np.identity(Q.shape[0])
  N = I - Q
  N = np.linalg.inv(N)

  return(sum(N[0,:]))


