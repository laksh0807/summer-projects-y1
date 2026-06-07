import numpy as np
import matplotlib.pyplot as plt

class PCA:
    """
    PCA - Principal Component Analysis, implemented from scratch.
    No sklearn, uses numpy eigrndecomposition only.
    We later verify using sklearn!
    """
    def __init__(self, n_components):
        self.n_components = n_components
        self.components_ = None                 # Principal Component Directions
        self.explained_variance_ = None         # Eigenvalues (variance per component)
        self.mean_ = None                       # Feature Means

    def fit(self, X):

        # Step 1 : Centre the data -
        self.mean_ = np.mean(X, axis=0)
        X_c = X - self.mean_

        # Step 2 : Covariance Matrix - 
        n = X_c.shape[0]
        C = (X_c.T @ X_c)/n

        # Step 3 : Eigendecomposition of C - 
        eigenvalues , eigenvectors = np.linalg.eigh(C)
        # eigh - is for symmetric matrices - returns real eigenvalues sorted ascending

        # Step 4 : Sort descending - 
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        # Keep only the top n components - 
        self.components_ = eigenvectors[:, :self.n_components]
        self.explained_variance_ = eigenvalues[:self.n_components]

        # Variance explained ratio
        total_var = np.sum(eigenvalues)
        self.explained_variance_ratio_ = self.explained_variance_ / total_var
        return self
    
    def transform(self, X):
        # Step 5 : Project onto principal components - 
        X_c = X - self.mean_
        return X_c @ self.components_
    
    def fit_transform(self, X):
        return self.fit(X).transform(X)
    
# Testing on 2D diagonal dataset 
np.random.seed(0)
n = 200

# Points along the diagonal y ≈ x, with noise
t = np.random.normal(0, 3, n)
X = np.column_stack([
    t + np.random.normal(0, 0.3, n),
    t + np.random.normal(0, 0.3, n)
])

pca = PCA(n_components=2)
pca.fit(X)

print("Principal components (columns):")
print(np.round(pca.components_, 4))
# First PC should be ~[0.707, 0.707] — the diagonal direction

print(f"\nVariance explained: {pca.explained_variance_ratio_}")
# First component should explain ~98%+ of variance

# Plot
X_proj = pca.transform(X)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(X[:, 0], X[:, 1], alpha=0.5, s=15, color='#5b9cf6')
origin = pca.mean_
for i, (vec, var) in enumerate(zip(pca.components_.T, pca.explained_variance_)):
    scale = var**0.5 * 2
    axes[0].annotate("", xy=origin + vec * scale, xytext=origin,
                arrowprops=dict(arrowstyle="->", color='#e89c55', lw=2.5))
    axes[0].text(*(origin + vec*scale*1.1), f'PC{i+1}', color='#e89c55', fontsize=10)

axes[0].set_title('Original data + principal components')
axes[0].set_aspect('equal')

axes[1].scatter(X_proj[:, 0], X_proj[:, 1], alpha=0.5, s=15, color='#3ecf8e')
axes[1].set_title('Data in PCA coordinates (PC1 vs PC2)')
axes[1].set_xlabel('PC1 (main variance)')
axes[1].set_ylabel('PC2 (noise)')
axes[1].set_aspect('equal')

plt.tight_layout()
plt.savefig('pca_result.png', dpi=150, bbox_inches='tight')
plt.show()

# Verify against sklearn
from sklearn.decomposition import PCA as SklearnPCA
pca_sk = SklearnPCA(n_components=2).fit(X)
print("\nSklearn components:")
print(np.round(pca_sk.components_.T, 4))   # may differ in sign, not direction