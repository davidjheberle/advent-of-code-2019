import utils

def calc_fuel(mass):
    return mass // 3 - 2

def part1(masses):
    print("Part 1")
    sum = 0
    for mass in masses:
        sum += calc_fuel(mass)
    return sum

def part2(masses):
    print("Part 2")
    sum = 0
    for mass in masses:
        while True:
            result = calc_fuel(mass)
            if result > 0:
                sum += result
                mass = result
            else:
                break
    return sum

lines = list(map(int, utils.read_input().strip().split('\n')))
print(part1(lines[:]))
print(part2(lines[:]))