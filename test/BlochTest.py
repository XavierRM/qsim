import unittest
import numpy as np
from core.Gates import X, H, Z, Y
from core.Bloch import BlochSphere
from core.QuantumRegister import QuantumRegister

class BlochTest(unittest.TestCase):
    def test_BaseVector(self):
        qreg = QuantumRegister(1)
        print("Base: ", BlochSphere(qreg).draw())
        #self.assertTrue(np.all([0, 1] == BlochSphere(qreg).draw()))
        
    def test_NotVector(self):
        qreg = QuantumRegister(1)
        qreg.applyGate(X(), 0)
        print("X: ", BlochSphere(qreg).draw())
        #self.assertTrue(np.all([0, 1] == BlochSphere(qreg).draw()))
    
    def test_HadamardVector(self):
        qreg = QuantumRegister(1)
        qreg.applyGate(H(), 0)
        print("H: ", BlochSphere(qreg).draw())
        #self.assertTrue(np.all([1.5707, 0j] == BlochSphere(qreg).draw()))
    
    def test_LocalPhaseVector(self):
        qreg = QuantumRegister(1)
        qreg.applyGate(Z(), 0)
        print("Z: ", BlochSphere(qreg).draw())
        #self.assertTrue(np.all([0, 1] == BlochSphere(qreg).draw()))
        
    def test_YGateVector(self):
        qreg = QuantumRegister(1)
        qreg.applyGate(Y(), 0)
        print("Y: ", BlochSphere(qreg).draw())
        #self.assertTrue(np.all([0, 1] == BlochSphere(qreg).draw()))
    
    
if __name__ == "__main__":
  unittest.main()
