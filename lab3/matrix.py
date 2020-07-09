def transpose(matrix):
    if matrix != []:
        cols = len(matrix[0])
        rows = len(matrix)
        newMat = [[0 for x in range(rows)] for y in range(cols)]

        for i in range(0, rows):
            for j in range(0, cols):
                newMat[j][i] = matrix[i][j]

        return newMat
    return []



def powers(list, num1, num2):
    if list != []:
        rows = len(list)
        cols = num2 + 1
        mat = [[0 for x in range(cols)] for y in range(rows)]

        for i in range(0, rows):
            for j in range(num1, cols):
                mat[i][j] = pow(list[i], j)

        return mat
    return []



def matmul(mat1, mat2):
    if mat1 != [] and mat2 != []:

        # Setup dimensions of result matrix
        newMatRows = len(mat1)
        newMatCols = len(mat2[0])
        newMat = [[0 for x in range(newMatCols)] for y in range(newMatRows)]

        #print(newMatRows)
        #print(newMatCols)

        # Row of mat 1
        for i in range(len(mat1)):
            # Col of mat 2
            for j in range(len(mat2[0])):
                res = 0
                # Row of mat 2
                for k in range(len(mat2)):
                    res = mat1[i][k] * mat2[k][j]
                    newMat[i][j] += res

        return newMat
    return []



# Assuming we are dealing with 2x2 matrices
def det(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    return a * d - b * c

def invert(matrix):
    newMat = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[len(matrix) - 1 - j][len(matrix[0]) - 1 - i])
            newMat[i][j] = matrix[len(matrix) - 1 - j][len(matrix[0]) - 1 - i] / det(matrix)

    newMat[0][1] = -(newMat[0][1])
    newMat[1][0] = -(newMat[1][0])
    return newMat



def loadtxt(file):
    lines = open(file)
    vals = []
    for line in lines:
        vals.append(line.split())
    return(vals)



# print(transpose([[1, 2], [3, 4], [5, 6]]))

# ===== TESTING powers ===== #
#print(powers([2, 3, 4], 0, 2)) # [[1, 2, 4], [1, 3, 9], [1, 4, 16]]
#print(powers([], 0, 10)) # []
#print(powers([2], 0, 2)) # [[1, 2, 4]]
#print(powers([2], 0, 0)) # [[1]])
#print(powers([2], 0, -1)) # [[]])
#print(powers([2, 3], 0, 2)) # [[1, 2, 4], [1, 3, 9]])

# ===== TESTING matmul ===== #
#print(matmul([[0, 1], [1, 0]], [[1, 0], [0, -1]]))
#print(matmul([], [])) # []
#print(matmul([[2]], [[4]])) # [[8]]
#print(matmul([[2, 1]], [[4], [3]])) # [[11]]
#print(matmul([[1, 2], [3, 4]], [[0, 1], [1, 0]])) # [[2, 1], [4, 3]]
#print(matmul([[1, 2], [3, 4]], [[1, 0], [0, 1]])) # [[1, 2], [3, 4]]
#print(matmul([[1, 2], [3, 4], [5, 6]], [[1, 1, 1], [1, 1, 1]])) # [[3, 3, 3], [7, 7, 7], [11, 11, 11]]
#print(matmul([[1, 2, 3], [4, 5, 6]], [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]))
# [[74, 80, 86, 92], [173, 188, 203, 218]]
#print(matmul([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(matmul([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ===== TESTING invert ===== #
#print(invert([[1, 0], [0, 1]])) # [[1, 0], [0, 1]]
#print(invert([[0, 1], [1, 0]])) # [[0, 1], [1, 0]]
#print(invert([[1, 2], [3, 4]])) # [[-2.0, 1.0], [1.5, -0.5]]

# ===== TESTING loadtxt ===== #
#print(loadtxt("chirps.txt"))