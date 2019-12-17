import getopt
import intcode
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
    ptr, rel_base, inputs, outputs = 0, 0, [1], []
    while ptr is not None:
        output, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base)
        outputs.append(output)
    return outputs[0]

def part2(raw_input):
    print("Part 2")
    program = intcode.get_program(raw_input)
    ptr, rel_base, inputs, outputs = 0, 0, [2], []
    while ptr is not None:
        output, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base)
        outputs.append(output)
    return outputs[0]

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))
