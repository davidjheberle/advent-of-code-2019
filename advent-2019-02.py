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
    program[1] = 12
    program[2] = 2
    intcode.run(program)
    return program[0]

def part2(raw_input):
    print("Part 2")
    original_program = intcode.get_program(raw_input)
    for noun in range(0, 100):
        for verb in range(0, 100):
            program = original_program.copy()
            program[1] = noun
            program[2] = verb
            intcode.run(program)
            if program[0] == 19690720:
                return 100 * noun + verb

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))