from collections import defaultdict
import utils

def adjacent(pos, grid=None):
    if grid is None:
        yield pos[0] + 1, pos[1]
        yield pos[0] - 1, pos[1]
        yield pos[0], pos[1] + 1
        yield pos[0], pos[1] - 1
    else:
        width, height = len(grid[0]), len(grid)
        x, y = pos
        a = grid[x][y + 1] if y + 1 < height else '.'
        yield 1 if a == '#' else 0
        a = grid[x][y - 1] if 0 < y else '.'
        yield 1 if a == '#' else 0
        a = grid[x + 1][y] if x + 1 < width else '.'
        yield 1 if a == '#' else 0
        a = grid[x - 1][y] if 0 < x else '.'
        yield 1 if a == '#' else 0

def part1(grid):
    print("Part 1")
    states = set()
    width, height = len(grid[0]), len(grid)
    while True:
        state = tuple(tuple(i) for i in grid)
        if state in states:
            total = 0
            for i in range(width):
                for j in range(height):
                    if grid[i][j] == '#':
                        total += 2 ** (i * len(grid) + j)
            return total
        states.add(state)
        tmp = [['.' for _ in range(width)] for _ in range(height)]
        for i in range(width):
            for j in range(height):
                if grid[i][j] == '#' and sum(adjacent((i, j), grid)) == 1:
                    tmp[i][j] = '#'
                if grid[i][j] == '.' and 1 <= sum(adjacent((i, j), grid)) <= 2:
                    tmp[i][j] = '#'
        
        grid = tmp

def part2(grid):
    print("Part 2")
    levels = 100
    minutes = 200
    connections = defaultdict(list)
    cells = {}
    width, height = len(grid[0]), len(grid)
    for i in range(width):
        for j in range(height):
            if i == 2 and j == 2:
                continue
            for level in range(-levels, levels + 1):
                cells[(i, j, level)] = False
                if level == 0 and grid[i][j] == '#':
                    cells[(i, j, level)] = True
                for x, y in adjacent((i, j)):
                    if 0 <= x < width and 0 <= y < height and (x, y) != (2, 2):
                        connections[(i, j, level)].append((x, y, level))
                if i == 0 and level - 1 >= -levels:
                    connections[(i, j, level)].append((1, 2, level - 1))
                if j == 0 and level - 1 >= -levels:
                    connections[(i, j, level)].append((2, 1, level - 1))
                if j == height - 1 and level - 1 >= -levels:
                    connections[(i, j, level)].append((2, 3, level - 1))
                if i == width - 1 and level - 1 >= -levels:
                    connections[(i, j, level)].append((3, 2, level - 1))
                if i == 1 and j == 2 and level + 1 <= levels:
                    for y in range(height):
                        connections[(i, j, level)].append((0, y, level + 1))
                if i == 2 and j == 1 and level + 1 <= levels:
                    for x in range(width):
                        connections[(i, j, level)].append((x, 0, level + 1))
                if i == 2 and j == 3 and level + 1 <= levels:
                    for x in range(width):
                        connections[(i, j, level)].append((x, height - 1, level + 1))
                if i == 3 and j == 2 and level + 1 <= levels:
                    for y in range(height):
                        connections[(i, j, level)].append((width - 1, y, level + 1))
    
    for _ in range(minutes):
        tmp = {}
        for k, _ in cells.items():
            alive = 0
            for y in connections[k]:
                if cells[y]:
                    alive += 1
            if (cells[k] and alive != 1) or (not cells[k] and alive not in [1, 2]):
                tmp[k] = False
            else:
                tmp[k] = True
        cells = tmp

    return sum(cells.values())

raw_input = utils.read_input().splitlines()
grid = [list(i) for i in raw_input]
print(part1(grid))
print(part2(grid))