import numpy as np
# https://numpy.org/doc/stable/reference/routines.linalg.html
# Rely on the above source for the documentation of NumPy linalg submodule

def compute_rank(A, tol=1e-10):
    """
    Compute the rank of matrix A by row reduction.
    Counts the number of non-zero pivots after Gaussian elimination.
    """
    M = np.array(A, dtype=float)
    rows, cols = M.shape
    pivot_row = 0
    rank = 0

    for col in range(cols):
        if pivot_row >= rows:
            break

        # Find pivot in this column at or below pivot_row
        pivot = np.argmax(np.abs(M[pivot_row:, col])) + pivot_row

        if np.abs(M[pivot, col]) < tol:
            continue    # no pivot in this column — it's a free variable column

        # Swap current pivot_row with the best pivot row
        M[[pivot_row, pivot]] = M[[pivot, pivot_row]]

        # Eliminate entries below the pivot
        for row in range(pivot_row + 1, rows):
            if np.abs(M[pivot_row, col]) > tol:
                factor = M[row, col] / M[pivot_row, col]
                M[row, col:] -= factor * M[pivot_row, col:]

        pivot_row += 1
        rank += 1

    return rank


# Test cases
A1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]    # rank-deficient: row3 = row1 + row2 roughly

A2 = [[1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]]   # identity — full rank 3

A3 = [[1, 2],
      [2, 4],
      [3, 6]]    # all rows are multiples of first row — rank 1

for A in [A1, A2, A3]:
    r = compute_rank(A)
    np_r = np.linalg.matrix_rank(np.array(A))
    print(f"Our rank: {r}, NumPy rank: {np_r}")   # must match