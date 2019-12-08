import getopt, sys

def read_input():
    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:]
    unixOptions = "f:"
    gnuOptions = "file="

    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
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

def intcode(positions):
    param, ptr, skip = {}, 0, (4, 4)
    while positions[ptr] is not 99:
        for i in range(1, 4): param[i] = positions[ptr + i]
        opcode = positions[ptr] % 100
        if opcode is 1: positions[param[3]] = positions[param[1]] + positions[param[2]]
        elif opcode is 2: positions[param[3]] = positions[param[1]] * positions[param[2]]
        ptr += skip[opcode - 1]
    return positions

def part1(input):
    print("Input: %s" % input)
    positions = list(map(int, input.split(',')))
    positions[1] = 12
    positions[2] = 2
    return intcode(positions)[0]

def part2(input):
    print("Input: %s" % input)
    original_positions = list(map(int, input.split(',')))

    for noun in range(0, 100):
        for verb in range(0, 100):
            positions = original_positions.copy()
            positions[1] = noun
            positions[2] = verb
            positions = intcode(positions)
            if positions[0] == 19690720:
                return 100 * noun + verb

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))