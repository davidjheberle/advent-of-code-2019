from collections import deque
import intcode
import utils

def part1(raw_input):
    print("Part 1")
    computer = intcode.Computer(raw_input)
    computer.generator = computer.run()
    print(chr(computer.generator.send(None)), end='', sep='')
    commands = deque([
        'west', 'take mug', 'north', 'take easter egg', 'south', 'east',
        'south', 'east', 'north', 'take candy cane', 'south', 'west', 'north',
        'east', 'take coin', 'north', 'north', 'take hypercube', 'south',
        'east', 'take manifold', 'west', 'south', 'south', 'east',
        'take pointer', 'west', 'west', 'take astrolabe', 'north', 'east',
        'north', 'drop manifold', 'drop easter egg', 'drop pointer',
        'drop candy cane', 'east'])
        
    while True:
        text = []
        try:
            while output := next(computer.generator):
                text.append(chr(output))
        except StopIteration:
            pass
        print(''.join(text))
        command = commands.popleft() if commands else input()
        if command == 'exit': return
        for c in command:
            output = computer.generator.send(ord(c))
            if output: print(chr(output), end='')
        computer.generator.send(ord('\n'))

def part2(raw_input):
    print("Part 2")
    return "Happy Holidays!"

raw_input = utils.read_input()
part1(raw_input)
print(part2(raw_input))