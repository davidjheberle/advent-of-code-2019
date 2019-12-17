import getopt
import intcode
import os
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

def part1(program):
    print("Part 1")
    block_count = 0
    ptr, rel_base, inputs = 0, 0, []
    while ptr is not None:
        _, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base)
        _, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base)
        tile_id, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base)
        if tile_id == 2: block_count += 1
    return block_count

def part2(program):
    print("Part 2")
    ball_x = paddle_x = 0
    score = 0
    intcode.set_memory(program, 0, 2)
    ptr, rel_base, inputs = 0, 0, []
    joystick_input = lambda: (ball_x > paddle_x) - (ball_x < paddle_x)
    while ptr is not None:
        x, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base, joystick_input)
        y, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base, joystick_input)
        tile_id, ptr, rel_base = intcode.run(program, inputs, ptr, rel_base, joystick_input)
        if ptr is not None:
            paddle_x = x if tile_id == 3 else paddle_x
            ball_x = x if tile_id == 4 else ball_x
            score = tile_id if (x, y) == (-1, 0) else score
    return score

raw_input = read_input()
print(part1(intcode.get_program(raw_input)))
print(part2(intcode.get_program(raw_input)))