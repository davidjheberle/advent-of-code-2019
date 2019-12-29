import intcode
import os
import utils

def part1(computer):
    print("Part 1")
    block_count = 0
    tile_id = 0
    computer.generator = computer.run()
    while True:
        try:
            next(computer.generator)
            next(computer.generator)
            tile_id = next(computer.generator)
            if tile_id == 2: block_count += 1
        except StopIteration:
            break
    return block_count

def part2(computer):
    print("Part 2")
    ball_x = paddle_x = score = tile_id = 0
    joystick_input = lambda: (ball_x > paddle_x) - (ball_x < paddle_x)
    computer.set_memory(0, 2)
    computer.generator = computer.run(joystick_input)
    while True:
        try:
            x = next(computer.generator)
            y = next(computer.generator)
            tile_id = next(computer.generator)
            if tile_id:
                paddle_x = x if tile_id == 3 else paddle_x
                ball_x = x if tile_id == 4 else ball_x
                score = tile_id if (x, y) == (-1, 0) else score
        except StopIteration:
            break
    return score

raw_input = utils.read_input()
print(part1(intcode.Computer(raw_input)))
print(part2(intcode.Computer(raw_input)))