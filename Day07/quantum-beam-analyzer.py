# python
import pprint

def is_a_beam(x, y, manifold):
    if manifold[y][x] == 'S':
        return True
    if manifold[y][x] == '^':
        return False
    if int(manifold[y][x]) > 0:
        return True
    return False

def is_a_splitter(x, y, manifold):
    if manifold[y][x] == '^':
        return True
    return False

def beam_splits_next_row(x, y, manifold):
    if y == len(manifold) - 1:
        return False
    return is_a_splitter(x, y+1, manifold)

def split_beam_next_row(x, y, manifold):
    manifold[y+1][x-1] = str(int(manifold[y+1][x-1]) + int(manifold[y][x]))
    manifold[y+1][x+1] = str(int(manifold[y+1][x+1]) + int(manifold[y][x]))
    manifold[y][x] = '0'

def continue_beam_next_row(x, y, manifold):
    if y == len(manifold) - 1:
        return
    if manifold[y][x] == 'S':
        manifold[y][x] = '0'
        manifold[y+1][x] = '1'
        return
    manifold[y+1][x] = str(int(manifold[y+1][x]) + int(manifold[y][x]))
    manifold[y][x] = '0'

def add_counts_to_manifold(manifold):
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if manifold[y][x] == '.':
                manifold[y][x] = '0'
    return manifold

def get_total_timelines(manifold):
    total = 0
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if is_a_beam(x, y, manifold):
                total += int(manifold[y][x])
    return total

def analyze_beam_path(manifold):
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if is_a_beam(x, y, manifold):
                if beam_splits_next_row(x, y, manifold):
                    split_beam_next_row(x, y, manifold)
                else:
                    continue_beam_next_row(x, y, manifold)

manifold = []
with open('Day07/manifold-actual.txt', 'r') as file:
    for line in file:
        manifold_line = list(line.strip())
        manifold.append(manifold_line)
manifold = add_counts_to_manifold(manifold)
analyze_beam_path(manifold)
pprint.pprint(manifold)
print(get_total_timelines(manifold))