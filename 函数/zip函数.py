
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print('matrix=',matrix)
print(list(zip(matrix[0],matrix[1],matrix[2])))
print(list(zip(*matrix)))
print(list(zip(*matrix))[::-1])
