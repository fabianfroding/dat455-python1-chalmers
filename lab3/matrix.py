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



# def matmul(mat1, mat2):
   #   print('matmul called')



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