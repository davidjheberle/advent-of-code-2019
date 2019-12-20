import intcode
import utils

def part1(raw_input):
    print("Part 1")
    program = intcode.Computer(raw_input)
    outputs, output = [], 0
    while output is not None:
        output = program.run([1])
        if output is not None: outputs.append(output)
    return outputs[0]

def part2(raw_input):
    print("Part 2")
    program = intcode.Computer(raw_input)
    outputs, output = [], 0
    while output is not None:
        output = program.run([2])
        if output is not None: outputs.append(output)
    return outputs[0]

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))

