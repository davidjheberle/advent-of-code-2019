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

def check(raw_input, x, y):
    program = intcode.Computer(raw_input)
    return program.run([x, y])

def part1(raw_input):
    print("Part 1")
    return sum(check(raw_input, x, y) for x in range(50) for y in range(50))

def part2(raw_input):
    print("Part 2")
    x = box = 100
    for y in range(box, 99999):
        while not check(raw_input, x, y): x += 1
        if check(raw_input, x + box - 1, y - box + 1): break
    return x * 10000 + y - 99

raw_input = read_input()
print(part1(raw_input))
print(part2(raw_input))