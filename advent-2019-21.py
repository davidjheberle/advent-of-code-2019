import intcode
import utils

def run_springscript(program):
    ascii_image = []
    while True:
        ascii_int = program.run()
        if ascii_int is None:
            break
        if ascii_int > 127:  # ascii table size
            return ascii_int, ''
        ascii_image.append(chr(ascii_int))
    return -1, ''.join(ascii_image)


def load_springscript(program, script):
    ascii_chars = list(map(ord, list('\n'.join(script) + '\n')))
    while len(ascii_chars) > 0:
        program.run(ascii_chars)


def get_hull_damage(program, script):
    load_springscript(program, script)
    damage, ascii_images = run_springscript(program)
    if ascii_images:
        print(ascii_images)
    return damage


def part1(program):
    print("Part 1")
    # (!A or !B or !C) and D
    script = [
        'NOT A T',
        'NOT B J',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'WALK']
    return get_hull_damage(program, script)


def part2(program):
    print("Part 2")
    script = [
        # (!A or !B or !C) and D and (E or H)
        # Inferred experimentally by inspecting the failed scenarios
        'NOT A T',
        'NOT B J',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'NOT E T',
        'NOT T T',
        'OR H T',
        'AND T J',
        'RUN']
    return get_hull_damage(program, script)

raw_input = utils.read_input()
print(part1(intcode.Computer(raw_input)))
print(part2(intcode.Computer(raw_input)))