total = 0

with open('input.txt', 'r') as file:
    for line in file:
        while len(line) != 0:
            if line.find('mul(') == -1:
                break
            line = line[line.index('mul('):] # first find the flag
            first_mul = line[line.index('mul(') + 4:line.index(',')]
            second_mul = line[line.index(',') + 1:line.index(')')]

            if first_mul.isdigit() and second_mul.isdigit():
                total += int(first_mul) * int(second_mul)

            line = line[line.index('mul(') + 1:]

print(total)

### Runtime complexity: O(n), where n represents the total number of characters

### Space complexity: O(1), since we're only storing the cumulative total
