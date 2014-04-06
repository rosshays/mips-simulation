import conversion as conv

# convert an instruction to a binary string(s)
# returns a 3-tuple of opcode, inst, format
# convert_instruction(inst)

# convert an register to a binary string
# returns a 2-tuple of binary version and decimal version
# convert_register(reg)

# convert an immediate value to a binary string
# will throw an error if the value is too large for MIPS
# convert_immediate(imm)

# takes a whole line as input and returns a binary string of the instruction
# as represented in MIPS machine code
# convert_line(line)

class Program:

    # create a new MIPS program to simulate
    # source should contain a list of mips source code, line by line
    def __init__(self, source):
        self.instructions = []
        self.machine_code = []
        self.registers = [0] * 32
        self.labels = {}
        self.pc = 0
        self.memory = Stack()

        counter = 0
        for line in source:
            inst, found_labels = conv.convert_line(line, self.labels)
            for label in found_labels:
                self.labels[label] = counter
            new_instruction = Instruction(self, line)
            self.machine_code.append(inst)
            self.instructions.append(new_instruction)
            counter += Instruction.SIZE
            
    def get_all_registers(self):
        return self.registers

    def get_register(self, reg):
        return self.registers[reg]

    def set_register(self, reg, value):
        if reg != 0:
            self.registers[reg] = value

    def get_memory(self, reg, offset):
        pass

    def set_memory(self, reg, offset, value):
        pass

class Instruction:
    SIZE = 4

    def __init__(self, program, line):
        self.program = program
        self.line = line

        tokens = line.split("#")[0].split()
        tokens = [i.split(",")[0] for i in tokens]

        i = 0
        labels = []
        while i < len(tokens):
            if tokens[0].find(":") != -1:
                labels.append(tokens[i])
                tokens.pop(i)
            else:
                i += 1

        self.labels_used = labels
        self.instruction = tokens[0]
        self.params = []
        for i in range(1, len(tokens)):
            self.params.append(tokens[i])
        
    def execute(self):
        if self.instruction == "add":
            s = self.program.get_register(self.params[1])
            t = self.program.get_register(self.params[2])
            d = s + t
            self.program.set_register(d)

        elif self.instruction == "addi":
            s = self.program.get_register(self.params[1])
            t = self.program.get_register(self.params[2])
            d = s + t
            self.program.set_register(d)

        elif self.instruction == "addiu":     
            return ("0010 01ssssstttttiiiiiiiiiiiiiiii", "I")
        elif self.instruction == "addu":
            return ("000000ssssstttttddddd00000100001", "R")
        elif self.instruction == "and":       
            return ("000000ssssstttttddddd00000100100", "R")
        elif self.instruction == "andi":      
            return ("001100ssssstttttiiiiiiiiiiiiiiii", "I")
        elif self.instruction == "beq":       
            return ("000100ssssstttttiiiiiiiiiiiiiiii", "I")
        elif self.instruction == "bgez":      
            return ("000001sssss00001iiiiiiiiiiiiiiii", "I")
        elif self.instruction == "bgezal":    
            return ("000001sssss10001iiiiiiiiiiiiiiii", "I")
        elif self.instruction == "bgtz":      
            return ("000111sssss00000iiiiiiiiiiiiiii", "I")
        elif self.instruction == "blez":      
            return ("000110sssss00000iiiiiiiiiiiiiiii", "I")
        elif self.instruction == "bltz":      
            return ("000001sssss00000iiiiiiiiiiiiiiii", "I")
        elif self.instruction == "bltzal":    
            return ("000001sssss10000iiiiiiiiiiiiiiii", "I")
        elif self.instruction == "bne":       
            return ("000101ssssstttttiiiiiiiiiiiiiiii", "I")
        elif self.instruction == "div":       
            return ("000000sssssttttt0000000000011010", "R")
        elif self.instruction == "divu":      
            return ("000000sssssttttt0000000000011011", "R")
        elif self.instruction == "j":         
            return ("000010iiiiiiiiiiiiiiiiiiiiiiiiii", "J")
        elif self.instruction == "jal":       
            return ("000011iiiiiiiiiiiiiiiiiiiiiiiiii", "J")
        elif self.instruction == "jr":        
            return ("000000sssss000000000000000001000", "R")
        elif self.instruction == "lb":        
            return ("100000ssssstttttiiiiiiiiiiiiiiii", "")
        elif self.instruction == "lui":       
            return ("001111-----tttttiiiiiiiiiiiiiiii", "")
        elif self.instruction == "lw":        
            return ("100011ssssstttttiiiiiiiiiiiiiiii", "")
        elif self.instruction == "mfhi":      
            return ("0000000000000000ddddd00000010000", "")
        elif self.instruction == "mflo":      
            return ("0000000000000000ddddd00000010010", "")
        elif self.instruction == "mult":      
            return ("000000sssssttttt0000000000011000", "")
        elif self.instruction == "multu":     
            return ("000000sssssttttt0000000000011001", "")
        elif self.instruction == "noop":      
            return ("00000000000000000000000000000000", "")
        elif self.instruction == "or":        
            return ("000000ssssstttttddddd00000100101", "")
        elif self.instruction == "ori":       
            return ("001101ssssstttttiiiiiiiiiiiiiiii", "")
        elif self.instruction == "sb":        
            return ("101000ssssstttttiiiiiiiiiiiiiiii", "")
        elif self.instruction == "sll":       
            return ("000000ssssstttttdddddhhhhh000000")
        elif self.instruction == "sllv":      
            return ("000000ssssstttttddddd-----000100")
        elif self.instruction == "slt":       
            return ("000000ssssstttttddddd00000101010", "")
        elif self.instruction == "slti":      
            return ("001010ssssstttttiiiiiiiiiiiiiiii", "")
        elif self.instruction == "sltiu":     
            return ("001011ssssstttttiiiiiiiiiiiiiiii", "")
        elif self.instruction == "sltu":      
            return ("000000ssssstttttddddd00000101011", "")
        elif self.instruction == "sltu":      
            return ("000000ssssstttttddddd00000101011", "")
        elif self.instruction == "sra":       
            return ("000000-----tttttdddddhhhhh000011")
        elif self.instruction == "srl":       
            return ("000000-----tttttdddddhhhhh000010")
        elif self.instruction == "srlv":      
            return ("000000ssssstttttddddd00000000110", "")
        elif self.instruction == "sub":       
            return ("000000ssssstttttddddd00000100010", "")
        elif self.instruction == "subu":      
            return ("000000ssssstttttddddd00000100011", "")
        elif self.instruction == "sw":        
            return ("101011ssssstttttiiiiiiiiiiiiiiii", "")
        elif self.instruction == "syscall":   
            return ("000000--------------------001100", "")
        elif self.instruction == "xor":       
            return ("000000ssssstttttddddd-----100110", "")
        elif self.instruction == "xori":      
            return ("001110ssssstttttiiiiiiiiiiiiiiii", "")





        pass
    
class Stack:

    def __init__(self):
        pass
