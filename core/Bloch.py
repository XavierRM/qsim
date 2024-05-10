import numpy as np

class BlochSphere:
    def __init__(self, qreg):
        self.qreg = qreg
    
    def _getCoords(self):
        arg = np.angle(self.qreg.can())
        normState = np.exp(-arg*1j)*np.array([self.qreg.state[0], self.qreg.state[1]], dtype=np.complex256)
        
        theta = 2*np.arccos(normState[0, 0].real)
        phi = np.angle(normState[1, 0])
        
        return [theta, phi]
    
    def draw(self):
        return self._getCoords()

  
  