# python

fresh_ranges = []
fresh_sets = []
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

this_fresh_set = set()
for fresh_range in fresh_ranges:
    if not this_fresh_set:
        this_fresh_set.update(range(fresh_range[0], fresh_range[1] + 1))
    else:
        if fresh_range[0] <= max(this_fresh_set) + 1:
            this_fresh_set.update(range(fresh_range[0], fresh_range[1] + 1))
            print(f"Merged fresh ID set: {this_fresh_set}")
        else:
            fresh_sets.append(this_fresh_set)
            print(f"Finalized fresh ID set: {this_fresh_set}")
            this_fresh_set = set()
            this_fresh_set.update(range(fresh_range[0], fresh_range[1] + 1))
fresh_sets.append(this_fresh_set)
print(f"Finalized fresh ID set: {this_fresh_set}")

for fresh_set in fresh_sets:
    total_fresh_IDs += len(fresh_set)
print(f"Total fresh IDs: {total_fresh_IDs}")
