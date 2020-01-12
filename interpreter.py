import logging

module_logger = logging.getLogger('barkerlang.interpreter')

class interpreter:


    def __init__(self, parser_ref, _stack_ref, encoder_ref, instruction_pointer_ref):
        self.parser_ref = parser_ref
        self.logger = logging.getLogger('barkerlang.interpreter.interpreter')
        self.stack_ref = _stack_ref
        self.instruction_pointer_ref = instruction_pointer_ref
        self.register = 0
        self.encoder_ref = encoder_ref
        self.mnemonic_codes = {
            "(": self.XENOTATION,
            "+": self.XENOTATION,
            "-": self.XENOTATION,
            ":": self.XENOTATION,
            "Y": self.MERGE,
            "∆": self.STACK2REG,
            "^": self.MEM2STACK,
            "V": self.STACK2MEM,
            "v": self.REG2STACK,
            "∞": self.GOTO,
            ">": self.BOOL_H,
            "<": self.BOOL_L,
            "*": self.OUT,
            "0": self.HALT
        }


    def evaluate(self):
        _string = self.instruction_pointer_ref.get_instruction()
        print("--------------------------------->")
        print(_string)

        mnemonic_code = str(_string[:1])
        self.logger.info("Evaluate Instruction: %s",mnemonic_code)
        self.mnemonic_codes[mnemonic_code](_string)
        # except:
        #     print("NEED FIX->Exit Programm")
        #     quit()



    def XENOTATION(self,_string):
        self.logger.info("mnemonic: XENOTATION")
        xenotation = self.parser_ref._xeno_parser(_string,0)
        self.stack_ref.push(xenotation)
        #print(self.stack_ref.full())


    def MERGE(self,_string):
        self.logger.info("mnemonic: MERGE")
        peak = self.stack_ref.pop()
        below = self.stack_ref.pop()
        if peak['datatype'] == 'XENOTATIONS' and below['datatype'] == 'XENOTATIONS':
            new_xenotation_value = peak['value'] + below['value']
            new_xenotation = self.encoder_ref.encode(new_xenotation_value)
            self.stack_ref.push(new_xenotation)
        else:
            pass
        print(self.stack_ref.full())


    def STACK2REG(self,_string):
        peak = self.stack_ref.pop()
        self.register = peak["value"]

    def REG2STACK(self,_string):
        new_xenotation = self.encoder_ref.encode(self.register)
        self.stack_ref.push(new_xenotation)


    def MEM2STACK(self,_string):
        register = self.register
        data = self.instruction_pointer_ref.read_register(register)

        new_instructions = self.parser_ref._xeno_parser(str(data),0)
        self.stack_ref.push(new_instructions) ### this needs to be serialized
        print("THIS IS Experimental:DONT LOAD GLYPHS IN HERE")
        # except:
        #     print("THIS IS Experimental")


    def STACK2MEM(self,_string):
        register = self.register
        data = self.stack_ref.pop()
        self.instruction_pointer_ref.write_register(register,data["data_string"])


    def GOTO(self,_string):
        register = self.register
        try:
            self.instruction_pointer_ref.set_instruction_pointer(register)
        except:
            print("EVERYTHING BROKE BECAUSE YOU TRYED TO WRITE IN A REG WHICH DOESENT EXIST")


    def BOOL_H(self,_string):
        self.logger.info("mnemonic: BOOL_H")
        peak = self.stack_ref.pop()
        below = self.stack_ref.pop()
        if peak["value"] > below["value"]:
            self.instruction_pointer_ref.skip_instruction()

    def BOOL_L(self,_string):
        self.logger.info("mnemonic: BOOL_L")
        peak = self.stack_ref.pop()
        below = self.stack_ref.pop()
        if peak["value"] < below["value"]:
            self.instruction_pointer_ref.skip_instruction()

    def OUT(self,_string):
        print("***************************")
        print(self.stack_ref.peek()["data_string"])
        print("***************************")


    def HALT(self,_string):
        print("HALT")
        quit()
