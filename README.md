# Quantum State Simulator

This tool simulates the evolution of a quantum state over time using 
random unitary matrices. In quantum mechanics, a quantum state represents 
the probability distribution of possible measurement outcomes of a quantum 
system. The evolution of a quantum state is governed by the Schrödinger 
equation, which is a fundamental equation of quantum mechanics. In this 
simulation, the quantum state is represented as a vector of complex 
coefficients, and each element of the vector corresponds to the 
probability amplitude of a particular quantum state. By applying random 
unitary matrices to the quantum state, we can simulate the evolution of 
the system over time. This tool uses the Python programming language to 
simulate the evolution of a quantum state over time. The simulation 
algorithm is implemented using the NumPy library, which provides a 
powerful set of tools for working with multi-dimensional arrays and 
matrices. In addition, the Matplotlib library is used to generate 
visualizations of the quantum state over time, and the PIL library is 
used to convert these visualizations into GIF animations. Finally, the 
Flask web framework is used to create a web application that allows users 
to interactively input quantum states and view the resulting animations in 
real-time.

1. `git clone https://github.com/Nit682/quantumstatesim.git`
2. `pip install -r requirements.txt`
3. `python app.py`
