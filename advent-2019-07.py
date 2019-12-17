import getopt
import intcode
import itertools
import sys

def read_input():
    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:]
    unixOptions = "f:"
    gnuOptions = "file="

    try:
        arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    fileName = None
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-f", "--file"):
            fileName = currentValue
            print("Reading %s" % fileName)

    file = open(fileName)
    raw_input = file.read()
    file.close()
    return raw_input

def part1(raw_input):
    print("Part 1")
    program = intcode.get_program(raw_input)
    phase_permutations = itertools.permutations(range(5), 5)
    outputs = []
    for phase_settings in phase_permutations:
        num_amplifiers = len(phase_settings)
        inputs, output = [], 0
        for i in range(num_amplifiers):
            inputs.append([phase_settings[i], output])
            output, _ = intcode.run(program.copy(), inputs[i])
        outputs.append(output)
        print((phase_settings, output))
    return max(outputs)

def part2(raw_input):
    print("Part 2")
    program = intcode.get_program(raw_input)
    phase_permutations = itertools.permutations(range(5, 10), 5)
    outputs = []
    for phase_settings in phase_permutations:
        programs, ptrs, inputs, output = [], [], [], 0
        num_amplifiers = len(phase_settings)
        for i in range(num_amplifiers):
            programs.append(program.copy())
            ptrs.append(0)
            inputs.append([phase_settings[i]])            
        while ptrs[0] is not None:
            for i in range(num_amplifiers):
                inputs[i].append(output)
                output, ptr = intcode.run(programs[i], inputs[i], ptrs[i])
                ptrs[i] = ptr
        print((phase_settings, inputs[0][0]))
        outputs.append(inputs[0][0])
    return max(outputs)

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))

