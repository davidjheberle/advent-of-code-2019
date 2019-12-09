import getopt, sys

fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
unixOptions = "f:"
gnuOptions = "file="

try:
    arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

fileName = None
for currentArgument, currentValue in arguments:
    if currentArgument in ("-f", "--file"):
        fileName = currentValue
        print("Reading %s" % fileName)

file = open(fileName)
raw_input = file.read()
file.close()

def traverse_wire(wire):
    print(wire)
    directions = {'D': [0, -1], 'U': [0, 1], 'L': [-1, 0], 'R': [1, 0]}
    wire_info = {}
    x, y, count = 0, 0, 0
    for part in wire:
        for _ in range(int(part[1:])):
            offset = directions[part[0]]
            x += offset[0]
            y += offset[1]
            count += 1
            wire_info[(x, y)] = count
    return wire_info

def solutions(raw_input):
    wires = [x.split(',') for x in raw_input.strip().split('\n')]
    wire_one = traverse_wire(wires[0])
    wire_two = traverse_wire(wires[1])

    intersections = wire_one.keys() & wire_two.keys()

    fewest_steps = min(intersections, key=lambda x: wire_one[x] + wire_two[x])
    steps = wire_one[fewest_steps] + wire_two[fewest_steps]

    closest = min([intersection for intersection in intersections], key=lambda x: abs(x[0]) + abs(x[1]))
    distance = abs(closest[0]) + abs(closest[1])
    return ("Part 1", distance, "Part 2", steps)

print(solutions(raw_input))