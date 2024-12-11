
grid = []
word = ['X', 'M', 'A', 'S']
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
found_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        grid.append(line[:-1])

def find_word(i, j, index):
    # checking if the index will be out of bounds
    if ((i + directions[index][0] * 3) >= len(grid) or (i + directions[index][0] * 3) < 0 or
    (j + directions[index][1] * 3) >= len(grid[i]) or (j + directions[index][1] * 3) < 0):
        return 0

    # checking if the boxes going in a certain direction satisfies the requirements
    if (grid[i + directions[index][0]][j + directions[index][1]] == 'M' and
        grid[i + directions[index][0] * 2][j + directions[index][1] * 2] == 'A' and
        grid[i + directions[index][0] * 3][j + directions[index][1] * 3] == 'S'):
        return 1
    return 0

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 'X':
            for index in range(len(directions)):
                found_count += find_word(i, j, index)

print(found_count)

### Runtime complexity: O(n), since if a square is X, then it iterates 8 times, making the runtime
### O(8n), where n represents the number of characters in the word search

### Space complexity: O(n), since we're storing the grid inside an array
