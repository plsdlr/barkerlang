import prime as p
import serializer as s


class _number:

    def __init__(self,initial_factor,parent_node):
        self.init_fact = initial_factor
        self.parent_node = parent_node
        self.child_nodes = []
        self.evaluate()


    def make_node(self, value):
        new_node = _number(value,self)
        self.child_nodes.append(new_node)


    def evaluate(self):
        if self.init_fact != 2 and self.init_fact % 2 != 0 and self.init_fact != 1 :
            new_number = p.find_prime_number_number(self.init_fact)
            factors_list = p.prime_factors(new_number)
            factors_list.append(1)
            for i in factors_list:
                self.make_node(i)


class encoder(_number):

    def __init__(self):
        self.teststring = ""
        self.nodes =[]


    def number_prime_factors(self,number):
        a = p.prime_factors(number)
        for h in a:                       #replace 
            new_term = _number(h,0)
            self.nodes.append(new_term)


    def parsing_list(self,node):
        for character in node:
            if character.child_nodes:
                self.teststring = self.teststring+"("
            elif character.init_fact == 2:
                self.teststring = self.teststring+":"
            if character.init_fact == 1:
                self.teststring = self.teststring+")"
            self.parsing_list(character.child_nodes)


    def cleanup(self):
        self.nodes = []
        self.teststring =""


    def encode(self,number):
        self.cleanup()
        self.number_prime_factors(number)
        self.parsing_list(self.nodes)
        serialized_data = s.serialize(self.teststring,0,number)
        return serialized_data
