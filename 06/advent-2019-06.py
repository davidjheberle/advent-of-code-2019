import getopt, sys

def read_input():
    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:]
    unixOptions = "f:"
    gnuOptions = "file="

    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
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

def intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]

def map_orbits(orbits):
    map = {}
    for o in orbits:
        bodies = o.split(')')
        map[bodies[1]] = bodies[0]
    return map

def get_orbit(body, orbit_map):
    orbit = []
    while body != 'COM':
        body = orbit_map[body]
        orbit.append(body)
    return orbit

def part1(input):
    orbit_map = map_orbits(raw_input.strip().split('\n'))
    count = 0
    for orbit in orbit_map.keys():
        body = orbit
        while body != 'COM':
            body = orbit_map[body]
            count += 1
    return count

def part2(input):
    orbit_map = map_orbits(raw_input.strip().split('\n'))
    orbit_you = get_orbit('YOU', orbit_map)
    orbit_san = get_orbit('SAN', orbit_map)
    orbit_common = intersection(orbit_you, orbit_san)
    return len(orbit_you) + len(orbit_san) - 2 * len(orbit_common)

raw_input = read_input() 
print(part1(raw_input))
print(part2(raw_input))

