def diagonal_sum(grid):
    sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row == col or row + col == len(grid)-1:
                sum += grid[row][col]
    print(sum)
	            
grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum(grid)

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
diagonal_sum(grid)

grid = [
	[5]
]
diagonal_sum(grid)
