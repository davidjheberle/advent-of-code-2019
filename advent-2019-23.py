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
        computers[i].generator = computers[i].run()
        computers[i].generator.send(None)
    
    while True:
        for i in range(network_size):
            network_input = input_queues[i].popleft() if input_queues[i] else -1
            output = computers[i].generator.send(network_input)
            if output:
                x = next(computers[i].generator)
                y = next(computers[i].generator)
                input_queues[output].append(x)
                input_queues[output].append(y)
                if output == 255: return y

def part2(raw_input):
    print("Part 2")
    computers = []
    input_queues = defaultdict(deque)
    network_size = 50
    nat = None, None
    last_nat_y = None
    
    for i in range(network_size):
        input_queues[i].append(i)
        computers.append(intcode.Computer(raw_input))
        computers[i].generator = computers[i].run()
        computers[i].generator.send(None)
    
    network_idle = False
    while True:
        if network_idle:
            x, y = nat
            if y == last_nat_y: return y
            input_queues[0].append(x)
            input_queues[0].append(y)
            last_nat_y = y

        network_idle = True
        for i in range(network_size):            
            network_input = input_queues[i].popleft() if input_queues[i] else -1
            output = computers[i].generator.send(network_input)
            if network_input != -1: network_idle = False
            while output != None:
                address = output
                x = next(computers[i].generator)
                y = next(computers[i].generator)
                output = next(computers[i].generator)
                if address == 255:
                    nat = x, y
                else:
                    input_queues[address].append(x)
                    input_queues[address].append(y)

raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))