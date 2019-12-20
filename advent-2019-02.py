import intcode
import utils

def part1(raw_input):
    print("Part 1")
    program = intcode.Computer(raw_input)
    program.set_memory(1, 12)
    program.set_memory(2, 2)
    program.run()
    return program.get_memory(0)

def part2(raw_input):
    print("Part 2")
    for noun in range(0, 100):
        for verb in range(0, 100):
            program = intcode.Computer(raw_input)
            program.set_memory(1, noun)
            program.set_memory(2, verb)
            program.run()
            if program.get_memory(0) == 19690720:
                return 100 * noun + verb

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))