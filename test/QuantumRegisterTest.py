from core.QuantumRegister import QuantumRegister
from core.Gates import CX

import unittest
import numpy as np
from scipy.linalg import logm

class QuantumRegisterTest(unittest.TestCase):
    size = 2
    zeroBra = np.array([[1] + [0 for _ in range((2**size)-1)]], dtype=complex)
    zeroKet = np.conjugate(np.transpose(zeroBra))
    
    '''
    def test_quantumRegisterKet(self):
        qr = QuantumRegister(self.size)
        
        self.assertEqual(qr.ket().size, 2**self.size)
        self.assertTrue(np.all(qr.ket() == self.zeroKet))
    
    def test_quantumRegisterBra(self):
        qr = QuantumRegister(self.size)
        
        self.assertEqual(qr.bra().size, 2**self.size)
        self.assertTrue(np.all(qr.bra() == self.zeroBra))
        
    def test_quantumRegisterDensityMatrix(self):
        qr = QuantumRegister(self.size)
        
        self.assertEqual(qr.densityMatrix().size**(1/2), 2**self.size)
        self.assertTrue(np.all(qr.densityMatrix() == np.dot(self.zeroKet, self.zeroBra)))
    '''

    def test_quantumRegisterParallelMeasure(self):
        qr = QuantumRegister(self.size)
        
        qr.parallelMeasure(0)


    '''        
    def test_applyNotGate(self):
        resultStateVector = np.array([[0], [1]])
        
        qr = QuantumRegister(self.size)
        self.assertTrue(np.all(qr.applyGate(X(), 0) == resultStateVector))
    '''

    '''
    def test_combineQRegisters(self):
        size = 1
        resultStateVector = np.array([[0], [0], [1], [0]])
        
        qr1 = QuantumRegister(size)
        qr2 = QuantumRegister(size)
        
        self.assertTrue(np.all(QuantumRegister.combine(qr1, qr2).ket() == resultStateVector))
    
    def test_applyMQGate(self):
        qr = QuantumRegister(3)
        
        qr.applyMQGate(CX(), [1, 2])
    '''
    
if __name__ == "__main__":
  unittest.main()
