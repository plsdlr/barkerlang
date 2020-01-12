class memory:

    def __init__(self,number_of_cells,instructions):
        self.memory_register = []
        self.init_instructions = instructions
        for i in range(0, number_of_cells):
            self.memory_register.append("0")
        self.load_instructions()

    def load_instructions(self):
        for counter, i in enumerate(self.init_instructions):
            self.memory_register[counter]= i

    def read_register(self, number):
        cell = self.memory_register[number]
        return cell

    def write_register(self, adress, newvalue):
        self.memory_register[adress] = newvalue
        #self.logger.info("----MEMORY STATE: %s", self.memory_array)


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def full(self):
        return self.items


class instruction_pointer(memory):

    def __init__(self,instructions, mem_size):
        memory.__init__(self, mem_size, instructions)
        self.instruction_pointer_position = 0
        #self.interpreter_ref = new_interp

    def get_instruction(self):
        new_instruction = self.read_register(self.instruction_pointer_position)
        self.instruction_pointer_position = self.instruction_pointer_position + 1
        return new_instruction

    def set_instruction_pointer(self,number):
        self.instruction_pointer_position = number

    def skip_instruction(self):
        self.instruction_pointer_position = self.instruction_pointer_position + 1
