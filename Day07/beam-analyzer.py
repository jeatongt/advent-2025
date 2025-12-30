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
    return is_a_splitter(x, y+1, manifold)

manifold = []
with open('Day06/manifold-test.txt', 'r') as file:
    for line in file:
        manifold_line = list(line.strip())
        manifold.append(manifold_line)