import numpy as np
import scipy as sp
import matplotlib as mp
import sympy 

from scipy import linalg
from scipy import signal
from sympy import Matrix

def main():
    print("Hello from hw1!")
    A_sym = Matrix([[1,3,5,25],[0,2,4,18],[2,4,6,32]]) 
    A_sym_rref = A_sym.rref()
    print(f"A in row reduced echelon form is: {A_sym_rref}")
    # This is for problem 3
    A = np.array([[-2, -0.02], [1, -10]])
    B = np.array([[5],[0]])
    C = np.array([[0,1]])
    D = 0
    # can use this to create an LTI for state space
    system = signal.StateSpace(A,B, C, D)

if __name__ == "__main__":
    main()
