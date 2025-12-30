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

map_list = []
with open('Day04/paper-map-actual.txt', 'r') as file:
    for map_line in file:
        map_line_list = list(map_line.strip())
        map_list.append(map_line_list)
free_roll_count = 0
for row in range(len(map_list)):
    for col in range(len(map_list[0])):
        if map_list[row][col] == '@':
            top_left, top, top_right, left, right, bottom_left, bottom, bottom_right = get_adjacent_rolls(map_list, row, col)
            if this_paper_roll_is_free(top_left, top, top_right, left, right, bottom_left, bottom, bottom_right):
                free_roll_count += 1
print(f"Total free paper rolls: {free_roll_count}")
