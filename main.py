import numpy as np

if __name__ == '__main__':
    A = np.array([[10, 0], [1, 1]])
    b = np.array([1, 1])
    x = np.dot(np.linalg.inv(A), b)

    x = np.array([0.0, 0.0])
    w = 1.05
    n = len(x)
    for iteration in range(1000):
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s = s + A[i][j] * x[j]
            # x[i] = (1-w)*x[i] + w/A[i][i]*(b[i] - s)
            x[i] = x[i] + w * ((b[i] - s) / A[i][i] - x[i])

    print("SOR: x=", x)

