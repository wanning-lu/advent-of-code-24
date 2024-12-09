safe_reports = 0
increasing = False
danger = False

def check_safety(report, danger):
    # first check if increasing or decreasing
    increasing = report[1] > report[0]

    # now check the entire report
    for i in range(len(report) - 1):
        
        # first check the safety criteria
        if ((report[i] > report[i+1] and increasing) or 
            (report[i] < report[i+1] and not increasing) or
            (abs(report[i] - report[i+1]) > 3) or
            (abs(report[i] - report[i+1]) < 1)):

            # if we've already removed one number, this report is unsafe
            if danger == True:
                return False
            # if we're at the end, it doesn't matter
            elif i == len(report) - 2:
                return True
            # remove the previous, current, and next number and check
            else:
                return (check_safety(report[:i] + report[i+1:], True) or 
                        check_safety(report[:i+1] + report[i+2:], True) or 
                        check_safety(report[:i-1] + report[i:], True))
    return True

# open the input and test safety of each line
with open('input.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))

        # first check if increasing or decreasing
        if check_safety(report, False):
            safe_reports += 1

print(safe_reports)

### Runtime complexity: O(n*4m), where n represents the number of reports and
### m represents the number of levels. At most, we will iterate over the report
### 4 times, since we can only have one strike.

### Space complexity: O(1), since we're only storing the number of safe reports