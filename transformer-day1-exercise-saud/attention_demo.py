import numpy as np
from typing import Tuple


def softmax(scores: np.ndarray) -> np.ndarray:
    shifted = scores - np.max(scores, axis=-1, keepdims=True)
    exp_scores = np.exp(shifted)
    return exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)


def scaled_dot_product_attention(
    Q: np.ndarray,
    K: np.ndarray,
    V: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:

    d_k = Q.shape[-1]

    scores = np.matmul(Q, K.T) / np.sqrt(d_k)

    attention_weights = softmax(scores)

    output = np.matmul(attention_weights, V)

    return output, attention_weights


if __name__ == "__main__":

    np.random.seed(42)

    seq_len = 5
    d_k = 8
    d_v = 8

    Q = np.random.randn(seq_len, d_k)
    K = np.random.randn(seq_len, d_k)
    V = np.random.randn(seq_len, d_v)

    output, attention = scaled_dot_product_attention(Q, K, V)

    print("Attention Weights:")
    print(np.round(attention, 3))

    print("\nOutput:")
    print(np.round(output, 3))