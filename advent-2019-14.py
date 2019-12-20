from collections import defaultdict
import re
import utils

PATTERN = re.compile(r'(\d+) (\w+)')
MAX = 1000000000000

def parse(lines):
    recipes = {}
    for line in lines:
        ingredients = {}
        last = None, None
        for match in PATTERN.finditer(line):
            if last[0] is not None:
                key, n = last
                ingredients[key] = n
            last = match.group(2), int(match.group(1))
        key, n = last
        recipes[key] = n, ingredients
    return recipes

def create(recipes, element, quantity):
    materials = defaultdict(int)
    materials[element] = quantity
    while True:
        try:
            key, n = next((key, n) for key, n in materials.items() if key != 'ORE' and n > 0)
            m, ingredients = recipes[key]
            x = (n + m - 1) // m
            materials[key] -= m * x
            for k, v in ingredients.items():
                materials[k] += x * v
        except StopIteration:
            break
    return materials['ORE']

def part1(lines):
    print("Part 1")
    recipes = parse(lines)
    return create(recipes, 'FUEL', 1)

def part2(lines):
    print("Part 2")
    recipes = parse(lines)
    good, bad = MAX // create(recipes, 'FUEL', 1), None
    while bad is None or good < bad - 1:
        quantity = 2 * good if bad is None else (good + bad) // 2
        ores = create(recipes, 'FUEL', quantity)
        if ores < MAX:
            good = quantity
        elif ores > MAX:
            bad = quantity
        else:
            return MAX
    return good

lines = utils.read_input().splitlines()
print(part1(lines))
print(part2(lines))