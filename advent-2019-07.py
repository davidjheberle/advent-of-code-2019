import intcode
import itertools
import utils

def part1(raw_input):
    print("Part 1")
    maximum = float('-inf')
    phase_permutations = itertools.permutations(range(5), 5)
    for phase_settings in phase_permutations:
        num_amplifiers = len(phase_settings)
        output = 0
        for i in range(num_amplifiers):
            computer = intcode.Computer(raw_input)
            computer.generator = computer.run()
            computer.generator.send(None)
            computer.generator.send(phase_settings[i])
            output = computer.generator.send(output)
        maximum = max(maximum, output)
    return maximum

def part2(raw_input):
    print("Part 2")
    maximum = float('-inf')
    phase_permutations = itertools.permutations(range(5, 10), 5)
    for phase_settings in phase_permutations:
        computers = []
        num_amplifiers = len(phase_settings)
        outputs = [0] * num_amplifiers
        for i in range(num_amplifiers):
            computers.append(intcode.Computer(raw_input))
            computers[i].generator = computers[i].run()
            computers[i].generator.send(None)
            computers[i].generator.send(phase_settings[i])
        flag = True
        while flag:
            for i in range(num_amplifiers):
                try:
                    outputs[i] = computers[i].generator.send(outputs[(i - 1) % 5])
                    next(computers[i].generator)
                except StopIteration:
                    flag = False
                    continue
        maximum = max(maximum, outputs[-1])
    return maximum

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))

