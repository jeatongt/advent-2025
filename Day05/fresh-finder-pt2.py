# python

fresh_ranges = []
fresh_IDs = set()
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
for fresh_range in fresh_ranges:
    fresh_IDs.update(range(fresh_range[0], fresh_range[1] + 1))

print(f"Total fresh IDs: {len(fresh_IDs)}")


