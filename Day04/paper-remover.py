# python

def get_adjacent_rolls(map_list, row, col):
    top_left = map_list[row-1][col-1] if row > 0 and col > 0 else ' '
    top = map_list[row-1][col] if row > 0 else ' '
    top_right = map_list[row-1][col+1] if row > 0 and col < len(map_list[0])-1 else ' '
    left = map_list[row][col-1] if col > 0 else ' '
    right = map_list[row][col+1] if col < len(map_list[0])-1 else ' '
    bottom_left = map_list[row+1][col-1] if row < len(map_list)-1 and col > 0 else ' '
    bottom = map_list[row+1][col] if row < len(map_list)-1 else ' '
    bottom_right = map_list[row+1][col+1] if row < len(map_list)-1 and col < len(map_list[0])-1 else ' '
    return top_left, top, top_right, left, right, bottom_left, bottom, bottom_right

def this_paper_roll_is_free(top_left, top, top_right, left, right, bottom_left, bottom, bottom_right):
    max_adjacent_rolls = 3
    adjacent_rolls = sum([top_left == '@', top == '@', top_right == '@',
                          left == '@', right == '@',
                          bottom_left == '@', bottom == '@', bottom_right == '@'])
    return adjacent_rolls <= max_adjacent_rolls

def remove_rolls(map_list):
    rolls_removed = 0
    for row in range(len(map_list)):
        for col in range(len(map_list[0])):
            if map_list[row][col] == '@':
                top_left, top, top_right, left, right, bottom_left, bottom, bottom_right = get_adjacent_rolls(map_list, row, col)
                if this_paper_roll_is_free(top_left, top, top_right, left, right, bottom_left, bottom, bottom_right):
                    rolls_removed += 1
                    map_list[row][col] = '.'  # Remove the roll
    print(f"Rolls removed: {rolls_removed}")
    return rolls_removed

map_list = []
with open('Day04/paper-map-actual.txt', 'r') as file:
    for map_line in file:
        map_line_list = list(map_line.strip())
        map_list.append(map_line_list)
total_rolls_removed = 0
rolls_removed_this_pass = remove_rolls(map_list)  # Initial removal
while rolls_removed_this_pass > 0:
    total_rolls_removed += rolls_removed_this_pass
    rolls_removed_this_pass = remove_rolls(map_list)
print(f"Total rolls removed: {total_rolls_removed}")