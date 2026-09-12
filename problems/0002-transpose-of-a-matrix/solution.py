import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    m = len(a[0])
    n = len(a)
    sol = []
    # for i in a:
    #     temp = []
    #     for j in range(n):
    #         temp.append(i[j])
    #     sol.append(temp)
    return np.transpose(a)
        