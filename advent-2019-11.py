import intcode
import utils

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

def hull_painting_robot(computer, start_color):
    canvas, position, directions, direction_index = {}, (0, 0), [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
    canvas[position] = start_color
    computer.generator = computer.run()
    computer.generator.send(None)
    while True:
        try:
            color = computer.generator.send(read_panel(position, canvas))
            paint_panel(color, position, canvas)
            direction = next(computer.generator)
            next(computer.generator)
            direction_index, _ = turn(direction, direction_index, directions)
            position = (position[0] + directions[direction_index][0], position[1] + directions[direction_index][1])
        except StopIteration:
            break
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
    canvas = hull_painting_robot(intcode.Computer(raw_input), '.')
    return len(canvas)

def part2(raw_input):
    print("Part 2")
    canvas = hull_painting_robot(intcode.Computer(raw_input), '#')
    return print_canvas(canvas)

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))