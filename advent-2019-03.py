import utils

def traverse_wire(wire):
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

def get_wires(raw_input):
    return [traverse_wire(x.split(',')) for x in raw_input.strip().split('\n')]

def get_intersections(wires):
    return wires[0].keys() & wires[1].keys()

def part1(intersections):
    print("Part 1")
    closest = min([intersection for intersection in intersections], key=lambda x: abs(x[0]) + abs(x[1]))
    distance = abs(closest[0]) + abs(closest[1])
    return distance

def part2(intersections, wires):
    print("Part 2")
    fewest_steps = min(intersections, key=lambda x: wires[0][x] + wires[1][x])
    steps = wires[0][fewest_steps] + wires[1][fewest_steps]
    return steps

wires = get_wires(utils.read_input())
intersections = get_intersections(wires)
print(part1(intersections))
print(part2(intersections, wires))