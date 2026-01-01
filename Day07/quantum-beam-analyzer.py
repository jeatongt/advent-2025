# python
import pprint

beam_paths = [] # This list will hold all the possible paths that beams might take
def initialize_beam_paths(manifold):
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if is_a_source(x, y, manifold):
                this_path = [(x, y)]
                beam_paths.append(this_path)
    return beam_paths

def is_a_source(x, y, manifold):
    if manifold[y][x] == 'S':
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

def advance_beam_path(path, manifold):
    x, y = path[-1]
    print(f"y == {y}, Beams so far:", len(beam_paths))
    if y == len(manifold) - 1:
        return
    if beam_splits_next_row(x, y, manifold):
        path.append((x-1, y+1))
        right_path = path + [(x+1, y+1)]
        advance_beam_path(path, manifold)
        beam_paths.append(right_path)
        advance_beam_path(right_path, manifold)
    else:
        path.append((x, y+1))
        advance_beam_path(path, manifold)

def analyze_beam_path(manifold):
    beam_paths = initialize_beam_paths(manifold)
    for path in beam_paths:
        advance_beam_path(path, manifold)
    return len(beam_paths)


manifold = []
with open('Day07/manifold-test.txt', 'r') as file:
    for line in file:
        manifold_line = list(line.strip())
        manifold.append(manifold_line)
total_timeline_splits = analyze_beam_path(manifold)
print(f"Total beam paths: {total_timeline_splits}")
# pprint.pprint(beam_paths)
