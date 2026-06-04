import numpy as np

def eigenvalues_2x2(A):
    """
    We compute eigenvalues of 2 x 2 matrix analytically.
    Uses:  λ² - trace·λ + det = 0
    """
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    tr = a + d
    det = a*d - b*c
    discriminant = tr**2 - 4 * det
    if discriminant < 0:
        return None   # complex eigenvalues
    lam1 = (tr + discriminant**0.5) / 2
    lam2 = (tr - discriminant**0.5) / 2
    return lam1, lam2

def matrix_power_via_diagonalisation(A, k):
    """
    Compute Aᵏ using diagonalisation: A = SΛS⁻¹ → Aᵏ = SΛᵏS⁻¹
    """
    eigenvalues, S = np.linalg.eig(A)      # Eig calculates and returns eigenvalues and right eigenvectors of A - which is the matrix S
    Lambda_k = np.diag(eigenvalues**k)
    S_inv = np.linalg.inv(S)
    return S @ Lambda_k @ S_inv


# Test
A = np.array([[3, 1],
              [1, 3]], dtype=float)

# Our analytic formula
lam1, lam2 = eigenvalues_2x2(A.tolist())
print(f"Eigenvalues (analytic): λ₁={lam1}, λ₂={lam2}")   # 4.0, 2.0

# NumPy verification
vals, vecs = np.linalg.eig(A)
print(f"Eigenvalues (NumPy):    {vals}")   # [4., 2.]

# Aᵏ via diagonalisation vs repeated multiplication
k = 10
A_k_diag  = matrix_power_via_diagonalisation(A, k)
A_k_brute = np.linalg.matrix_power(A, k)

print(f"\nA¹⁰ via diagonalisation:\n{np.round(A_k_diag, 4)}")
print(f"\nA¹⁰ via repeated multiply:\n{A_k_brute}")
print(f"\nDifference: {np.round(np.abs(A_k_diag - A_k_brute).max(), 10)}")
# Should be essentially zero (floating-point rounding only)