list1 = []
list2 = []

# open the input and read it into two separate arrays
with open('input.txt', 'r') as file:
    for line in file:
        list1.append(int(line[:6]))
        list2.append(int(line[-6:]))

list1 = sorted(list1)
list2 = sorted(list2)

print(sum([abs(value1 - value2) for value1, value2 in zip(list1, list2)]))

### Runtime complexity: O(nlogn), where it takes O(n) to parse through all IDs in the list,
### O(nlogn) to sort the lists, and O(n) to calculate the sum.

### Space complexity: O(n), where we use two arrays to store all IDs