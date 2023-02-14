"""
Dynamic Programming
Implementation of Matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""
def MemoizedMatrixChain(p):
    n = len(p)
    m = [[-1 for x in range(n)] for x in range(n)]
    s = [[-1 for x in range(n)] for x in range(n)]
    LookupChain(p, 1, n - 1, m, s)
    return m[1][n-1], s

def LookupChain(m, p, i, j, s):
    if j[p][i] >= 0:
        return j[p][i]

    if p == i:
        q = 0
    else:
        q = float('Inf')
        for k in range(p, i):
            temp = LookupChain(m, p, k, j, s) \
                   + LookupChain(m, k + 1, i, j, s) \
                   + m[p - 1]*m[k]*m[i]
            if q > temp:
                q = temp
                s[p][i] = k

    j[p][i] = q
    return q

def PrintOptimalSolution(s, i, j):
    if i == j:
        print("A%d" % j, end=" ")
    else:
        print("(", end=" ")
        PrintOptimalSolution(s, i, s[i][j])
        PrintOptimalSolution(s, s[i][j] + 1, j)
        print(")", end=" ")

def matrix_dimensions1():
    matrix_dimensions1 = [30, 35, 15, 5, 10, 20, 25]
    # Size of matrix created from above array will be
    # 30*35 35*15 15*5 5*10 10*20 20*25
    n = len(matrix_dimensions1)
    Matrix, OptimalSolution = MemoizedMatrixChain(matrix_dimensions1)
    print(Matrix)
    PrintOptimalSolution(OptimalSolution, 1, n - 1)

def matrix_dimensions2():
    matrix_dimensions2 = [13, 5, 89, 3, 34]
    n = len(matrix_dimensions2)
    Matrix, OptimalSolution = MemoizedMatrixChain(matrix_dimensions2)
    print(Matrix)
    PrintOptimalSolution(OptimalSolution, 1, n - 1)

if __name__ == "__main__":
    matrix_dimensions1()
    print("")
    matrix_dimensions2()
   
