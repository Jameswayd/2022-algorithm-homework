"""
Dynamic Programming
Implementation of Matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""
def MatrixChainOrder(p):
    n = len(p)
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    for Length in range(2, n):
        for i in range(1, n - Length + 1):
            j = i + Length - 1

            m[i][j] = float('Inf')
            for k in range(i, j):
                cost = (
                    m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                )
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return m[1][n-1], s

# Print order of matrix with Ai as Matrix
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
    Matrix, OptimalSolution = MatrixChainOrder(matrix_dimensions1)
    print(Matrix)
    PrintOptimalSolution(OptimalSolution, 1, n - 1)

def matrix_dimensions2():
    matrix_dimensions2 = [13, 5, 89, 3, 34]
    n = len(matrix_dimensions2)
    Matrix, OptimalSolution = MatrixChainOrder(matrix_dimensions2)
    print(Matrix)
    PrintOptimalSolution(OptimalSolution, 1, n - 1)



if __name__ == "__main__":
    matrix_dimensions1()
    print("")
    matrix_dimensions2()
   


