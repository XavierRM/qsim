import numpy as np

class QuantumRegister:
  def __init__(self, nqubits=int):
    self.nqubits = nqubits
    self._state = np.zeros(2**nqubits, dtype=complex).reshape(-1, 1)
    self._state[0][0] = 1
  
  def ket(self):
    return self._state
  
  def bra(self):
    return self._state.transpose().conjugate()
  
  def densityMatrix(self):
    return np.dot(self.ket(), self.bra())