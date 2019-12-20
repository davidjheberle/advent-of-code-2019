from collections import defaultdict
from itertools import count
import utils

def parse_input(raw_input):
    maze = {}
    goals = {}
    for y, row in enumerate(raw_input.split('\n')):
        for x, cell in enumerate(row):
            p = complex(x, y)
            maze[p] = cell
            if cell in '#.': continue
            goals[cell] = p
    return maze, goals

def find_links(maze, start):
    links = {}
    walk = defaultdict(lambda: [99999, {}])
    walk[start] = (0, set())
    next = [(start, set())]
    for step in count(1):
        if len(next) == 0: break
        cur, next = next, []
        for p, ds in cur:
            for d in [1, 1j, -1, -1j]:
                c = maze[p + d]
                if c == '#' or walk[p + d][0] <= step: continue
                if c.islower():
                    links[c] = (step, ds)
                nds = ds
                if c.isupper():
                    nds = nds | {c.lower()}
                walk[p + d] = (step, nds)
                next.append((p + d, nds))
    return links

def part1(raw_input):
    print("Part 1")
    maze, goals = parse_input(raw_input)
    all_keys = {k for k in goals if k.islower()}
    links = {'@': find_links(maze, goals['@'])}
    for k in all_keys:
        links[k] = find_links(maze, goals[k])
    
    cache = {}
    def walk(name, need_keys):
        if len(need_keys) == 0: return 0
        key = name + ''.join(need_keys)
        if key in cache: return cache[key]
        shortest = float('inf')
        for k in need_keys:
            l, doors = links[name][k]
            # check if too long
            if l >= shortest: continue
            # check if unable to open
            if not doors.isdisjoint(need_keys): continue
            tail = walk(k, need_keys - {k})
            if shortest > l + tail: shortest = l + tail
        cache[key] = shortest
        return shortest

    return walk('@', all_keys)

def part2(raw_input):
    print("Part 2")
    maze, goals = parse_input(raw_input)
    s = goals['@']
    maze[s] = maze[s + 1] = maze[s - 1] = maze[s + 1j] = maze[s - 1j] = '#'
    maze[s + 1 + 1j] = '1'; goals['1'] = s + 1 + 1j
    maze[s - 1 + 1j] = '2'; goals['2'] = s - 1 + 1j
    maze[s + 1 - 1j] = '3'; goals['3'] = s + 1 - 1j
    maze[s - 1 - 1j] = '4'; goals['4'] = s - 1 - 1j
    all_keys = {k for k in goals if k.islower()}
    links = {}
    for k in '1234':
        links[k] = find_links(maze, goals[k])
    for k in all_keys:
        links[k] = find_links(maze, goals[k])

    cache = {}
    def walk(names, need_keys):
        if len(need_keys) == 0: return 0
        key = ''.join(sorted(names)) + ''.join(sorted(need_keys))
        if key in cache: return cache[key]
        shortest = float('inf')
        for k1 in need_keys:
            for k2 in names:
                if k1 not in links[k2]: continue
                l, doors = links[k2][k1]
                # check if too long
                if l >= shortest: continue
                # check if unable to open
                if not doors.isdisjoint(need_keys): continue
                tail = walk((names - {k2}) | {k1}, need_keys - {k1})
                if shortest > l + tail: shortest = l + tail
        cache[key] = shortest
        return shortest
    return walk({'1', '2', '3', '4'}, all_keys)

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))