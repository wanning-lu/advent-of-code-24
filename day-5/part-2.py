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
total_invalid = 0
is_valid = 0
# read through each update and correct the ones which are wrong
# if we encounter a page that's placed wrong, we'll place it before
# the first occurrence
with open('updates.txt', 'r') as file:
    for line in file:
        update = list(map(int, line.split(',')))
        seen = []
        invalid = False
        for i, num in enumerate(update):
            if num not in go_before:
                continue

            for prev in update[:i]:
                if prev in go_before[num]:
                    invalid = True
                    # now we need to put the num before the prev, we're going to just
                    # shift everything else up
                    update[update.index(prev) + 1:] = update[update.index(prev):i] + update[i+1:]
                    update[update.index(prev)] = num
                    break

        # let's check validity again lol
        seen = []
        check_valid = True
        for num in update:
            if num not in go_before:
                seen.append(num)
                continue

            for prev in seen:
                if prev in go_before[num]:
                    check_valid = False
                    break

            if not check_valid: break
            seen.append(num)
        
        if check_valid:
            is_valid += 1

        if invalid:
            total_invalid += 1
            total += update[math.floor(len(update)/2)] # add the middle number

print(is_valid)
print(total_invalid)
print(total)

### Same runtime and spacetime complexity as part 1, since we implement a form
### of bubble search
        

        
