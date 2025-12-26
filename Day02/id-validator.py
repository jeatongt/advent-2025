# python

def id_is_invalid(id_number):
    """ID is invalid if it:
      - has an even number of digits
      - is made of two equal strings of digits"""
    id_str = str(id_number)
    length = len(id_str)
    if length % 2 != 0:
        return False
    half = length // 2
    return id_str[:half] == id_str[half:]

invalid_total = 0
with open('Day02/id_ranges_actual.txt', 'r') as file:
    for line in file:
        range_list = line.strip().split(',')
        for range_item in range_list:
            start_str, end_str = range_item.split('-')
            start_num = int(start_str)
            end_num = int(end_str)
            invalid_count = 0
            for id_number in range(start_num, end_num + 1):
                if id_is_invalid(id_number):
                    invalid_count += 1
                    invalid_total += id_number
            print(f"Range {start_num}-{end_num} has {invalid_count} invalid IDs.")
print(f"Total sum of invalid IDs: {invalid_total}")