import intcode
import utils

def part1(raw_input):
    print("Part 1")
    computer = intcode.Computer(raw_input)
    computer.set_memory(1, 12)
    computer.set_memory(2, 2)
    computer.generator = computer.run()
    for _ in computer.generator:
        pass
    return computer.get_memory(0)

def part2(raw_input):
    print("Part 2")
    for noun in range(0, 100):
        for verb in range(0, 100):
            computer = intcode.Computer(raw_input)
            computer.set_memory(1, noun)
            computer.set_memory(2, verb)
            computer.generator = computer.run()
            for _ in computer.generator:
                pass
            if computer.get_memory(0) == 19690720:
                return 100 * noun + verb

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))