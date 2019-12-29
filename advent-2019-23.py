from collections import defaultdict, deque
import intcode
import utils

def part1(raw_input):
    print("Part 1")
    computers = []
    input_queues = defaultdict(deque)
    network_size = 50
    for i in range(network_size):
        input_queues[i].append(i)
        computers.append(intcode.Computer(raw_input))
    
    while True:
        for i in range(network_size):
            network_input = input_queues[i].popleft() if input_queues[i] else -1
            output = computers[i].cor.send(network_input)
            if output:
                tmp = next(computers[i].cor)
                input_queues[output].append(tmp)
                tmp = next(computers[i].cor)
                if output == 255:
                    return tmp
                input_queues[output].append(tmp)

def part2(program):
    print("Part 2")
    return None

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(intcode.Computer(raw_input)))