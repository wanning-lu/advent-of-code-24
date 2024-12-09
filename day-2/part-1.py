safe_reports = 0
increasing = False

# open the input and test safety of each line
with open('input.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))

        # we know the max difference must be 3 and min difference must be 1
        if (abs(report[0] - report[-1]) > (3 * (len(report) - 1)) or 
            abs(report[0] - report[-1]) < (len(report) - 1)):
            continue

        # first check if increasing or decreasing
        increasing = report[1] > report[0]

        # extra check
        if report[1] == report[0]:
            continue

        # now check the entire report
        for i in range(len(report) - 1):
            
            # first check that the numbers are all increasing or decreasing
            if report[i] > report[i+1] and increasing:
                break
            if report[i] < report[i+1] and not increasing:
                break

            # next check the difference
            if abs(report[i] - report[i+1]) > 3 or abs(report[i] - report[i+1]) < 1:
                break
        else:
            # if we've reached this point, report is safe
            safe_reports += 1

print(safe_reports)

### Runtime complexity: O(n*m), where n represents the number of reports and
### m represents the number of levels

### Space complexity: O(1), since we're only storing the number of safe reports