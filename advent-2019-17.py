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

def is_intersection(grid, x, y, width, height):
    if x == 0 or y == 0 or x == width -1 or y == height - 1:
        return False
    return grid[(x - 1, y)] == ord('#') and grid[(x + 1, y)] == ord('#') \
        and grid[(x, y - 1)] == ord('#') and grid[(x, y + 1)] == ord('#')

def is_grid_char(num):
    chars = set('#.^v<>')
    return str(chr(num)) in chars or num == 10

def get_grid(program):
    grid = {}
    x, y, width, height = 0, 0, 0, 0
    ptr, rel_base, inputs = 0, 0, []
    output, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base)
    while ptr is not None:
        if not is_grid_char(output):
            break
        if output == 10:
            y += 1
            width = max(width, x)
            x = 0
        else:
            grid[(x, y)] = output
            x += 1
        output, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base)
    height = y - 1
    return grid, width, height

def get_alignment_param_sum(grid, width, height):
    alignment_param_sum = 0
    for y in range(0, height):
        for x in range(0, width):
            if grid[(x, y)] == 35 and is_intersection(grid, x, y, width, height):
                alignment_param_sum += x * y
    return alignment_param_sum

def serialize_grid(grid, width, height):
    return '\n'.join([''.join(map(chr, [grid[(x, y)] for x in range(0, width)])) for y in range(0, height)])

def part1(program):
    print("Part 1")
    grid, width, height = get_grid(program)
    return get_alignment_param_sum(grid, width, height)

def string_to_ascii_list(string):
    return list(map(ord, list(string)))

def get_collected_dust(program):
    input_routine = string_to_ascii_list('A,A,B,C,B,C,B,C,C,A\n'
                                         'R,8,L,4,R,4,R,10,R,8\n'
                                         'L,12,L,12,R,8,R,8\n'
                                         'R,10,R,4,R,4\n'
                                         'n\n')
    ptr, rel_base, outputs = 0, 0, []
    while ptr is not None:
        output, ptr, rel_base = intcode.run(program, input_routine, ptr, rel_base)
        if ptr is not None: outputs.append(output)
    return outputs[-1]

def part2(program):
    print("Part 2")
    intcode.set_memory(program, 0, 2)
    grid, width, height = get_grid(program[:])
    print(serialize_grid(grid, width, height))
    return get_collected_dust(program)

program = intcode.get_program(read_input())
print(part1(program[:]))
print(part2(program[:]))