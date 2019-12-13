import getopt, sys

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

def get_program(raw_input):
    return list(map(int, raw_input.split(',')))

def get_params(program, ptr, num):
    params = {}
    for i in range(1, num + 1):
        params[i] = program[ptr + i]
    return params

def intcode(program, program_input=[], ptr=0):
    output, params, num_params = 0, {}, (3, 3)
    while program[ptr] != 99:
        opcode = program[ptr] % 100
        params = get_params(program, ptr, num_params[opcode - 1])
        if opcode == 1: program[params[3]] = program[params[1]] + program[params[2]]
        elif opcode == 2: program[params[3]] = program[params[1]] * program[params[2]]
        ptr += num_params[opcode - 1] + 1
    return output

def part1(raw_input):
    print("Part 1")
    program = get_program(raw_input)
    program[1] = 12
    program[2] = 2
    intcode(program)
    return program[0]

def part2(raw_input):
    print("Part 2")
    original_program = get_program(raw_input)
    for noun in range(0, 100):
        for verb in range(0, 100):
            program = original_program.copy()
            program[1] = noun
            program[2] = verb
            intcode(program)
            if program[0] == 19690720:
                return 100 * noun + verb

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))