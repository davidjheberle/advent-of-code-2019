from collections import deque
import getopt
import intcode
import sys

def read_input():
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
    return raw_input

def neighbors(x, y):
    return [((x, y - 1), 1), ((x, y + 1), 2), ((x - 1, y), 3), ((x + 1, y), 4)]

def path(src, dst, free):
    if src == dst:
        return []
    seen = set()
    queue = deque(((src, []), ))
    while True:
        pos1, path = queue.popleft()
        for pos2, d in neighbors(*pos1):
            if pos2 == dst:
                return path + [(pos2, d)]
            if pos2 in seen or pos2 not in free:
                continue
            queue.append((pos2, path + [(pos2, d)]))
            seen.add(pos2)

def explore(program):
    visited = set()
    free = set()
    oxygen = None
    pending = {(0, 0)}
    pos1 = 0, 0
    inputs = []

    while pending:
        target, status = pending.pop(), 1
        visited.add(target)
        for pos2, d in path(pos1, target, free):
            inputs.append(d)
            status = program.run(inputs)
            if status == 0:
                break
            pos1 = pos2
            if status == 2:
                oxygen = pos1
        if status:
            free.add(pos1)
        pending.update(pos2 for pos2, _ in neighbors(*pos1) if pos2 not in visited)

    return oxygen, free

def part1(program):
    print("Part 1")
    oxygen, free = explore(program)
    return len(path((0, 0), oxygen, free))

def part2(program):
    print("Part 2")
    oxygen, free = explore(program)
    return max(len(path(oxygen, pos, free)) for pos in free)

raw_input = read_input()
print(part1(intcode.Computer(raw_input)))
print(part2(intcode.Computer(raw_input)))