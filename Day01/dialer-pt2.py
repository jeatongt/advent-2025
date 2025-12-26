# python

START_POSITION = 50

def get_next_position_and_zeros(current_position, direction, steps):
    num_zeros = 0
    num_zeros = steps // 100
    steps_mod = steps % 100
    if direction == 'L':
        next_position = current_position - steps_mod
        if current_position == 0 and next_position < 0:
            next_position = next_position + 100
        if current_position > 0 and next_position < 0:
            next_position = next_position + 100
            num_zeros += 1
        if next_position == 0:
            num_zeros += 1
    elif direction == 'R':
        next_position = current_position + steps_mod
        if next_position >= 100:
            next_position = next_position - 100
            num_zeros += 1
    else:
        raise ValueError("Invalid move. Use 'L' for left and 'R' for right.")
    print(f"Moved {direction}{steps}: from {current_position} to {next_position}. Zeros: {num_zeros}")
    return next_position, num_zeros

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
    clicked_on_zero = 0
    if position == 0:
        clicked_on_zero += 1
    for line in file:
        moves = parse_moves(line)
        for direction, steps in moves:
            position, zeros = get_next_position_and_zeros(position, direction, steps)
        clicked_on_zero += zeros
    print(f"Final Position: {position}")
    print(f"Times clicked on 0: {clicked_on_zero}")