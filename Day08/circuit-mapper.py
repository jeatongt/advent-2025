# python
import math
import pprint

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)



junctions = []
circuits = []
distances = []
with open('Day08/junction-map-actual.txt', 'r') as file:
    for line in file:
        coordinates = list(int(x) for x in line.strip().split(","))
        junctions.append(tuple(coordinates))
for junction in junctions:
    circuit = []
    circuit.append(junction)
    circuits.append(circuit)
# Calculate distances between all pairs of junctions
for junction1 in junctions:
    for junction2 in junctions:
        if junction1 != junction2:
            dist = (junction1, junction2, distance(junction1, junction2))
            distances.append(dist)
# Sort the distances for each junction
sorted_distances = sorted(distances, key=lambda x: x[2])
distances = sorted_distances
# Build circuitsn from n closest junctions
n = 1
for dist in distances:
    if n > 2000: # doubled because each junction appears twice in distances
        break
    n += 1
    junction1, junction2, dist_value = dist
    circuit1 = None
    circuit2 = None
    for circuit in circuits:
        if junction1 in circuit:
            circuit1 = circuit
        if junction2 in circuit:
            circuit2 = circuit
    if circuit1 is not None and circuit2 is not None and circuit1 != circuit2:
        # Merge circuits
        circuit1.extend(circuit2)
        circuits.remove(circuit2)
list_lengths = [len(circuit) for circuit in circuits]
sorted_lengths = sorted(list_lengths, reverse=True)
print("Lengths of circuits (largest to smallest):", sorted_lengths)
# pprint.pprint(junctions)
# pprint.pprint(circuits)