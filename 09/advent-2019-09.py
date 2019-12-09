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

def get_params(program, ptr, num, rel_base):
    params = {}
    for i in range(1, num + 1):
        mode = get_memory(program, ptr) // int('100'.ljust(i + 2, '0')) % 10
        if mode == 0: params[i] = get_memory(program, ptr + i)
        elif mode == 1: params[i] = ptr + i
        elif mode == 2: params[i] = rel_base + get_memory(program, ptr + i)
    return params

def buffer_memory(program, index):
    if index >= len(program):
        buffer = [0] * (index + 1 - len(program))
        program.extend(buffer)

def get_memory(program, index):
    buffer_memory(program, index)
    return program[index]

def set_memory(program, index, value):
    buffer_memory(program, index)
    program[index] = value

def intcode(program, program_input=[], ptr=0, rel_base=0):
    output, params, num_params = 0, {}, (3, 3, 1, 1, 2, 2, 3, 3, 1)
    while get_memory(program, ptr) != 99:
        opcode = get_memory(program, ptr) % 100
        params = get_params(program, ptr, num_params[opcode - 1], rel_base)
        if opcode == 1: set_memory(program, params[3], get_memory(program, params[1]) + get_memory(program, params[2]))
        elif opcode == 2: set_memory(program, params[3], get_memory(program, params[1]) * get_memory(program, params[2]))
        elif opcode == 3: set_memory(program, params[1], program_input.pop(0))
        elif opcode == 4: output = get_memory(program, params[1])
        elif opcode == 5 and get_memory(program, params[1]) or opcode == 6 and not get_memory(program, params[1]): ptr = get_memory(program, params[2]) - 3
        elif opcode == 7: set_memory(program, params[3], 1 if get_memory(program, params[1]) < get_memory(program, params[2]) else 0)
        elif opcode == 8: set_memory(program, params[3], 1 if get_memory(program, params[1]) == get_memory(program, params[2]) else 0)
        elif opcode == 9: rel_base += get_memory(program, params[1])
        ptr += num_params[opcode - 1] + 1
        if opcode == 4: return output, ptr, rel_base
    return output, None, None

def part1(raw_input):
    program = get_program(raw_input)
    ptr, rel_base, inputs = 0, 0, [1]
    while ptr is not None:
        output, ptr, rel_base = intcode(program, inputs, ptr, rel_base)
        print(("Output", output))
    return ("Part 1", output)

def part2(raw_input):
    program = get_program(raw_input)
    ptr, rel_base, inputs = 0, 0, [2]
    while ptr is not None:
        output, ptr, rel_base = intcode(program, inputs, ptr, rel_base)
        print(("Output", output))
    return ("Part 2", output)

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))

