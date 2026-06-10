class Matrix:
    """
    A minimal matrix class using pure Python lists.
    All operations implemented from scratch — no NumPy.
    
    Functions:
        1. __getitem__()  - returns a item when fetched with its key
        2. multiply()     - returns the multiplication 2 matrices
        3. transpose()    - returns A^T, when input is A
        4. determinant()  - returns the determinant
        5. inverse()      - returns the inverse of a matrix
        6. is_symmetric() - returns true if A=A^T within tolerance
        7. trace()        - returns the trace of matrix A
    """

    def __init__(self, data):
        self.data = data
        self.row = len(data)
        self.cols = len(data[0]) if data else 0

    def __repr__(self):
        rows_str = ["  [" + "  ".join(f"{v:8.4f}" for v in row) + "]" for row in self.data]
        return "Matrix([\n" + "\n".join(rows_str) + "\n])"
    
    def __getitem__(self, key):
        return self.data[key]
    
    def multiply(self, other):
        """Matrix Multiplication: self @ other. O(n^3)."""
        if self.cols != other.rows:
            raise ValueError(f"Incompatible shapes: {self.rows}×{self.cols} × {other.rows}×{other.cols}")
        result = [[0.0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)
    
    def transpose(self):
        """Return A^T, swap rows and columns"""
        result = [[self.data[r][c] for r in range(self.rows)] for c in range(self.cols)]
        return Matrix(result)
    
    def determinant(self):
        """
        Compute the determinant using cofactor expansion (Laplace)
        O(n!) - fine for small matrices - can use LU in production
        """
        if self.rows != self.cols:
            raise ValueError("Determinant only defined for square matrices")
        n = self.rows
        if n == 1:
            return self.data[0][0]
        if n == 2:
            return self.data[0][0]*self.data[1][1] - self.data[0][1]*self.data[1][0]
        # Cofactor expansion along first row
        det = 0
        for j in range(n):
            minor = Matrix([[self.data[r][c] for c in range(n) if c != j] for r in range(1, n)])
            sign = (-1) ** j
            det += sign * self.data[0][j] * minor.determinant()
        return det
    
    def inverse(self):
        """
        Compute inverse using gauss jordan elimination.
        Augments [A | I] and row reduces to [I | A^-1]
        """
        if self.rows != self.cols:
            raise ValueError("Only square matrices have inverses")
        n = self.rows
        det = self.determinant()
        if abs(det) < 1e-12:
            raise ValueError(f"Matrix is singular (det={det}) — no inverse exists")

        # Augmented matrix [A | I]
        M = [self.data[i][:] + [1.0 if i == j else 0.0 for j in range(n)]
             for i in range(n)]

        # Forward elimination
        for col in range(n):
            # Pivot: find row with max value in this column
            pivot = max(range(col, n), key=lambda r: abs(M[r][col]))
            M[col], M[pivot] = M[pivot], M[col]
            # Scale pivot row so pivot element = 1
            scale = M[col][col]
            M[col] = [v / scale for v in M[col]]
            # Eliminate this column in all OTHER rows
            for row in range(n):
                if row != col:
                    factor = M[row][col]
                    M[row] = [M[row][j] - factor * M[col][j] for j in range(2*n)]

        # Extract right half — that's A⁻¹
        inv_data = [M[i][n:] for i in range(n)]
        return Matrix(inv_data)
    
    def is_symmetric(self, tol=1e-10):
        """Return True if A = A^T within tolerance."""
        if self.rows != self.cols:
            return False
        return all(
            abs(self.data[i][j] - self.data[j][i]) < tol
            for i in range(self.rows)
            for j in range(self.cols)
        )
    
    def trace(self):
        """ Sum of diagonal entries = Sum of eigenvalues """
        if self.rows != self.cols:
            raise ValueError("Trace only defined for square matrices")
        return sum(self.data[i][i] for i in range(self.rows))
    
# Full verification 
import numpy as np

A = Matrix([[2, 1, 0],
             [1, 3, 1],
             [0, 1, 4]])

print("Matrix A:")
print(A)

print(f"\nDeterminant: {A.determinant():.6f}")
print(f"NumPy det:   {np.linalg.det(np.array(A.data)):.6f}")

A_inv = A.inverse()
print("\nInverse:")
print(A_inv)

# Verify A · A^-1 = I
product = A.multiply(A_inv)
print("\nA x A^-1 (should be I):")
print(product)

print(f"\nSymmetric: {A.is_symmetric()}")   # True for this A
print(f"Trace: {A.trace()}")                # 2+3+4 = 9