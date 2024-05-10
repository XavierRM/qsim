from core.QuantumRegister import QuantumRegister
from core.Gates import X, H
from core.util import entropy, partialTrace

import unittest
import numpy as np
from scipy.linalg import logm

class UtilTest(unittest.TestCase):
    def test_calcEntropy(self):
        qr = QuantumRegister(1)

        self.assertTrue(entropy(qr.densityMatrix()) == -0)
        
    def test_calcEntropyWithH(self):
        qr = QuantumRegister(1)
        
        qr.applyGate(H(), 0)
                
        self.assertTrue(entropy(qr.densityMatrix()) == -0)
        
    def test_calcEntropyWithMixedState(self):
        qr1 = QuantumRegister(1)
        qr2 = QuantumRegister(1).applyGate(X(), 0)
        
        densityMatrix1 = 0.99 * qr1.densityMatrix()
        densityMatrix2 = 0.01 * qr2.densityMatrix()
        
        mixedDM = densityMatrix1 + densityMatrix2
        
        self.assertTrue(entropy(mixedDM) > 0)
        
    def test_calcPartialTrace(self):
        qr = QuantumRegister(4)

        print(partialTrace(qr.densityMatrix()))

        self.assertTrue(partialTrace(qr.densityMatrix()) == 1)
        

if __name__ == "__main__":
  unittest.main()
