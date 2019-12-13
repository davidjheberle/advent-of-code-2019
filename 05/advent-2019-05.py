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
        params[i] = ptr + i if program[ptr] // int('100'.ljust(i + 2, '0')) % 10 else program[ptr + i]
    return params

def intcode(program, program_input=[], ptr=0):
    output, params, num_params = 0, {}, (3, 3, 1, 1, 2, 2, 3, 3)
    while program[ptr] != 99:
        opcode = program[ptr] % 100
        params = get_params(program, ptr, num_params[opcode - 1])
        if opcode == 1: program[params[3]] = program[params[1]] + program[params[2]]
        elif opcode == 2: program[params[3]] = program[params[1]] * program[params[2]]
        elif opcode == 3: program[params[1]] = program_input.pop(0)
        elif opcode == 4: output = program[params[1]]
        elif opcode == 5 and program[params[1]] or opcode == 6 and not program[params[1]]: ptr = program[params[2]] - 3
        elif opcode == 7: program[params[3]] = 1 if program[params[1]] < program[params[2]] else 0
        elif opcode == 8: program[params[3]] = 1 if program[params[1]] == program[params[2]] else 0
        ptr += num_params[opcode - 1] + 1
        if opcode == 4: return output, ptr
    return output, None

def part1(raw_input):
    print("Part 1")
    program = get_program(raw_input)
    program_input, ptr, output, last_output = [1], 0, None, None
    while ptr is not None:
        last_output = output
        output, ptr = intcode(program, program_input, ptr)
        print((output, ptr))
    return last_output

def part2(raw_input):
    print("Part 2")
    program = get_program(raw_input)
    return intcode(program, [5])[0]

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))

