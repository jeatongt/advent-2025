# python
import math

junctions = {}
with open('Day08/junction-map-test.txt', 'r') as file:
    for line in file:
        coordinates = list(line.strip())
        print(coordinates)