# python

def is_a_beam(x, y, manifold):
    if manifold[y][x] == '|':
        return True
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

def split_beam_next_row(x, y, manifold):
    manifold[y+1][x-1] = '|'
    manifold[y+1][x+1] = '|'

def continue_beam_next_row(x, y, manifold):
    if y == len(manifold) - 1:
        return
    manifold[y+1][x] = '|'

def analyze_beam_path(manifold):
    beam_splits = 0
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if is_a_beam(x, y, manifold):
                if beam_splits_next_row(x, y, manifold):
                    split_beam_next_row(x, y, manifold)
                    beam_splits += 1
                else:
                    continue_beam_next_row(x, y, manifold)
    return beam_splits

manifold = []
with open('Day07/manifold-actual.txt', 'r') as file:
    for line in file:
        manifold_line = list(line.strip())
        manifold.append(manifold_line)
total_beam_splits = analyze_beam_path(manifold)
print(f"Total beam splits: {total_beam_splits}")