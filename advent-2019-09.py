import intcode
import utils

def part1(raw_input):
    print("Part 1")
    computer = intcode.Computer(raw_input)
    computer.generator = computer.run()
    computer.generator.send(None)
    return computer.generator.send(1)

def part2(raw_input):
    print("Part 2")
    computer = intcode.Computer(raw_input)
    computer.generator = computer.run()
    computer.generator.send(None)
    return computer.generator.send(2)

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))

