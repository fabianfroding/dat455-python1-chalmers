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
    mat1Rows = len(mat1[0])
    mat1Cols = len(mat1)
    mat2Rows = len(mat2[0])
    mat2Cols = len(mat2)
    newMat = [[0 for x in range(mat1Rows)] for y in range(mat1Cols)]

    for i in range(0, mat1Cols):
        for j in range(0, mat1Rows):
            k = mat1[i][j] * mat2[j][i]
            #print(mat1[i][j])
            print(mat2[mat2Rows - 1 - j][mat2Cols - 1 - i])
            #print(k)
            #print(str(mat1[i][j]) + " * " + str(mat2[j][i]) + " = " + str(k))
            #newMat[i][j] = mat1[i][j]

    return newMat


# def invert():
   #   print('invert called')



# def loadtxt():
    #  print('loadtxt called')



# print(transpose([[1, 2], [3, 4], [5, 6]]))

# print(powers([2, 3, 4], 0, 2)) # [[1, 2, 4], [1, 3, 9], [1, 4, 16]]
# print(powers([], 0, 10)) # []
# print(powers([2], 0, 2)) # [[1, 2, 4]]
# print(powers([2], 0, 0)) # [[1]])
# print(powers([2], 0, -1)) # [[]])
# print(powers([2, 3], 0, 2)) # [[1, 2, 4], [1, 3, 9]])

s1 = [[0, 1], [1, 0]]
s3 = [[1, 0], [0, -1]]

print(matmul(s1, s3))