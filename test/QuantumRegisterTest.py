import unittest
import numpy as np
from core.QuantumRegister import QuantumRegister

class QuantumRegisterTest(unittest.TestCase):
    size = 2
    zeroBra = np.array([[1] + [0 for _ in range((2**size)-1)]], dtype=complex)
    zeroKet = np.conjugate(np.transpose(zeroBra))
  
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

if __name__ == "__main__":
  unittest.main()
