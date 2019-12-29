import intcode
import utils

def is_intersection(grid, x, y, width, height):
    if x == 0 or y == 0 or x == width -1 or y == height - 1:
        return False
    return grid[(x - 1, y)] == ord('#') and grid[(x + 1, y)] == ord('#') \
        and grid[(x, y - 1)] == ord('#') and grid[(x, y + 1)] == ord('#')

def get_grid(computer):
    grid, output = {}, 0
    x, y, width, height = 0, 0, 0, 0
    while output := next(computer.generator):
        if output == 10:
            y += 1
            width = max(width, x)
            if x == 0: break
            x = 0
        else:
            grid[(x, y)] = output
            x += 1
    height = y - 1
    return grid, width, height

def get_alignment_param_sum(grid, width, height):
    alignment_param_sum = 0
    for y in range(0, height):
        for x in range(0, width):
            if grid[(x, y)] == 35 and is_intersection(grid, x, y, width, height):
                alignment_param_sum += x * y
    return alignment_param_sum

def part1(computer):
    print("Part 1")
    computer.generator = computer.run()
    grid, width, height = get_grid(computer)
    return get_alignment_param_sum(grid, width, height)

def get_collected_dust(computer):
    program = [
        'A,A,B,C,B,C,B,C,C,A\n',
        'R,8,L,4,R,4,R,10,R,8\n',
        'L,12,L,12,R,8,R,8\n',
        'R,10,R,4,R,4\n',
        'n\n'
    ]

    while output := next(computer.generator):
        print(chr(output), end='', sep='')
    
    for line in program:
        for instruction in line:
            output = computer.generator.send(ord(instruction))
            print(instruction, end='')
            if output: print(chr(output), end='')
        while output := next(computer.generator):
            if output and chr(output).isascii():
                print(chr(output), end='')
            else:
                return output

def part2(computer):
    print("Part 2")
    computer.set_memory(0, 2)
    computer.generator = computer.run()
    return get_collected_dust(computer)

raw_input = utils.read_input()
print(part1(intcode.Computer(raw_input)))
print(part2(intcode.Computer(raw_input)))