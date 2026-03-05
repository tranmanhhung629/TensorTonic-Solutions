import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    M,N = A.shape #lay chieu dai, rong cua ma tran A
    #tao ma tran moi kich thuoc N,M
    result = np.zeros((N,M))
    for i in range(M):
        for j in range(N):
            result[j,i]=A[i,j]
    return result
    pass
