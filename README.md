# Quantum Simulator

In order to try the different aspects of both statevector based and density matrix based simulators there's a main.py file to play with them

## Imports

All components are divided in files and to import them we can do so like:

```python
from QuantumRegister import QuantumRegister
from DMQuantumRegister import QuantumRegister
from Gates import H, X
from Block import BlochSphere
```

## Quantum Register (Statevector based)

In order to use this QuantumRegister import it like specified in [Imports](#imports) (QuantumRegister module), once imported we can use certain auxiliar methods to get some information about the state being hold by our *QuantumRegister*, like done in the follwing example:

```python
from QuantumRegister import QuantumRegister

qr = QuantumRegister(2)

qr.nqubits # Number of qubits used by the register

qr.ket() # Ket form of our StateVector
qr.bra() # Bra form of our StateVector

qr.densityMatrix() # Density Matrix representing our quantum register
```

### Applying gates to our register

We can use either single qubit or double qubit gates, for this purpouse a distinction has been set for both methods, for exmaple:

```python
from QuantumRegister import QuantumRegister
from Gates import X

qr = QuantumRegister(1)

qr.applyGate(X(), 0)
```

```python
from QuantumRegister import QuantumRegister
from Gates import CX

qr = QuantumRegister(2)

qr = qr.applyMQGate(CX(), [0, 1])
```
<span style="color: red;">NOTE: </span> The application of the multiqubit gates hasn't been tested much for this QuantumRegister version there's something I'm going over and can't seem to solve.

### Measurement
The application of the measurement will invalidate our state and won't be reusable after

```python
from QuantumRegister import QuantumRegister
from Gates import H

qr = QuantumRegister(1)

qr.applyGate(H(), 0)
qr.measure(0)
```
## Quantum Register (Density Matrix based)

In order to use this QuantumRegister import it like specified in [Imports](#imports) (DMQuantumRegister module), once imported we can use certain auxiliar methods to get some information about the state being hold by our *QuantumRegister*, like done in the follwing example:

```python
from QuantumRegister import QuantumRegister

qr = QuantumRegister(2)

qr.nqubits # Number of qubits used by the register

qr.matrix() # Density Matrix representing our quantum register
```

### Applying gates to our register

We can use either single qubit or double qubit gates, for this purpouse a distinction has been set for both methods, for exmaple:

```python
from DMQuantumRegister import QuantumRegister
from Gates import X

qr = QuantumRegister(2)

qr.applyGate(X(), 0)
```

```python
from DMQuantumRegister import QuantumRegister
from Gates import CX

qr = QuantumRegister(2)

# Preparing Bell state
qr = qr.applyGate(X(), 0)
qr = qr.applyNQGate(CX(), [0, 1])
```

### Measurement
The application of the measurement will invalidate our state and won't be reusable after

```python
from QuantumRegister import QuantumRegister
from Gates import H

qr = QuantumRegister(1)

qr.applyGate(H(), 0)
qr.measure(0)
```

## Gates

I've added the matrices of some of the most common gates, to use them import them like stated in [Imports](#imports), the following gates have been implemented:

```python
from Gates import H, X, Z, Y, CX, swap

# They're functions that will return the built matrix of the operation requested
X()
H()
Z()
Y()
CX()

# The swap operation receives a list of indices with a required len of 2
# arg[0] has to be < arg[1]
swap([0, 1])

```

## Bloch Sphere

For now it does not draw the actual sphere, but the call to *draw* will print out the coordinates to do so, it only supports the QuantumRegister from the QuantumRegister module (Statevector based).

```python
from QuantumRegister import QuantumRegister
from Gates import H
from Bloch import BlochSphere

qr = QuantumRegister(1)

qr = qr.applyGate(H(), 0)

BlochSphere(qr).draw()
```

## Utility functions

There's some utility functions to calculate the **Entropy** and **PartialTrace** of a density matrix:

```python
from DMQuantumRegister import QuantumRegister
from util import entropy, partialTrace

qr = QuantumRegister(2)

entropy(qr.matrix())
partialTrace(qr.matrix())
```
## <span style="color: darkred;">Tests</span>

Tests haven't been updated since an early version so they might not work, reference the points above for examples on how to use every component provided
