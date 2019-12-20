import utils

def parse_layer(encoded_list, width, height):
    layer = []
    for h in range(height):
        layer.append([])
        for _ in range(width):
            value = encoded_list.pop(0)
            layer[h].append(value)
    return layer
    
def get_layer_count(layer, count_value):
    count = 0
    for row in layer:
        count += row.count(count_value)
    return count

def part1(raw_input):
    print("Part 1")
    encoded_list = list(map(int, raw_input.strip()))
    layers, min_zero, min_layer = [], None, None
    while len(encoded_list) > 0:
        layers.append(parse_layer(encoded_list, 25, 6))
    for layer in layers:
        zero_count = get_layer_count(layer, 0)
        if min_zero is None or zero_count < min_zero:
            min_layer = layer
            min_zero = zero_count
    get_layer_count(min_layer, 0)
    return get_layer_count(min_layer, 1) * get_layer_count(min_layer, 2)

def part2(raw_input):
    print("Part 2")
    encoded_list = list(map(int, raw_input.strip()))
    layers = []
    while len(encoded_list) > 0:
        layers.append(parse_layer(encoded_list, 25, 6))
    result = ""
    for h in range(6):
        for w in range(25):
            pixel = 2
            for layer in layers:
                pixel = layer[h][w]
                if pixel != 2: break
            if pixel == 0:
                result = result + ' '
            else:
                result = result + str(pixel)
        result = result + '\n'
    return result


raw_input = utils.read_input()
print(part1(raw_input))
print(part2(raw_input))

