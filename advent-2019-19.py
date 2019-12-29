import intcode
import utils

def check(raw_input, x, y):
    computer = intcode.Computer(raw_input)
    computer.generator = computer.run()
    computer.generator.send(None)
    computer.generator.send(x)
    return computer.generator.send(y)

def part1(raw_input):
    print("Part 1")
    return sum(check(raw_input, x, y) for x in range(50) for y in range(50))

def part2(raw_input):
    print("Part 2")
    x = box = 100
    for y in range(box, 99999):
        while not check(raw_input, x, y): x += 1
        if check(raw_input, x + box - 1, y - box + 1): break
    return x * 10000 + y - 99

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))