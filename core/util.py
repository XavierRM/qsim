import numpy as np
from scipy.linalg import logm

def entropy(densityMatrix):
  return -np.trace(densityMatrix @ logm(densityMatrix)).real

def partialTrace(densityMatrix):
  dim = densityMatrix.shape[1]
  identity = np.eye(dim)
  
  return np.trace(np.einsum('ij,jk->ik', densityMatrix, identity))