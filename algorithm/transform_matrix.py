matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

# 打印矩阵
def printMatrix(m):
    for ele in m:
        for e in ele:
            print('%3d' % e, end='')
        print('')

# 转置矩阵
def transformMatrix(m):
    new_matrix = [[] for i in range(len(m[0]))]
    for line in m:
        for ele in range(len(line)):
            new_matrix[ele].append(line[ele])
    return new_matrix

printMatrix(matrix)
print('-'*40)
printMatrix(transformMatrix(matrix))
