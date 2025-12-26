# python

def highest_number_in_list(num_list):
    return max(num_list)

def highest_joltage_in_bank(battery_bank):
    battery_list = list(battery_bank.strip())
    best_first_battery = highest_number_in_list(battery_list[:len(battery_list)-1])
    best_second_battery = highest_number_in_list(battery_list[battery_list.index(best_first_battery)+1:len(battery_list)])
    return 10*int(best_first_battery) + int(best_second_battery)

with open('Day03/batteries_actual.txt', 'r') as file:
    total_joltage = 0
    for line in file:
        joltage = highest_joltage_in_bank(line)
        print(f"Highest joltage in bank {line.strip()} is {joltage}")
        total_joltage += joltage
    print(f"Total joltage from all banks: {total_joltage}")