import numpy as np
import random

class QuantumRegister:
    def __init__(self, nqubits, dm=None):
        self.nqubits = nqubits
        
        if dm is None:
            self.dm = np.zeros((2**nqubits, 2**nqubits), dtype=np.complex256)
            self.dm[0][0] = 1
        else:
            self.dm = dm
        
    def matrix(self):
        return self.dm
    
    def applyGate(self, gate, qubit):
        identity = np.array([[1, 0], [0, 1]])
        finalGate = None
        
        if(qubit == 0):
            finalGate = gate
        else:
            finalGate = np.zeros((2, 2), dtype=np.complex256)
            finalGate[0][0] = 1
            finalGate[1][1] = 1        

        for i in range(1, self.nqubits):
            finalGate = np.kron(gate if (i == qubit) else identity, finalGate)
                
        return QuantumRegister(self.nqubits, finalGate @ self.dm @ finalGate.conj().T)

    def applyNQGate(self, gate, qubits):        
        for i in range(0, len(qubits)):
            index = i*2
            gateToApply = gate[index:index+2, index:index+2]
            self = self.applyGate(gateToApply, qubits[i])
            
        return QuantumRegister(self.nqubits, self.dm)
    
    def measure(self, qubit):
        p = 0
        mask = 1 << qubit
        
        for i in range(2**self.nqubits):
            p += self.dm[i][i] if i & mask else 0

        r = random.random()
        auxp = p
        proj = self.__projector(qubit, int(r < p))
        
        if r >= p:
            auxp = 1 - p
            
        self.dm = (proj @ self.dm @ proj)/auxp
        
        return int(r < p)
    
    def __projector(self, qubit, v):
        proj = np.zeros((2**self.nqubits, 2**self.nqubits), dtype=np.complex256)
        mask = 1 << qubit
        
        proj[qubit][qubit] = (qubit & mask) == v 
        
        return proj