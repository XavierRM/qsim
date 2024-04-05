import unittest
import numpy as np
from qsim.QuantumRegister import QuantumRegister

class QuantumRegisterTest(unittest.TestCase):
    size = 2
    zeroKet = np.conjugate(np.transpose(np.zeros(size)))
    zeroBra = np.zeros(size)
  
    def test_quantumRegisterKet(self):
        qr = QuantumRegister(self.size)
        
        self.assertEqual(qr.ket().size, self.size)
        self.assertTrue(np.all(qr.ket() == np.zeros((self.size, 1))))
    
    def test_quantumRegisterBra(self):
        qr = QuantumRegister(self.size)
        
        self.assertEqual(qr.bra().size, self.size)
        self.assertTrue(np.all(qr.bra() == np.zeros(self.size)))
        
    def test_quantumRegisterDensityMatrix(self):
        qr = QuantumRegister(self.size)
        
        self.assertEqual(qr.densityMatrix().size, 2**self.size)
        self.assertTrue(np.all(qr.densityMatrix() == np.dot(self.zeroKet, self.zeroBra)))

if __name__ == "__main__":
  unittest.main()