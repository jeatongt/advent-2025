# python
import math
import re

# Still doing it wrong. I need turn the whole sheet into a byte array
# and then process each column as a byte array, not split by spaces

def get_operands(worksheet, column):
    return [int(number) for number in worksheet[column]]

worksheet_unrotated = []
with open("Day06/homework_actual.txt") as file:
    for line in file:
        maybe_operators = line.split()
        if maybe_operators[0] == "+" or maybe_operators[0] == "*":
            operators = maybe_operators
        else:
            this_line = list(line.rstrip('\n'))
            worksheet_unrotated.append(this_line)
# print(worksheet_unrotated)
worksheet = [list(row) for row in zip(*worksheet_unrotated)]
# print(worksheet)
operands = []
operand_row = []
for row in worksheet:
    joined_row = ''.join(row)
    if joined_row.strip().isdigit():
        operand_row.append(joined_row.strip())
    else:
        if operand_row:
            operands.append(operand_row)
            operand_row = []
if operand_row:
    operands.append(operand_row)
print("Operators:", operators)
print("Operands:", operands)
print("First column of operands:", get_operands(operands, 0))
print(len(operators))
answers = []
for i in range(len(operators)):
    print("Processing column", i)
    if operators[i] == "+":
        answers.append(sum(get_operands(operands, i)))
    elif operators[i] == "*":
        answers.append(math.prod(get_operands(operands, i)))
print("Total of answers:", sum(answers))