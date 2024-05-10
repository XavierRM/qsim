import unittest
import numpy as np
from core.Gates import X, swap

class GatesTest(unittest.TestCase):
    def test_notGate(self):
        self.assertTrue(np.all(X() == np.array([[0, 1], [1, 0]])))
        
    def test_swapGate(self):
        swap([0, 1])
        
if __name__ == "__main__":
  unittest.main()
