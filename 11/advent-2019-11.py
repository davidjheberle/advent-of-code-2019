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

def read_panel(position, canvas):
    if position in canvas.keys():
        if canvas[position] == '#': return 1
        elif canvas[position] == '.': return 0
    return 0

def paint_panel(instruction, position, canvas):
    paints = ('.', '#')
    canvas[position] = paints[instruction]

def turn(input, index, directions):
    if input == 0:
        index -= 1
    elif input == 1:
        index += 1
    if index < 0:
        index = len(directions) - 1
    elif index > len(directions) - 1:
        index = 0
    return index, directions[index]

def hull_painting_robot(program, start_color):
    canvas, position, directions, direction_index = {}, (0, 0), [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
    canvas[position] = start_color
    ptr, rel_base, inputs, = 0, 0, []
    while ptr is not None:
        inputs.append(read_panel(position, canvas))
        output, ptr, rel_base = intcode(program, inputs, ptr, rel_base)
        paint_panel(output, position, canvas)
        if ptr is None: break
        output, ptr, rel_base = intcode(program, inputs, ptr, rel_base)
        direction_index, _ = turn(output, direction_index, directions)
        position = (position[0] + directions[direction_index][0], position[1] + directions[direction_index][1])
    return canvas

def print_canvas(canvas):
    canvas_array = []
    x_min, x_max, y_min, y_max = None, None, None, None
    for key in canvas:
        if x_min is None: x_min = key[0]
        elif key[0] < x_min: x_min = key[0]
        if x_max is None: x_max = key[0]
        elif key[0] > x_max: x_max = key[0]
        if y_min is None: y_min = key[1]
        elif key[1] < y_min: y_min = key[1]
        if y_max is None: y_max = key[1]
        elif key[1] > y_max: y_max = key[1]
    start = (x_min, y_min)
    x_length = x_max - x_min + 1
    y_length = y_max - y_min + 1
    for _ in range(y_length):
        canvas_array.append(['.'] * x_length)
    for key in canvas:
        canvas_array[key[1]-start[1]][key[0]-start[0]] = canvas[key]
    final_string = ''
    for y in range(y_length):
        for x in range(x_length):
            final_string += canvas_array[y_length-y-1][x]
        final_string += '\n'
    return final_string

def part1(raw_input):
    print("Part 1")
    canvas = hull_painting_robot(get_program(raw_input), '.')
    return len(canvas)

def part2(raw_input):
    print("Part 2")
    canvas = hull_painting_robot(get_program(raw_input), '#')
    return print_canvas(canvas)

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))