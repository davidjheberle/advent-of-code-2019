import getopt
import math
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

def calc_fuel(mass):
    result = math.floor(mass / 3) - 2
    return result

def part1(lines):
    print("Part 1")
    sum = 0
    for l in lines:
        sum += calc_fuel(int(l))
    return sum

def part2(lines):
    print("Part 2")
    sum = 0
    for l in lines:
        mass = int(l)
        while True:
            result = calc_fuel(mass)
            if result > 0:
                sum += result
                mass = result
            else:
                break
    return sum

raw_input = read_input()
print(part1(raw_input.strip().split('\n')))
print(part2(raw_input.strip().split('\n')))