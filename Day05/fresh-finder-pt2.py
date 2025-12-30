# python

fresh_ranges = []
total_fresh_IDs = 0
with open('Day05/db-actual.txt', 'r') as file:
    for line in file:
        range_parts = line.strip().split('-')
        if range_parts[0] == '':
            continue
        if len(range_parts) == 2:
            range_start = int(range_parts[0])
            range_end = int(range_parts[1])
            fresh_ranges.append((range_start, range_end))
        if len(range_parts) == 1:
            continue
fresh_ranges.sort()
print(f"Fresh ranges: {fresh_ranges}")

this_range_max = -1
this_range = []
total_fresh_IDs = 0
for fresh_range in fresh_ranges:
    if this_range == []:
        this_range = [fresh_range[0], fresh_range[1]]
        this_range_max = fresh_range[1]
    if fresh_range[0] > this_range_max + 1:
        print(f"Gap detected before range: {fresh_range}")
        print(f"Finalized fresh ID set: {this_range}")
        total_fresh_IDs += this_range[1] - this_range[0] + 1
        this_range = [fresh_range[0], fresh_range[1]]
        this_range_max = fresh_range[1]
    else:
        if fresh_range[1] > this_range_max:
            this_range_max = fresh_range[1]
            this_range[1] = fresh_range[1]
if this_range != []:
    print(f"Finalized fresh ID set: {this_range}")
    total_fresh_IDs += this_range[1] - this_range[0] + 1


print(f"Total fresh IDs: {total_fresh_IDs}")
