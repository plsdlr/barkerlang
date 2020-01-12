import os
import argparse
import logging
from decoder import xenoparser as parser
from stack_memory import Stack as stack
from stack_memory import instruction_pointer as pointer
from interpreter import interpreter as interpreter
from encode import encoder as encoder


parser_cmd = argparse.ArgumentParser(description='******  BARKERLANG 0.33 ******'+'\n'+'A LANGUAGE POWERED BY XENOTATIONS AND GLYPHS')
parser_cmd.add_argument('--path',  help='Load Instructions from File')
parser_cmd.add_argument('--instruction',  help='Raw instruction')
parser_cmd.add_argument('--mem_size',  help='Experimental memory size')

args = parser_cmd.parse_args()

logging.basicConfig(level=logging.DEBUG)
module_logger = logging.getLogger('barkerlang.main')

logging.info("LOAD CODE")

mem_size = 99
#code = open("/Users/paul/xenotations_first.txt", "r")

def load_from_fime(path):
    code = open(path, "r")
    c = code.readlines()
    clean_code = list(map(lambda x: x.rstrip(), c))
    return clean_code

logging.info("INIT STACK")
new_stack = stack()
logging.info("INIT PARSER")
new_decoder = parser()
new_encoder = encoder()

if args.path:
    logging.info("LOAD CODE")
    clean_code = load_from_fime(args.path)
else:
    logging.error("No Input Specification")
    exit()



logging.info("INIT MEMORY")
new_mem = pointer(clean_code, mem_size)
new_interp = interpreter(new_decoder,new_stack,new_encoder,new_mem)

logging.info("START EXECUTION")




while True:
    os.system("clear")
    new_interp.evaluate()
    print("_______________________________")
    logging.info("STACK DUMP:")
    logging.info(new_interp.stack_ref.items)
    print("_______________________________")
    logging.info("REGISTER:")
    logging.info(new_interp.register)
    print("_______________________________")
    logging.info("MEMORY DUMP:")
    logging.info(new_mem.memory_register)
    print("_______________________________")
    logging.info("INSTRUCTION POINTER:")
    logging.info(new_mem.instruction_pointer_position)
    print("_______________________________")
    input("Nex Step")
