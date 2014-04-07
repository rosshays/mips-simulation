import tokenize

# MIPS INSTRUCTION SET:
#
# add $d, $s, $t
# addi $d, $s, imm
# addiu $d, $s, imm
# addu $d, $s, $t
# and $d, $s, $t 
# andi $t, $s, imm 
# beq $s, $t, offset 
# bgez $s, offset 
# bgezal $s, offset 
# bgtz $s, offset 
# blez $s, offset
# bltz $s, offset 
# bltzal $s, offset 
# bne $s, $t, offset
# div $s, $t 
# divu $s, $t 
# j target 
# jal target 
# jr $s
# lui $t, imm
# lw $t, offset($s)
# mfhi $d
# mflo $d
# mult $s, $t
# multu $s, $t
# noop
# or $d, $s, $t
# ori $d, $s, imm
# sb $t, offset($s) 
# sll $d, $t, h 
# sllv $d, $t, $s 
# slt $d, $s, $t 
# slti $t, $s, imm 
# sltiu $t, $s, imm
# sra $d, $t, h 
# srl $d, $t, h 
# srlv $d, $t, $s
# sub $d, $s, $t 
# subu $d, $s, $t 
# sw $t, offset($s) 
# syscall 
# xor $d, $s, $t 
# xori $t, $s, imm 

def convert_instruction(inst):
	if inst == "add":           return ("000000ssssstttttddddd00000100000", "R")
	elif inst == "addi":        return ("001000ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "addiu":       return ("0010 01ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "addu":        return ("000000ssssstttttddddd00000100001", "R")
	elif inst == "and":         return ("000000ssssstttttddddd00000100100", "R")
	elif inst == "andi":        return ("001100ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "beq":         return ("000100ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "bgez":        return ("000001sssss00001iiiiiiiiiiiiiiii", "I")
	elif inst == "bgezal":      return ("000001sssss10001iiiiiiiiiiiiiiii", "I")
	elif inst == "bgtz":        return ("000111sssss00000iiiiiiiiiiiiiii", "I")
	elif inst == "blez":        return ("000110sssss00000iiiiiiiiiiiiiiii", "I")
	elif inst == "bltz":        return ("000001sssss00000iiiiiiiiiiiiiiii", "I")
	elif inst == "bltzal":      return ("000001sssss10000iiiiiiiiiiiiiiii", "I")
	elif inst == "bne":         return ("000101ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "div":         return ("000000sssssttttt0000000000011010", "R")
	elif inst == "divu":        return ("000000sssssttttt0000000000011011", "R")
	elif inst == "j":           return ("000010iiiiiiiiiiiiiiiiiiiiiiiiii", "J")
	elif inst == "jal":         return ("000011iiiiiiiiiiiiiiiiiiiiiiiiii", "J")
	elif inst == "jr":          return ("000000sssss000000000000000001000", "R")
	elif inst == "lb":          return ("100000ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "lui":         return ("001111-----tttttiiiiiiiiiiiiiiii", "I")
	elif inst == "lw":          return ("100011ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "mfhi":        return ("0000000000000000ddddd00000010000", "R")
	elif inst == "mflo":        return ("0000000000000000ddddd00000010010", "R")
	elif inst == "mult":        return ("000000sssssttttt0000000000011000", "R")
	elif inst == "multu":       return ("000000sssssttttt0000000000011001", "R")
	elif inst == "noop":        return ("00000000000000000000000000000000", "")
	elif inst == "or":          return ("000000ssssstttttddddd00000100101", "R")
	elif inst == "ori":         return ("001101ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "sb":          return ("101000ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "sll":         return ("000000ssssstttttdddddhhhhh000000", "R")
	elif inst == "sllv":        return ("000000ssssstttttddddd-----000100", "R")
	elif inst == "slt":         return ("000000ssssstttttddddd00000101010", "R")
	elif inst == "slti":        return ("001010ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "sltiu":       return ("001011ssssstttttiiiiiiiiiiiiiiii", "I")
	elif inst == "sltu":        return ("000000ssssstttttddddd00000101011", "R")
	elif inst == "sltu":        return ("000000ssssstttttddddd00000101011", "R")
	elif inst == "sra":         return ("000000-----tttttdddddhhhhh000011", "R")
	elif inst == "srl":         return ("000000-----tttttdddddhhhhh000010", "R")
	elif inst == "srlv":        return ("000000ssssstttttddddd00000000110", "R")
	elif inst == "sub":         return ("000000ssssstttttddddd00000100010", "R")
	elif inst == "subu":        return ("000000ssssstttttddddd00000100011", "R")
	elif inst == "sw":          return ("101011ssssstttttiiiiiiiiiiiiiiii", "I")
	# elif inst == "syscall":     return ("000000--------------------001100", "")
	elif inst == "xor":         return ("000000ssssstttttddddd-----100110", "R")
	elif inst == "xori":        return ("001110ssssstttttiiiiiiiiiiiiiiii", "I")
	else: raise Exception("invalid instruction: " + str(inst))

def convert_register(register):
	if register == "$zero" or register == "$0": return "00000" 
	elif register == "$at" or register == "$1": return "00001"
	elif register == "$v0" or register == "$2": return "00010" 
	elif register == "$v1" or register == "$3": return "00011" 
	elif register == "$a0" or register == "$4": return "00100" 
	elif register == "$a1" or register == "$5": return "00101" 
	elif register == "$a2" or register == "$6": return "00110" 
	elif register == "$a3" or register == "$7": return "00111" 
	elif register == "$t0" or register == "$8": return "01000" 
	elif register == "$t1" or register == "$9": return "01001" 
	elif register == "$t2" or register == "$10": return "01010"  
	elif register == "$t3" or register == "$11": return "01011"  
	elif register == "$t4" or register == "$12": return "01100"  
	elif register == "$t5" or register == "$13": return "01101"  
	elif register == "$t6" or register == "$14": return "01110"  
	elif register == "$t7" or register == "$15": return "01111"  
	elif register == "$s0" or register == "$16": return "10000"  
	elif register == "$s1" or register == "$17": return "10001"  
	elif register == "$s2" or register == "$18": return "10010"  
	elif register == "$s3" or register == "$19": return "10011"  
	elif register == "$s4" or register == "$20": return "10100"  
	elif register == "$s5" or register == "$21": return "10101"  
	elif register == "$s6" or register == "$22": return "10110"  
	elif register == "$s7" or register == "$23": return "10111"  
	elif register == "$t8" or register == "$24": return "11000"  
	elif register == "$t8" or register == "$25": return "11001"  
	elif register == "$k0" or register == "$26": return "11010"  
	elif register == "$k1" or register == "$27": return "11011"  
	elif register == "$gp" or register == "$28": return "11100"  
	elif register == "$sp" or register == "$29": return "11101"  
	elif register == "$fp" or register == "$30": return "11110"  
	elif register == "$ra" or register == "$31": return "11111"  
	else: raise Exception("invalid register: " + register)

def convert_register_number(register):
	if register == "$zero" or register == "$0": return 0 
	elif register == "$at" or register == "$1": return 1 
	elif register == "$v0" or register == "$2": return 2 
	elif register == "$v1" or register == "$3": return 3 
	elif register == "$a0" or register == "$4": return 4 
	elif register == "$a1" or register == "$5": return 5 
	elif register == "$a2" or register == "$6": return 6 
	elif register == "$a3" or register == "$7": return 7 
	elif register == "$t0" or register == "$8": return 8 
	elif register == "$t1" or register == "$9": return 9 
	elif register == "$t2" or register == "$10": return 10  
	elif register == "$t3" or register == "$11": return 11  
	elif register == "$t4" or register == "$12": return 12  
	elif register == "$t5" or register == "$13": return 13  
	elif register == "$t6" or register == "$14": return 14  
	elif register == "$t7" or register == "$15": return 15  
	elif register == "$s0" or register == "$16": return 16  
	elif register == "$s1" or register == "$17": return 17  
	elif register == "$s2" or register == "$18": return 18  
	elif register == "$s3" or register == "$19": return 19  
	elif register == "$s4" or register == "$20": return 20  
	elif register == "$s5" or register == "$21": return 21  
	elif register == "$s6" or register == "$22": return 22  
	elif register == "$s7" or register == "$23": return 23  
	elif register == "$t8" or register == "$24": return 24  
	elif register == "$t8" or register == "$25": return 25  
	elif register == "$k0" or register == "$26": return 26  
	elif register == "$k1" or register == "$27": return 27  
	elif register == "$gp" or register == "$28": return 28  
	elif register == "$sp" or register == "$29": return 29  
	elif register == "$fp" or register == "$30": return 30  
	elif register == "$ra" or register == "$31": return 31  
	else: raise Exception("invalid register: " + register)

def convert_regmem(regmem):
	offset = regmem[:regmem.find("(")]
	reg = regmem[regmem.find("(") + 1 : regmem.find(")")]
	return reg, offset

def convert_immediate(imm):
	is_neg = bin(imm)[0] == '-'
	if is_neg:
		bin_str = bin(imm)[3:]
	else:
		bin_str = bin(imm)[2:]

	diff = 16 - len(bin_str)
	if diff <= 0: 
		raise Exception("immediate value too large: " + str(imm))
	else: 
		bin_str = diff * '0' + bin_str

	# check if we need to convert to two's complement negative form
	if is_neg:
		# invert all bits in the string
		for i in range(0,len(bin_str)):
			if bin_str[i] == '0':
				bin_str = bin_str[:i] + "1" + bin_str[i + 1:]
			else:
				bin_str = bin_str[:i] + "0" + bin_str[i + 1:]
		# add on to the string
		for i in range(len(bin_str)-1, -1, -1):
			if bin_str[i] == '0': 
				bin_str = bin_str[:i] + "1" + bin_str[i + 1:]
				break
			else:
				bin_str = bin_str[:i] + "0" + bin_str[i + 1:]           
	return bin_str

def pad_immediate(imm_str, desired_length):
	char = imm_str[0]
	imm_str = char * (desired_length - len(imm_str)) + imm_str
	return imm_str

def convert_line(input_line, line_number, label_dict = None):
	# get the tokens of our input line
	tokens = input_line.split("#")[0].split()
	tokens = [i.split(",")[0] for i in tokens]

	# get rid of all the labels in the input line
	i = 0
	while i < len(tokens):
		if tokens[i].find(":") != -1:
			tokens.pop(i)
		else:
			i += 1
	if len(tokens) == 0:
		return None

	instruction, format = convert_instruction(tokens[0])

	if format == "R":
		instruction = instruction.replace("ttttt", convert_register(tokens[3]))
		instruction = instruction.replace("sssss", convert_register(tokens[2]))
		instruction = instruction.replace("ddddd", convert_register(tokens[1]))

	elif format == "I":
		# special logic for branch instructions
		if tokens[0] == "beq" or tokens[0] == "bne":
			# figure out the offset (label_value - line_number)
			offset = label_dict[tokens[3]] - line_number
			instruction = instruction.replace("sssss", convert_register(tokens[1]))
			instruction = instruction.replace("ttttt", convert_register(tokens[2]))
			instruction = instruction.replace("iiiiiiiiiiiiiiii", convert_immediate(offset))
		elif tokens[0][0] == 'b':
			# figure out the offset (label_value - line_number)
			offset = label_dict[tokens[2]] - line_number
			instruction = instruction.replace("sssss", convert_register(tokens[1]))
			instruction = instruction.replace("iiiiiiiiiiiiiiii", convert_immediate(offset))

		# non branch instructions
		else:
			instruction = instruction.replace("sssss", convert_register(tokens[2]))
			instruction = instruction.replace("ttttt", convert_register(tokens[1]))
			instruction = instruction.replace("iiiiiiiiiiiiiiii", convert_immediate(int(tokens[3])))

	elif format == "J":
		label_address = label_dict[tokens[1]]
		label_address = convert_immediate(label_address)
		label_address = pad_immediate(label_address, 26)
		instruction = instruction.replace("iiiiiiiiiiiiiiiiiiiiiiiiii", str(label_address))

	else:
		print("This should not happen.")

	return instruction