import intcode
import utils

def run_springscript(computer):
    try:
        while output := next(computer.generator):
            if output and output < 256:
                print(chr(output), end='')
            else:
                print(output)
    except StopIteration:
        return output

def load_springscript(computer, script):
    computer.generator = computer.run()
    while output := next(computer.generator):
        print(chr(output), end='', sep='')
    print()
    
    for line in script:
        for letter in line:
            output = computer.generator.send(ord(letter))
            print(letter, end='')
            if output:
                print(chr(output))

def get_hull_damage(computer, script):
    load_springscript(computer, script)
    return run_springscript(computer)

def part1(computer):
    print("Part 1")
    # (!A or !B or !C) and D
    script = [
        'NOT A T\n',
        'NOT B J\n',
        'OR T J\n',
        'NOT C T\n',
        'OR T J\n',
        'AND D J\n',
        'WALK\n']
    get_hull_damage(computer, script)

def part2(computer):
    print("Part 2")
    # (!A or !B or !C) and D and (E or H)
    # Inferred experimentally by inspecting the failed scenarios
    script = [
        'NOT A J\n',
        'AND D J\n',
        'NOT B T\n',
        'AND D T\n',
        'OR T J\n',
        'NOT C T\n',
        'AND D T\n',
        'AND H T\n',
        'OR T J\n',
        'RUN\n'
    ]
    get_hull_damage(computer, script)

raw_input = utils.read_input()
part1(intcode.Computer(raw_input))
part2(intcode.Computer(raw_input))