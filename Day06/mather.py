# python
import math

def get_operands(worksheet, column):
    return [int(row[column]) for row in worksheet]

operands = []
operators = []
answers = []
with open("Day06/homework_actual.txt") as file:
    for line in file:
        this_line = line.split()
        if this_line[0] == "+" or this_line[0] == "*":
            operators = this_line
        else:
            operands.append(this_line)
print("Operators:", operators)
print("Operands:", operands)
print("First column of operands:", get_operands(operands, 0))
print(len(operators))
for i in range(len(operators)):
    print("Processing column", i)
    if operators[i] == "+":
        answers.append(sum(get_operands(operands, i)))
    elif operators[i] == "*":
        answers.append(math.prod(get_operands(operands, i)))
print("Total of answers:", sum(answers))