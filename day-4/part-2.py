grid = []
found_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        grid.append(line[:-1])

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'A':
            makes_x = False
            # check top left square first
            if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == 'M':
                if i+1 < len(grid) and j+1 < len(grid[i]) and grid[i+1][j+1] == 'S':
                    makes_x = True
            elif i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == 'S': 
                if i+1 < len(grid) and j+1 < len(grid[i]) and grid[i+1][j+1] == 'M':
                    makes_x = True
            
            print(i, j, makes_x)
            # now check bottom left square
            if makes_x:
                if i+1 >= 0 and j-1 >= 0 and grid[i+1][j-1] == 'M':
                    if i-1 < len(grid) and j+1 < len(grid[i]) and grid[i-1][j+1] == 'S':
                        # print(i, j)
                        found_count += 1
                elif i+1 >= 0 and j-1 >= 0 and grid[i+1][j-1] == 'S': 
                    if i-1 < len(grid) and j+1 < len(grid[i]) and grid[i-1][j+1] == 'M':
                        # print(i, j)
                        found_count += 1

print(found_count)

### Runtime complexity: O(n), since it makes a constant check for characters at
### each occurrence of 'A'

### Space complexity: O(n), since we're storing the grid inside an array
