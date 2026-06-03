import numpy as np
# https://numpy.org/doc/stable/reference/routines.linalg.html
# Rely on the above source for the documentation of NumPy linalg submodule

def gaussian_elimination(A, b):
    """
    Solve Ax = b using gaussian elimination with partial pivoting
    Returns solution vector x
    A : n x n matrix (list of list or a numpy array)
    b : n length vector
    """
    n = len(b)

    # Now we build the augmented matrix [A|b]
    M = np.array([row + [b[i]]for i, row in enumerate(A)], dtype=float)

    # Forward elimination
    for col in range(n):
        # Partial pivoting: swap current row with the row below
        # that has the largest absolute value in this column.
        # This improves numerical stability.
        max_row = np.argmax(np.abs(M[col:, col])) + col
        M[[col, max_row]] = M[[max_row, col]]

        pivot = M[col, col]
        if abs(pivot) < 1e-12:
            raise ValueError("Matrix is singular — system has no unique solution")

        # Eliminate entries below the pivot in this column
        for row in range(col + 1, n):
            factor = M[row, col] / pivot
            M[row, col:] -= factor * M[col, col:]

    # Back substitution: solve from bottom row upwards
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:])) / M[i, i]

    return x

# Test it
A = [[2, 4, -2],
     [4, 9, -3],
     [-2, -3, 7]]
b = [2, 8, 10]

x = gaussian_elimination(A, b)
print(f"Solution: {x}")              # [1. 2. 2.]
print("Numpy Results:")
# Verify: should be [2, 8, 10]
print(np.dot(np.array(A), x))        # [2. 8. 10.] (b value)
# Compare against numpy's solver
print(np.linalg.solve(np.array(A), np.array(b)))  # same answer (returns x value)