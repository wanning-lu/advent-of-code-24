total = 0
input_string = ""

with open('input.txt', 'r') as file:
    for line in file:
        input_string += line # need to process as one large string due to continuation of do()'s and don't()'s

# valid_line represents the enabled mul() operations, while input_string denotes the rest of the string  
valid_line = input_string[:input_string.index("don't()")]
input_string = input_string[input_string.index("don't()") + 6:]
while len(input_string) != 0:
    
    if valid_line.find('mul(') == -1 and input_string.find('mul(') == -1:
        break
    if valid_line.find('mul(') == -1:
        if input_string.find("do()") == -1:
            break
        input_string = input_string[input_string.index('do()')+4:] # find where it is enabled again
        valid_line = input_string
        if input_string.find("don't()") != -1:
            valid_line = input_string[:input_string.index("don't()")] # store that string until it's disabled
            input_string = input_string[input_string.index("don't()") + 6:] # cut the line so it continues after valid string
        else:
            input_string = ""

    valid_line = valid_line[valid_line.index('mul('):] # first find the flag
    first_mul = valid_line[valid_line.index('mul(') + 4:valid_line.index(',')]
    second_mul = valid_line[valid_line.index(',') + 1:valid_line.index(')')]

    if first_mul.isdigit() and second_mul.isdigit():
        total += int(first_mul) * int(second_mul)

    valid_line = valid_line[valid_line.index('mul(') + 1:]
            
print(total)

### Runtime complexity: O(n), where n represents the total number of characters

### Space complexity: O(n), since we're storing the input_string in one continuous string
