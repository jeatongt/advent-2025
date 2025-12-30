# python
import math
import re

# So what got me here is that the number of spaces in front of each operand matter.
# So I'll need to parse out the operands differently.

def get_operands(worksheet, column):
    return [int(row[column]) for row in worksheet]

def join_item_to_precending_spaces(line_with_spaces):
    joined_line = []
    current_item = ""
    for item in line_with_spaces:
        if item.isspace():
            current_item += item
        else:
            current_item += item
            joined_line.append(current_item)
            current_item = ""
    return joined_line

operands = []
operators = []
answers = []
with open("Day06/homework_test.txt") as file:
    for line in file:
        this_line = line.split()
        if this_line[0] == "+" or this_line[0] == "*":
            operators = this_line
        else:
            this_line_with_spaces = re.split(r'(\s+)', line.rstrip('\n'))
            # print("Line with spaces:", this_line_with_spaces)
            this_line_with_spaces_not_empty = [item for item in this_line_with_spaces if item != '']
            # print("Line with spaces not empty:", this_line_with_spaces_not_empty)
            operands.append(join_item_to_precending_spaces(this_line_with_spaces_not_empty))
print("Operators:", operators)
print("Operands:", operands)
# print("First column of operands:", get_operands(operands, 0))
print(len(operators))
# for i in range(len(operators)):
#     print("Processing column", i)
#     if operators[i] == "+":
#         answers.append(sum(get_operands(operands, i)))
#     elif operators[i] == "*":
#         answers.append(math.prod(get_operands(operands, i)))
# print("Total of answers:", sum(answers))