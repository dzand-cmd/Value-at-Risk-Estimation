import numpy as np
from scipy.stats import norm 

def historical_var(returns, confidence=0.95):
    """
    returns: array-like of returns
    confidence: e.g. 0.95 for 95% VaR
    """
    returns = np.sort(returns)
    index = int((1 - confidence) * len(returns))
    return -returns[index]

def parametric_var(returns, confidence=0.95):
    mu = np.mean(returns)
    sigma = np.std(returns)
    
    z = norm.ppf(1 - confidence)  # negative value
    
    var = mu + z * sigma
    return -var

def monte_carlo_var(S0, mu, sigma, T=1, simulations=10000, confidence=0.95):
    """
    S0: initial price
    mu: expected return
    sigma: volatility
    T: time horizon (in years)
    """
    Z = np.random.standard_normal(simulations)
    
    # Geometric Brownian Motion
    ST = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    # returns
    returns = (ST - S0) / S0
    
    returns = np.sort(returns)
    index = int((1 - confidence) * simulations)
    
    return -returns[index]

# Fake return data (replace with real data later)
np.random.seed(42)
returns = np.random.normal(0.001, 0.02, 1000)

# Historical VaR
h_var = historical_var(returns)

# Parametric VaR
p_var = parametric_var(returns)

# Monte Carlo VaR
mc_var = monte_carlo_var(S0=100, mu=0.001, sigma=0.02)

print("Historical VaR:", h_var)
print("Parametric VaR:", p_var)
print("Monte Carlo VaR:", mc_var)