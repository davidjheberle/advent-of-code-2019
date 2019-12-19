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
    program = intcode.Computer(raw_input)
    outputs, output = [], 0
    while output is not None:
        output = program.run([1])
        if output is not None: outputs.append(output)
    return outputs[-1]

def part2(raw_input):
    print("Part 2")
    program = intcode.Computer(raw_input)
    return program.run([5])

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))

