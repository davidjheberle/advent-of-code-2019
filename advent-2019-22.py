import functools
import utils

def deal_inc(deck, n):
    new_deck = [-1] * len(deck)
    i = 0
    while len(deck):
        new_deck[i % len(new_deck)] = deck.pop(0)
        i += n
    return new_deck

def modular_comp(shuffle_sequence, m, n, card = None, pos = None):
    a, b = 1, 0
    for shuffle_cmd in shuffle_sequence:
        a, b = shuffle_cmd(m, a, b)
    r = (b * pow(1 - a, m - 2, m)) % m
    if card:
        calc_pos = ((card - r) * pow(a, n, m) + r) % m
    if pos:
        calc_card = ((pos - r) * pow(a, n * (m - 2), m) + r) % m
    return (calc_card if pos else card, calc_pos if card else pos)

def part1(shuffles):
    print("Part 1")
    deck = list(range(10007))
    cmds = {
        'deal with increment ': deal_inc,
        'deal into new stack': (lambda x: x[::-1]),
        'cut ': (lambda x, n: x[n:] + x[:n])
    }

    for s in shuffles:
        for cmd, fn in cmds.items():
            if s.startswith(cmd):
                if cmd[-1] == ' ':
                    arg = int(s[len(cmd):])
                    deck = fn(deck, arg)
                else:
                    deck = fn(deck)
                break
    return deck.index(2019)

def part2(shuffles):
    print("Part 2")
    cmds = {
        'deal with increment ': lambda x, m, a, b: (a * x % m, b * x % m),
        'deal into new stack': lambda _, m, a, b: (-a % m, (m - 1 - b) % m),
        'cut ': lambda x, m, a, b: (a, (b - x) % m)
    }
    shuffle_sequence = []
    for s in shuffles:
        for cmd, fn in cmds.items():
            if (s.startswith(cmd)):
                arg = int(s[len(cmd):]) if cmd[-1] == ' ' else 0
                shuffle_sequence += [functools.partial(fn, arg)]
                break
    card, pos = modular_comp(shuffle_sequence, m = 119315717514047, n = 101741582076661, pos = 2020)
    return card, pos

raw_input = utils.read_input()
shuffles = [s for s in raw_input.strip().split('\n')]
print(part1(shuffles))
print(part2(shuffles))