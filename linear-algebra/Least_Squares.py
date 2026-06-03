import numpy as np
import matplotlib.pyplot as plt

def least_squares_normal_eqn(A, b):
    """
    Solve least squares problem minimise ||Ax-b||^2 via the normal equation
    Returns xhat = (AtA)^-1 Atb
    """
    At = A.T        # For transposing matrix, can also use np.transpose(A)
    Ata = At @ A    # '@' symbol means matrix multiplication in NumPy (Source is NumPy Documentation!)
    Atb = At @ b
    x_hat = np.linalg.solve(Ata, Atb)
    return x_hat

def linear_regression(x_data, y_data):
    """
    Fit y = b0 + b1x using least squares.
    Returns (b0, b1)
    """
    n = len(x_data)
    # Now design matrix : columns of ones + columns of x values
    A = np.column_stack([np.ones(n), x_data])
    # np.column_stack() is used to combine 1-D or 2-D arrays as columns into a single 2-D array.
    # How it Works1-D Arrays: Converts them into 2-D column vectors and stacks them side-by-side.
    # 2-D Arrays: Stacks them as-is, similar to np.hstack().
    # All arrays must have the same length (same number of rows). 
    # np.ones(n) is used to make a new array of specified shape, size, dtype. here makes 1d array [1, 1, ...till n 1]
    beta = least_squares_normal_eqn(A, y_data)
    return beta

# We demonstarate by generating noisy data along y = 2x + 3
np.random.seed(42)
x = np.random.uniform(0, 10, 100)
y = 2 * x + 3 + np.random.normal(0, 1.5, 100)
# np.random.seed(n) - initiates a psuedo random number generator state using a fixed seed (42)
# np.random.uniform(low, high, size) - Samples 100 values from a flat, uniform probability distribution over the interval [0, 10).
# y = 2 * x + 3 + np.random.normal(0, 1.5, 100) - Establishes a true slope of m=2 and intercept of b=3.
# Introduces random statistical noise via np.random.normal(0, 1.5, 100).
# This noise follows a normal (Gaussian) bell curve centered at a mean of 0 with a standard deviation of 1.5.

beta = linear_regression(x, y)
print(f"β₀ = {beta[0]:.4f}  (true: 3)")
print(f"β₁ = {beta[1]:.4f}  (true: 2)")

# Verify against numpy.linalg.lstsq - a NumPy function used to compute the least-squares solution to a linear matrix equation
A = np.column_stack([np.ones(100), x])
beta_np, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
print(f"NumPy lstsq: β₀ = {beta_np[0]:.4f}, β₁ = {beta_np[1]:.4f}")
# Both should match to many decimal places

# Plot
x_line = np.linspace(0, 10, 200)
y_fit = beta[0] + beta[1] * x_line
y_true = 3 + 2 * x_line

# https://matplotlib.org/stable/ - Matplotlib Documentation used here !
plt.figure(figsize=(9, 5)) # Generate a new container window for your plot
plt.scatter(x, y, s=20, alpha=0.5, color='#5b9cf6', label='Data (noisy)') # Generates a scatter plot by plotting individual data points X, Y
plt.plot(x_line, y_fit,  color='#3ecf8e', lw=2, label=f'Fit: y={beta[0]:.2f}+{beta[1]:.2f}x') # Generates std cont line charts 
plt.plot(x_line, y_true, color='#e89c55', lw=1.5, ls='--', label='True: y=3+2x')
plt.legend() # Places a visual key on your chart to decipher labels tied to different lines or data substances
plt.title('Least Squares Fit via Normal Equation') # Adds a descriptive header above the plot         
plt.savefig('least_squares.png', dpi=150, bbox_inches='tight') # Exports the completed diagram into a local file format (e.g., .png, .pdf, .svg)
plt.show() # Opens an active graphical user interface (GUI) window to display the layout directly on your monitor.