import functools
import itertools
import math
import utils

class Body:
    def __init__(self, p, v):
        self.pos = p
        self.vel = v

    def __str__(self):
        spos = 'pos=<x={0}, y={1}, z={2}>'.format(*self.pos)
        svel = 'vel=<x={0}, y={1}, z={2}>'.format(*self.vel)
        return '{0}, {1}'.format(spos, svel)

def get_moons(raw_input):
    moons = []
    lines = raw_input.splitlines()
    for line in lines:
        pos = [int(x[2:]) for x in line.strip('<>').split(', ')]
        vel = [0, 0, 0]
        moons.append(Body(pos, vel))
    return moons

def apply_gravity(m1, m2):
    for axis in range(3):
        if m1.pos[axis] < m2.pos[axis]:
            m1.vel[axis] += 1
            m2.vel[axis] -= 1
        elif m1.pos[axis] > m2.pos[axis]:
            m1.vel[axis] -= 1
            m2.vel[axis] += 1

def update(moons):
    for i, j in itertools.combinations(range(len(moons)), 2):
        apply_gravity(moons[i], moons[j])
    for i in range(len(moons)):
        for j in range(3):
            moons[i].pos[j] += moons[i].vel[j]

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def part1(raw_input, steps):
    print("Part 1")
    moons, total = get_moons(raw_input), 0
    for _ in range(steps):
        update(moons)
    for m in moons:
        potential, kinetic = sum([abs(x) for x in m.pos]), sum([abs(x) for x in m.vel])
        total += potential * kinetic
    return total

'''
LCM works because each axis is cycling independently. Let's do a simple example:

3 series, each repeating at a different period. If the state is based on all 3 series, 
then how long until we see the same state again?

    0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
S1: 0 1 2 3 0 1 2 3 0 1 2 3 0 1 2 3 0
S2: 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
S3; 0 1 2 3 4 5 0 1 2 3 4 5 0 1 2 3 4
S1 has a period of 4, S2 of 2, S3 of 6. And the combined series has a period of 12, 
which is the LCM of 2, 4, and 6. You'll get pairwise repetitions earlier than that.

S1 and S2 have a combined period of 4. S2 and S3 have a combined period of 6. 
But S1 and S3 have a combined period of 12.

There's a more mathematically rigorous way to describe this, but the 
above illustrates what's happening.

Explanation by u/rabuf (https://www.reddit.com/user/rabuf/) 
'''
def part2(raw_input):
    print("Part 2")
    moons, steps = get_moons(raw_input), 0
    # Orbital periods: https://en.wikipedia.org/wiki/Orbital_period
    peroid = {}
    # Save starting values grouped by axis.
    start = [[(m.pos[axis], m.vel[axis]) for m in moons] for axis in range(3)]
    while len(peroid) < 3:
        steps += 1
        update(moons)

        for axis in range(3):
            # See if current (pos_axis, vel_axis) for all moons match their starting values:
            if axis not in peroid and start[axis] == [(m.pos[axis], m.vel[axis]) for m in moons]:
                peroid[axis] = steps
    return functools.reduce(lcm, peroid.values())

raw_input = utils.read_input()
print(part1(raw_input, 1000))
print(part2(raw_input))