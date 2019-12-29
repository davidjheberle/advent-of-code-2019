class Computer:

    def __init__(self, raw_input):
        self.program = self.get_program(raw_input)
        self.ptr = 0
        self.rel_base = 0
        self.cor = self.run()
        self.first_val = self.cor.send(None)

    def get_program(self, raw_input):
        return list(map(int, raw_input.split(',')))

    def get_params(self, index, num):
        params = {}
        for i in range(1, num + 1):
            mode = self.get_memory(index) // int('100'.ljust(i + 2, '0')) % 10
            if mode == 0: params[i] = self.get_memory(index + i)
            elif mode == 1: params[i] = index + i
            elif mode == 2: params[i] = self.rel_base + self.get_memory(index + i)
        return params

    def buffer_memory(self, index):
        if index >= len(self.program):
            buffer = [0] * (index + 1 - len(self.program))
            self.program.extend(buffer)

    def get_memory(self, index):
        self.buffer_memory(index)
        return self.program[index]

    def set_memory(self, index, value):
        self.buffer_memory(index)
        self.program[index] = value

    def run(self, program_input=[], input_function=None):
        # if self.ptr is None: return None
        params, num_params = {}, (3, 3, 1, 1, 2, 2, 3, 3, 1)
        while self.get_memory(self.ptr) != 99:
            opcode = self.get_memory(self.ptr) % 100
            params = self.get_params(self.ptr, num_params[opcode - 1])
            if opcode == 1: self.set_memory(params[3], self.get_memory(params[1]) + self.get_memory(params[2]))
            elif opcode == 2: self.set_memory(params[3], self.get_memory(params[1]) * self.get_memory(params[2]))
            elif opcode == 3:
                tmp = yield
                # self.set_memory(params[1], program_input.pop(0) if program_input else input_function())
                self.set_memory(params[1], tmp)
            elif opcode == 4: yield self.get_memory(params[1])
            elif opcode == 5 and self.get_memory(params[1]) or opcode == 6 and not self.get_memory(params[1]): self.ptr = self.get_memory(params[2]) - 3
            elif opcode == 7: self.set_memory(params[3], 1 if self.get_memory(params[1]) < self.get_memory(params[2]) else 0)
            elif opcode == 8: self.set_memory(params[3], 1 if self.get_memory(params[1]) == self.get_memory(params[2]) else 0)
            elif opcode == 9: self.rel_base += self.get_memory(params[1])
            self.ptr += num_params[opcode - 1] + 1