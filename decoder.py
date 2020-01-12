from functools import reduce
import prime as p
import serializer as s

class xenoparser():

    def eval_test(self,a,b):
        valcell = self.reduce_list(a)
        vall_add_sub = self.reduce_list_add_sub(b)
        primeval = p.nth_prime_number(valcell+vall_add_sub)
        return primeval

    def reduce_list(self, _list):
        #ugly quick fix delete later
        if _list:
            return reduce(lambda x ,y: x*y, _list)
        else:
            return 0

    def reduce_list_add_sub(self, _add_sub):
        if _add_sub:
            return reduce(lambda x ,y: x+y, _add_sub)
        else:
            return 0

    def _xeno_parser(self,character,datatype):
        list_of_expressions= []
        list_of_add_and_sub = []
        list_of_expressions.append([])
        list_of_add_and_sub.append([0])
        for i in character:
            if i == "(":
                list_of_expressions.append([])
                list_of_add_and_sub.append([0])
            elif i == ")":
                last_element = list_of_expressions.pop()
                last_element_add_sub = list_of_add_and_sub.pop()
                value = self.eval_test(last_element,last_element_add_sub)
                list_of_expressions[-1].append(value)
            elif i == ":":
                list_of_expressions[-1].append(2)
            elif i == "+":
                list_of_add_and_sub[-1].append(1)
            elif i == "-":
                list_of_add_and_sub[-1].append(-1)
            elif i == "p":
                pass
            else:
                print("WRONG SYNTAX")
                exit()
        value = self.reduce_list(list_of_expressions[0])+ self.reduce_list_add_sub(list_of_add_and_sub[0])
        return s.serialize(character,datatype,value)
