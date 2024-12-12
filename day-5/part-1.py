import math

go_before = {}

# store which numbers must go before a certain number
with open('keys.txt', 'r') as file:
    for line in file:
        key = int(line[:2])
        value = int(line[3:])
        if key not in go_before:
            go_before[key] = []
        go_before[key].append(value)

total = 0
# read through each update and determine if it's valid
with open('updates.txt', 'r') as file:
    for line in file:
        update = list(map(int, line.split(',')))
        seen = []
        valid = True
        for num in update:
            if num not in go_before:
                seen.append(num)
                continue

            for prev in seen:
                if prev in go_before[num]:
                    valid = False
                    break

            if not valid: break
            seen.append(num)
        
        if valid:
            total += update[math.floor(len(update)/2)] # add the middle number

print(total)

### Runtime complexity: O(m^2) for each of the updates, where m represents the
### number of pages. Otherwise, the overall complexity should be O(k*m^2 + n) where
### k is the number of updates and n is the number of keys

### Spacetime complexity: O(n + m) since we're storing a dictionary of all the
### keys, and we're putting the pages into a list at any given line
        

        
