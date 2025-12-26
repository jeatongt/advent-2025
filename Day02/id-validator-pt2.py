# python

def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]   

def id_is_invalid(id_number):
    id_str = str(id_number)
    length = len(id_str)
    substring_lengths = factors(length)
    for sub_len in substring_lengths:
        substrings = [id_str[i:i + sub_len] for i in range(0, len(id_str), sub_len)]
        if len(substrings) > 1 and len(set(substrings)) == 1:
            return True
    return False

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