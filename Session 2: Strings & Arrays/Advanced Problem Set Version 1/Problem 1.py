def transpose(matrix):
    # if not matrix or not matrix[0]:
    #     return []

    # rows = len(matrix)
    # cols = len(matrix[0])
    
    # transposed_matrix = [[0] * rows for _ in range(cols)]
    
    # for i in range(rows):
    #     for j in range(cols):
    #         transposed_matrix[j][i] = matrix[i][j]
    
    # print(transposed_matrix)

    print([[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))])
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)
