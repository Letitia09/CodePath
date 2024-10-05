def local_maximums(grid):
    local_maxes = []
    for i in range(1,len(grid)-1):
        l=[]
        for j in range(1,len(grid[i])-1):
            max1=max(
                grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                grid[i][j-1], grid[i][j], grid[i][j+1],
                grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                )
            l.append(max1)
        local_maxes.append(l)
    print(local_maxes)
	        
grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
local_maximums(grid)

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
local_maximums(grid)
