import numpy as np

def batch_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
    m = np.mean(X,axis=(0,2,3),keepdims=True)
    s = np.std(X,axis=(0,2,3),keepdims=True)
    norm_x = (X - m)/(s + epsilon)
    return (gamma * norm_x) + beta