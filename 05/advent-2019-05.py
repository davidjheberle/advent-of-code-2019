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
    param, ptr, skip = {}, 0, (4, 4, 2, 2, 3, 3, 4, 4)
    while positions[ptr] is not 99:
        opcode = positions[ptr] % 100
        for i in range(1, 4): param[i] = ptr + i if positions[ptr] // int('100'.ljust(i + 2, '0')) % 10 else positions[ptr + i]
        if opcode is 1: positions[param[3]] = positions[param[1]] + positions[param[2]]
        elif opcode is 2: positions[param[3]] = positions[param[1]] * positions[param[2]]
        elif opcode is 3: positions[param[1]] = int(input("Input an integer: "))
        elif opcode is 4: print(positions[param[1]])
        elif opcode is 5 and positions[param[1]] or opcode is 6 and not positions[param[1]]: ptr = positions[param[2]] - 3
        elif opcode is 7: positions[param[3]] = 1 if positions[param[1]] < positions[param[2]] else 0
        elif opcode is 8: positions[param[3]] = 1 if positions[param[1]] == positions[param[2]] else 0
        ptr += skip[opcode - 1]
    return positions

raw_input = read_input()
positions = list(map(int, input.split(',')))
intcode(positions)

