# python

def ingredient_is_fresh(ingredient_id, fresh_ranges):
    for range_start, range_end in fresh_ranges:
        if range_start <= ingredient_id <= range_end:
            return True
    return False

fresh_ranges = []
fresh_ingredients = []
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
            if ingredient_is_fresh(int(line.strip()), fresh_ranges):
                fresh_ingredients.append(int(line.strip()))
print(f"Fresh ingredients: {fresh_ingredients}")
print(f"Total fresh ingredients: {len(fresh_ingredients)}")