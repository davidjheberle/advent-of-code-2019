from math import atan2, hypot, pi
import getopt
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

def get_asteroid_map(raw_input):
    lines = raw_input.splitlines()
    asteroids = [(x, y) for y in range(len(lines))
        for x in range(len(lines[0])) if lines[y][x] == '#']
    return asteroids

def angle(a, b):
    return atan2(b[0] - a[0], a[1] - b[1]) % (2 * pi)

def visible(asteroids, a):
    return len(set(angle(a, b) for b in asteroids if a != b))

def part1(asteroids):
    print("Part 1")
    return max(visible(asteroids, a) for a in asteroids)

def part2(asteroids):
    print("Part 2")
    a = max(asteroids, key=lambda a: visible(asteroids, a))
    asteroids.remove(a)
    asteroids.sort(key=lambda b: hypot(b[0] - a[0], b[1] - a[1]))
    ranks = {b : sum(angle(a, b) == angle(a, c) for c in asteroids[:i])
        for i, b in enumerate(asteroids)}
    x, y = sorted(asteroids, key=lambda b: (ranks[b], angle(a, b)))[199]
    return x * 100 + y

asteroids = get_asteroid_map(read_input())
print(part1(asteroids))
print(part2(asteroids))