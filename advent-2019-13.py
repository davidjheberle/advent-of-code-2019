import intcode
import os
import utils

def part1(program):
    print("Part 1")
    block_count = 0
    inputs, tile_id = [], 0
    while tile_id is not None:
        program.run(inputs)
        program.run(inputs)
        tile_id = program.run(inputs)
        if tile_id == 2: block_count += 1
    return block_count

def part2(program):
    print("Part 2")
    ball_x = paddle_x = 0
    score = 0
    program.set_memory(0, 2)
    inputs, tile_id = [], 0
    joystick_input = lambda: (ball_x > paddle_x) - (ball_x < paddle_x)
    while tile_id is not None:
        x = program.run(inputs, joystick_input)
        y = program.run(inputs, joystick_input)
        tile_id = program.run(inputs, joystick_input)
        if tile_id is not None:
            paddle_x = x if tile_id == 3 else paddle_x
            ball_x = x if tile_id == 4 else ball_x
            score = tile_id if (x, y) == (-1, 0) else score
    return score

raw_input = utils.read_input()
print(part1(intcode.Computer(raw_input)))
print(part2(intcode.Computer(raw_input)))