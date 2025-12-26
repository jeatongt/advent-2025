# python

def highest_number_in_list(num_list):
    return max(num_list)

def highest_n_joltages_in_bank(battery_bank, num_batteries):
    battery_bank_list = list(battery_bank.strip())
    eligible_batteries = battery_bank_list[:len(battery_bank_list)-num_batteries+1]
    best_battery_list = []
    preceding_battery_position = -1
    for i in range(num_batteries):
        best_battery = highest_number_in_list(eligible_batteries)
        best_battery_list.append(best_battery)
        this_battery_position = battery_bank_list[preceding_battery_position+1:].index(best_battery) + preceding_battery_position+1
#        print(f"Eligible batteries: {eligible_batteries}, Best battery: {best_battery}, Position: {this_battery_position}, Preceding position: {preceding_battery_position}")
        preceding_battery_position = this_battery_position
        eligible_batteries = battery_bank_list[preceding_battery_position+1:len(battery_bank_list)-num_batteries+i+2]
    joltage_str = ''.join(best_battery_list)
    return int(joltage_str)

with open('Day03/batteries_actual.txt', 'r') as file:
    total_joltage = 0
    for line in file:
        joltage = highest_n_joltages_in_bank(line, 12)
        print(f"Highest joltage in bank {line.strip()} is {joltage}")
        total_joltage += joltage
    print(f"Total joltage from all banks: {total_joltage}")