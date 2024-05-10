import numpy as np
from Gates import swap

class QuantumRegister:
  def __init__(self, nqubits=int, stateVector=None):
    self.nqubits = nqubits
    if(stateVector is None):
      self.state = np.zeros(2**nqubits, dtype=np.complex256).reshape(-1, 1)
      self.state[0][0] = 1
    else:
      self.state = stateVector
    
  @staticmethod
  def combine(most, least):
    return QuantumRegister(most.nqubits + least.nqubits, np.kron(most.ket(), least.ket()))
  
  def ket(self):
    return self.state
  
  def bra(self):
    return self.state.transpose().conjugate()
  
  def densityMatrix(self):
    return np.dot(self.ket(), self.bra())
  
  def append(self, otherQReg):
    self.state = np.kron(self.state, otherQReg.ket())
  
  def measure(self, qubit):
    """
    Time complexity:
      O(5*2^n)
      ω(4*2^n)
    
    Space complexity:
      O(2^n)
      ω(2^n)
    
    n -> Number of qubits for our state
    """
    
    if(qubit < 0 or qubit >= self.nqubits):
      raise ValueError("Qubit out of bounds")

    l = [j for j in range(2**self.nqubits) if j//2**(qubit)%2]
    r = np.random.rand()
    p = sum(np.absolute(self.state[i, 0]) for i in l)
    
    auxL = [j for j in range(2**self.nqubits) if j//2**(qubit)%2 == 0] if r < p else l
    del l
    measureP = p if r < p else 1 - p
    
    for i in auxL:
        self.state[i, 0] = 0
        
    self.state = self.state/np.sqrt(measureP)
    
    return int(r < p)

  def applyGate(self, gateMatrix, index):
    """
    Time complexity depends on the numpy implementation and the optimizations it might have,
    but based on the definition of the dot product we can assess:
      O(2*2^n)
      ω(2*2^n)
    
    Space complexity:
      O(2^n)
      ω(2^n)
    
    n -> Number of qubits for our state
    """
    self.state = gateMatrix @ self.ket()
    return self
  
  def applyMQGate(self, gateM, qubits):
    gateQ = int(np.log2(gateM.shape[0]))
    
    if len(qubits) > self.nqubits:
      raise ValueError("Not enough qubits in register")
    
    if gateQ > self.nqubits:
      raise ValueError("Gate size is too big")
    
    if gateQ != len(qubits):
      raise ValueError("Gate size doesnt match positions to be applied")
    
    changes = None
    
    if len(qubits) > 1:
      changes = np.argsort(qubits + [i for i in range(self.nqubits) if i not in qubits])
      
      for i in range(len(qubits)):
        if i != changes[i]:
          self.applyMQGate(swap([np.abs(i - changes[i])]), [i])
    
    operation2 = np.kron(np.eye(2**(self.nqubits - gateQ)), gateM)
    
    self.state = operation2 @ self.ket()
    
    if changes is not None:
      for id in range(len(qubits)):
        target = np.where(changes == id)[0][0]
        if id != target:
          self.applyGate(swap(target - id), id)
          
    return self