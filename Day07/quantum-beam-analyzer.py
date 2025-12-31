# python
import pprint

def is_a_beam(x, y, manifold):
    if manifold[y][x] == '|':
        return True
    if manifold[y][x] == 'S':
        return True
    return False

def is_a_splitter(x, y, manifold):
    if manifold[y][x] == '^':
        return True
    if manifold[y][x] == '/':
        return True
    if manifold[y][x] == 'l':
        return True
    return False

def beam_splits_next_row(x, y, manifold):
    if y == len(manifold) - 1:
        return False
    return is_a_splitter(x, y+1, manifold)

def split_beam_next_row(x, y, manifold, split_already_this_iteration):
    if manifold[y+1][x] == '^' and split_already_this_iteration == 0:
        manifold[y+1][x-1] = '|'
        manifold[y+1][x] = '/'
        return 1
    elif manifold[y+1][x] == '/' and split_already_this_iteration == 0:
        manifold[y+1][x+1] = '|'
        manifold[y+1][x] = 'l'
        return 1
    else:
        return 0

def continue_beam_next_row(x, y, manifold):
    if y == len(manifold) - 1:
        return
    manifold[y+1][x] = '|'

def analyze_beam_path(manifold):
    last_timeline_splits = -1
    timeline_splits = 0
    split_this_iteration = 0
    while timeline_splits != last_timeline_splits:
        last_timeline_splits = timeline_splits
        print(f"Manifold so far with {timeline_splits} splits:")
        pprint.pprint(manifold)
        for y in range(len(manifold)):
            for x in range(len(manifold[0])):
                if is_a_beam(x, y, manifold):
                    if beam_splits_next_row(x, y, manifold):
                        split_this_iteration += split_beam_next_row(x, y, manifold, split_this_iteration)
                    else:
                        continue_beam_next_row(x, y, manifold)
        if split_this_iteration > 0:
            timeline_splits += 1
            split_this_iteration = 0
    return timeline_splits

manifold = []
with open('Day07/manifold-test.txt', 'r') as file:
    for line in file:
        manifold_line = list(line.strip())
        manifold.append(manifold_line)
total_timeline_splits = analyze_beam_path(manifold)
print(f"Total timeline splits: {total_timeline_splits}")