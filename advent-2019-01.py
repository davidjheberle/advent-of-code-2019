import getopt
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
    return mass // 3 - 2

def part1(masses):
    print("Part 1")
    sum = 0
    for mass in masses:
        sum += calc_fuel(mass)
    return sum

def part2(masses):
    print("Part 2")
    sum = 0
    for mass in masses:
        while True:
            result = calc_fuel(mass)
            if result > 0:
                sum += result
                mass = result
            else:
                break
    return sum

lines = list(map(int, read_input().strip().split('\n')))
print(part1(lines[:]))
print(part2(lines[:]))