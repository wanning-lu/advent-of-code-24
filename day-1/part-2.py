list1_ids = set()
list2 = []
list2_freq = {}

# open the input and read it into two separate arrays
with open('input.txt', 'r') as file:
    for line in file:
        list1_ids.add(int(line[:6]))
        list2.append(int(line[-6:]))

for location_id in list2:
    if location_id not in list1_ids:
        continue
    if location_id not in list2_freq:
        list2_freq[location_id] = 1
    else:
        list2_freq[location_id] += 1

sim_score = 0
for key, value in zip(list2_freq.keys(), list2_freq.values()):
    sim_score += key * value

print(sim_score)

### Runtime complexity: O(n), where it takes O(n) to parse through all IDs in the list,
### O(n) to find the occurrences of each ID, and O(n) to go through all keys and values in the dict.

### Space complexity: O(n), where we use a set to store IDs that occur in list 1, 
### an array to store all values in the second list, and a dictionary to store
### the occurrences of values in the second list.