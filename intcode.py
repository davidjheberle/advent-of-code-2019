def get_program(raw_input):
    return list(map(int, raw_input.split(',')))

def get_params(program, ptr, num, rel_base):
    params = {}
    for i in range(1, num + 1):
        mode = get_memory(program, ptr) // int('100'.ljust(i + 2, '0')) % 10
        if mode == 0: params[i] = get_memory(program, ptr + i)
        elif mode == 1: params[i] = ptr + i
        elif mode == 2: params[i] = rel_base + get_memory(program, ptr + i)
    return params

def buffer_memory(program, index):
    if index >= len(program):
        buffer = [0] * (index + 1 - len(program))
        program.extend(buffer)

def get_memory(program, index):
    buffer_memory(program, index)
    return program[index]

def set_memory(program, index, value):
    buffer_memory(program, index)
    program[index] = value

def run(program, program_input=[], ptr=0, rel_base=0, input_function=None):
    if ptr is None: return None, None, None
    output, params, num_params = 0, {}, (3, 3, 1, 1, 2, 2, 3, 3, 1)
    while get_memory(program, ptr) != 99:
        opcode = get_memory(program, ptr) % 100
        params = get_params(program, ptr, num_params[opcode - 1], rel_base)
        if opcode == 1: set_memory(program, params[3], get_memory(program, params[1]) + get_memory(program, params[2]))
        elif opcode == 2: set_memory(program, params[3], get_memory(program, params[1]) * get_memory(program, params[2]))
        elif opcode == 3: set_memory(program, params[1], program_input.pop(0) if program_input else input_function())
        elif opcode == 4: output = get_memory(program, params[1])
        elif opcode == 5 and get_memory(program, params[1]) or opcode == 6 and not get_memory(program, params[1]): ptr = get_memory(program, params[2]) - 3
        elif opcode == 7: set_memory(program, params[3], 1 if get_memory(program, params[1]) < get_memory(program, params[2]) else 0)
        elif opcode == 8: set_memory(program, params[3], 1 if get_memory(program, params[1]) == get_memory(program, params[2]) else 0)
        elif opcode == 9: rel_base += get_memory(program, params[1])
        ptr += num_params[opcode - 1] + 1
        if opcode == 4: return output, ptr, rel_base
    return output, None, None