import getopt
import networkx
import numpy
import string
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

array_to_string = lambda a: '\n'.join([''.join([str(c) for c in line]) for line in a])
is_in_map = lambda n, w, b = 0: all(0 + b <= n[i] < w.shape[i] - b for i in (0, 1))
is_empty = lambda n, w: is_in_map(n, w) and w[n[0], n[1]] == '.'
move = lambda n, d, a = 1: (n[0] + a * d[0], n[1] + a * d[1], *n[2:])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_maze(raw_input):
    return numpy.array([[*l] for l in raw_input.strip('\n').split('\n')])

def explore_maze(maze, total_levels = 1):
    portals = [{}, {}]
    for i in numpy.ndindex(maze.shape):
        c1 = maze[i]
        if c1 not in string.ascii_uppercase:
            continue
        for d in directions[:2]:
            if not is_in_map(move(i, d), maze):
                continue
            c2 = maze[move(i, d)]
            if c2 not in string.ascii_uppercase:
                continue
            pos = move(i, d, -1) if is_empty(move(i, d, -1), maze) else move(i, d, 2)
            portals[is_in_map(pos, maze, b = 4)][c1 + c2] = pos

    G = networkx.Graph()
    for level in range(total_levels):
        nodes = [(*i, level) for i in numpy.ndindex(maze.shape)]
        G.add_nodes_from(nodes)
        G.add_edges_from((n, move(n, d)) for d in directions for n in nodes if is_in_map(move(n, d), maze))
        G.remove_nodes_from((*x, level) for x in numpy.argwhere(maze != '.'))

        for k, inner in portals[1].items():
            if total_levels > 1:
                G.add_edge((*inner, level), (*portals[0][k], level + 1))
                G.add_edge((*portals[0][k], level), (*inner, level - 1))
            else:
                G.add_edge((*inner, 0), (*portals[0][k], 0))

    start = (*portals[0]['AA'], 0)
    goal = (*portals[0]['ZZ'], 0)
    return next(networkx.shortest_simple_paths(G, start, goal))

def part1(raw_input):
    print("Part 1")
    result = explore_maze(get_maze(raw_input), 1)
    return len(result) - 1

def part2(raw_input):
    print("Part 2")
    result = explore_maze(get_maze(raw_input), 40)
    return len(result) - 1

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))