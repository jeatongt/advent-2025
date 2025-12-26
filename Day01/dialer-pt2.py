# python

START_POSITION = 50

def get_next_position(current_position, direction, steps):
    if direction == 'L':
        next_position = current_position - steps
        next_position = next_position % 100
        if next_position < 0:
            next_position = next_position + 100
    elif direction == 'R':
        next_position = current_position + steps
        next_position = next_position % 100
        if next_position >= 100:
            next_position = next_position - 100
    else:
        raise ValueError("Invalid move. Use 'L' for left and 'R' for right.")
    print(f"Moved {direction}{steps}: from {current_position} to {next_position}")
    return next_position

def parse_moves(moves_str):
    moves = []
    for move in moves_str.split(','):
        move = move.strip()
        direction = move[0]
        steps = int(move[1:])
        moves.append((direction, steps))
    return moves

with open('Day01/rotations_actual.txt', 'r') as file:
    position = START_POSITION
    landed_on_zero = 0
    if position == 0:
        landed_on_zero += 1
    for line in file:
        moves = parse_moves(line)
        for direction, steps in moves:
            position = get_next_position(position, direction, steps)
        if position == 0:
            landed_on_zero += 1
    print(f"Final Position: {position}")
    print(f"Times Landed on 0: {landed_on_zero}")