import utils

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

def part1(raw_input):
    print("Part 1")
    orbit_map = map_orbits(raw_input.strip().split('\n'))
    count = 0
    for orbit in orbit_map.keys():
        body = orbit
        while body != 'COM':
            body = orbit_map[body]
            count += 1
    return count

def part2(raw_input):
    print("Part 2")
    orbit_map = map_orbits(raw_input.strip().split('\n'))
    orbit_you = get_orbit('YOU', orbit_map)
    orbit_san = get_orbit('SAN', orbit_map)
    orbit_common = intersection(orbit_you, orbit_san)
    return len(orbit_you) + len(orbit_san) - 2 * len(orbit_common)

raw_input = utils.read_input() 
print(part1(raw_input))
print(part2(raw_input))

