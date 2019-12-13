import getopt, sys
import os

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

def intcode(program, program_input=[], ptr=0, rel_base=0, input_function=None):
    if ptr is None: return None, None, None
    output, params, num_params = 0, {}, (3, 3, 1, 1, 2, 2, 3, 3, 1)
    while get_memory(program, ptr) != 99:
        opcode = get_memory(program, ptr) % 100
        params = get_params(program, ptr, num_params[opcode - 1], rel_base)
        if opcode == 1: set_memory(program, params[3], get_memory(program, params[1]) + get_memory(program, params[2]))
        elif opcode == 2: set_memory(program, params[3], get_memory(program, params[1]) * get_memory(program, params[2]))
        elif opcode == 3: set_memory(program, params[1], program_input.pop(0) if program_input else input_function())
        elif opcode == 4: output = get_memory(program, params[1])
        elif opcode == 5 and get_memory(program, params[1]) or opcode == 6 and not get_memory(program, params[1]): ptr = get_memory(program, params[2]) - 3
        elif opcode == 7: set_memory(program, params[3], 1 if get_memory(program, params[1]) < get_memory(program, params[2]) else 0)
        elif opcode == 8: set_memory(program, params[3], 1 if get_memory(program, params[1]) == get_memory(program, params[2]) else 0)
        elif opcode == 9: rel_base += get_memory(program, params[1])
        ptr += num_params[opcode - 1] + 1
        if opcode == 4: return output, ptr, rel_base
    return output, None, None

def part1(program):
    print("Part 1")
    block_count = 0
    ptr, rel_base, inputs = 0, 0, []
    while ptr is not None:
        _, ptr, rel_base = intcode(program, inputs, ptr, rel_base)
        _, ptr, rel_base = intcode(program, inputs, ptr, rel_base)
        tile_id, ptr, rel_base = intcode(program, inputs, ptr, rel_base)
        if tile_id == 2: block_count += 1
    return block_count

def part2(program):
    print("Part 2")
    ball_x = paddle_x = 0
    score = 0
    set_memory(program, 0, 2)
    ptr, rel_base, inputs = 0, 0, []
    joystick_input = lambda: (ball_x > paddle_x) - (ball_x < paddle_x)
    while ptr is not None:
        x, ptr, rel_base = intcode(program, inputs, ptr, rel_base, joystick_input)
        y, ptr, rel_base = intcode(program, inputs, ptr, rel_base, joystick_input)
        tile_id, ptr, rel_base = intcode(program, inputs, ptr, rel_base, joystick_input)
        if ptr is not None:
            paddle_x = x if tile_id == 3 else paddle_x
            ball_x = x if tile_id == 4 else ball_x
            score = tile_id if (x, y) == (-1, 0) else score
    return score

raw_input = read_input()
print(part1(get_program(raw_input)))
print(part2(get_program(raw_input)))