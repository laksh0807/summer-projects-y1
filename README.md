# Quantitative Finance & Engineering: Summer Roadmap
A rigorous, deep dive into core software architecture, foundational mathematics, derivative pricing models, and portfolio optimization before starting Year 2.

---

## Roadmap & Progress Tracker

### Phase 1: Core Python & Architecture
- [x] Environment configuration & baseline tooling (`venv`, `pip`, VS Code)
- [x] Object-Oriented Programming (OOP) deep-dive & custom packages
- [x] Production-grade Bank Account Simulator with strict data validation
- [x] Custom low-level data structures (Stack & Queue implemented from scratch)

### Phase 2: Numerical Linear Algebra from Scratch
- [x] Matrix operations, vector spaces, and elimination mechanics
- [x] Custom QR Decomposition implementation
- [x] Custom Least Squares Approximation solver
- [x] Matrix Rank Computing algorithm
- [x] Eigenvalues & Eigenvectors engine
- [x] Singular Value Decomposition (SVD) & Principal Component Analysis (PCA)

### Phase 3: Advanced Data Structures & Algorithms *(In Progress)*
- [x] Algorithmic Big-O time and space complexity modeling
- [x] Memory-managed Pointer Structures: Singly & Doubly Linked Lists
- [ ] Empirical benchmarking of classic Sorting Engines (Merge, Quick, Insertion, Bubble)
- [ ] Non-linear Topologies: Binary Search Trees (BST), Heaps, and Tries
- [ ] Graph Architectures: Adjacency structures, BFS/DFS, and Dijkstra’s Shortest Path
- [ ] Dynamic Programming: Tabulation vs. Memoization paradigms

### Phase 4: Mathematical Probability & Quant Teasers
- [ ] Axiomatic probability, Bayes' Theorem, and combinatorial mechanics
- [ ] Analytical derivation of discrete/continuous distributions (Binomial, Poisson, Normal, Exponential)
- [ ] Statistical limit theorems: Law of Large Numbers (LLN) & Central Limit Theorem (CLT)
- [ ] Maximum Likelihood Estimation (MLE) & Bayesian updating regimes
- [ ] Stochastic Modeling: Foundational Markov Chains
- [ ] High-pressure Quant brain teasers (Zhou / Green Book interview sets)

### Phase 5: LeetCode Algorithmic Sprint
- [ ] Algorithmic Patterns: Sliding Windows, Two Pointers, Hashing
- [ ] Advanced Graph structures & multi-dimensional Grid traversals
- [ ] 1D and 2D Dynamic Programming optimizations
- [ ] Targets: 50+ medium/hard interview problems systematically categorized

### Phase 6: Financial Data Science & Tooling
- [ ] **NumPy**: Vectorization, broadcasting mechanics, and optimized linear algebra arrays
- [ ] **Pandas**: Time-series manipulation, rolling statistics, and financial tracking logic
- [ ] **SQL**: Advanced relational data architecture, window functions, and indexing optimization
- [ ] **Applied Stats**: Ordinary Least Squares (OLS) regressions, hypothesis testing, and CAPM Beta extraction
- [ ] **APIs & Automation**: Live financial market streaming via `yfinance` & custom wrapper engines

### Phase 7: Financial Engineering & Stochastic Calculus
- [ ] Geometric Brownian Motion (GBM) simulation engines & Monte Carlo pathway rendering
- [ ] Modern Portfolio Theory (MPT): Mean-Variance optimization & Efficient Frontier mapping
- [ ] Derivative Pricing: Analytical **Black-Scholes-Merton Option Pricing Model**
- [ ] Risk Engines: Exact partial differential computation of the **5 Options Greeks** (Delta, Gamma, Vega, Theta, Rho)

### Phase 8: Production Portfolio Pieces
- [ ] **Project 1**: Automated Portfolio Optimizer Package with continuous Monte Carlo risk pathways
- [ ] **Project 2**: Production-grade Black-Scholes Options Pricer with an automated Implied Volatility Surface generator

---

## Infrastructure & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/laksh0807/summer-projects-y1
   cd summer-projects-y1
   ```

2. **Initialize a secure Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv\Scripts\activate  
   ```

3. **Install the complete environment stack:**
   ```bash
   pip install -r requirements.txt
   ```

## Comprehensive Tech Stack
* **Language:** Python 3.14.5
* **Core Computational Stack:** NumPy, SciPy, Pandas, Statsmodels
* **Visualization Engines:** Matplotlib, Seaborn
* **Data Ingestion:** yfinance, Relational SQL Engines
