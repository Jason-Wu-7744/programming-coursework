# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

A = np.array([[3, -1, 1],
              [1, 3, 1],
              [1, 2, 7]])
b = np.array([[7],
              [-3],
              [11]])

def GaussSeidel_iteration(A, b, e, max_iter=10000):
    """Course iteration with an iterate-difference/residual stop and finite cap."""
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).reshape(-1, 1)
    n = len(b)
    if A.shape != (n, n) or not np.all(np.isfinite(A)) or not np.all(np.isfinite(b)):
        raise ValueError("A and b must be finite and have compatible dimensions")
    if e <= 0 or not np.isfinite(e) or max_iter < 1 or np.any(np.diag(A) == 0):
        raise ValueError("Require positive tolerance/iteration limit and nonzero diagonal")
    x = np.zeros((n, 1))
    for iteration in range(max_iter):
        old = x.copy()
        for i in range(n):
            total = sum(A[i, j] * x[j, 0] for j in range(n) if j != i)
            x[i, 0] = (b[i, 0] - total) / A[i, i]
        if not np.all(np.isfinite(x)):
            raise RuntimeError("Gauss-Seidel iteration diverged")
        print(x)  # Retain the assignment requirement to show each iteration.
        if np.linalg.norm(x - old, np.inf) <= e and np.linalg.norm(A @ x - b, np.inf) <= e:
            return x
    raise RuntimeError("Gauss-Seidel did not converge within max_iter")
print('根为：\n', GaussSeidel_iteration(A, b, 0.1))

# Iteration counts depend on the corrected convergence criterion and input.