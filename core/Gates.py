import numpy as np

def X():
    return np.array([[0, 1], [1, 0]])

def H():
    return np.array([[1/2**0.5, 1/2**0.5], [1/2**0.5, -1/2**0.5]])

def Z():
    return np.array([[1, 0], [0, -1]])

def Y():
    return np.array([[0, -1j], [1j, 0]])

def CX():
    return np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])

def swap(applyTo):
    if(len(applyTo) == 1):
        return np.eye(2)
    
    numQ = applyTo[1] - applyTo[0] + 1
    swapM = np.eye(2**numQ)
    
    if applyTo[1] == applyTo[0]:
        return swapM
    
    if(len(applyTo) != 2):
        raise ValueError("Swap operation can only be made to two qubits")
    
    if applyTo[1] < applyTo[0]:
        raise ValueError("Wrong input order: qubitIndex[1] < qubitIndex[0]")
    
    mask1 = 1 << applyTo[0]
    mask2 = 1 << applyTo[1]

    for i in range(2**numQ):
        if (i & mask1) and not (i & mask2):
            swapM[i, i] = 0
            swapM[i-mask1+mask2, i-mask1+mask2] = 0
            swapM[i, i-mask1+mask2] = 1
            swapM[i-mask1+mask2, i] = 1
    
    return swapM
            
    
     