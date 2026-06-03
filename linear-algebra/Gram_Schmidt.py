# Code to implement Gram Schmidt Orthogonalization

import numpy as np

def gram_schmidt(A):
    """
    Gram-Schmidt orthonormalisation.
    A: n x k matrix whose columns are the input vectors.
    Returns Q: n x k matrix with orthonormal columns,
            R: k x k upper triangular matrix such that A = QR.
    """
    n, k = A.shape()
    Q = np.zeros_like(A, dtype=float) # creates a new array or tensor filled with zeros

    for j in range(k):
        v = A[: , j].astype(float).copy()
        # Subtracts projections onto all previous orthonormal vectors
        for i in range(j):
            v -= np.dot(Q[:, i], A[:, j]) * Q[:, i]
        # Normalise
        norm = np.linalg.norm(v)
        if norm < 1e-10:
            raise ValueError("Columns are linearly dependent")
        Q[:, j] = v/norm
    
    R = Q.T @ A     # R = QTA
    return Q, R

# Testing
A = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=float)

Q, R = gram_schmidt(A)

# Verifying that Q has orthonormal columns : Qt @ Q should be Identity I
print(np.round(Q.T @ Q, 10)) # Should be identity

# Verifying A = QR
print(np.round(Q@R - A, 10)) # Should be all zeros

# Compare with NumPy's QR
Q_np, R_np = np.linalg.qr(A)
# Columns may differ in sign but the span remains the same space