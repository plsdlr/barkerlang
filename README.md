# barkerlang

barkerlang is a experimental programming language utilizing xenotation. A longer definition will be given later. It needs Python 3.6. To run one of the provided files:

    python3 main.py --path pathtofilehere  


Provided code examples:

    adding
    for loop
    while loop

Full Code Example (adding):

    ::((::))
    :(:::)
    Y
    * 

Currently everything runs in Debug Mode. Example output for "for loop":

    INFO:root:LOAD CODE
    INFO:root:INIT STACK
    INFO:root:INIT PARSER
    INFO:root:LOAD CODE
    INFO:root:INIT MEMORY
    INFO:root:START EXECUTION
    
    --------------------------------->
    +p
    INFO:barkerlang.interpreter.interpreter:Evaluate Instruction: +
    INFO:barkerlang.interpreter.interpreter:mnemonic: XENOTATION
    _______________________________
    INFO:root:STACK DUMP:
    INFO:root:[{'data_string': '+p', 'value': 1, 'datatype': 'XENOTATIONS'}]
    _______________________________
    INFO:root:REGISTER:
    INFO:root:0
    _______________________________
    INFO:root:MEMORY DUMP:
    INFO:root:['+p', '::((:)):', '((:)):', '(((:):))', '∆', 'V', '∆', 'V', '(:)', '::((:)):', '∆', '+p', 'Y', '^', '+p', 'Y', 'V', '^', '(((:):))', '∆', '^', '(:)(:)', '∆', '<', '∞', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    _______________________________
    INFO:root:INSTRUCTION POINTER:
    INFO:root:1
    _______________________________
    Nex Step


Use at own Risk.
