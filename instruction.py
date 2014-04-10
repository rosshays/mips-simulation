import conversion as conv

class Instruction:
	SIZE = 4

	def __init__(self, program, line, line_number):
		self.program = program
		self.line = line
		self.line_number = line_number # used for highlighting later on

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
		
	# execute the instruction represented by self and return the new PC
	def execute(self, pc, label_dict):
		if self.instruction == "add":
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = conv.convert_register_number(self.params[2])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			d = s + t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE

		elif self.instruction == "addi":
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = int(self.params[2])
			s = self.program.get_register(p1)
			t = p2
			d = s + t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE

		# elif self.instruction == "addiu":     
		#     return ("0010 01ssssstttttiiiiiiiiiiiiiiii", "I")
		# elif self.instruction == "addu":
			# return ("000000ssssstttttddddd00000100001", "R")

		elif self.instruction == "and":       
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = conv.convert_register_number(self.params[2])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			d = s & t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE

		elif self.instruction == "andi":      
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = int(self.params[2])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			d = s & t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE

		elif self.instruction == "beq":       
			reg1 = conv.convert_register_number(self.params[0])
			reg2 = conv.convert_register_number(self.params[1])
			if self.program.get_register(reg1) == self.program.get_register(reg2):
				return label_dict[self.params[2]]
			else:
				return pc + Instruction.SIZE

		elif self.instruction == "bgez":      
			reg1 = conv.convert_register_number(self.params[0])
			if self.program.get_register(reg1) >= 0:
				return label_dict[self.params[1]]
			else:
				return pc + Instruction.SIZE

		elif self.instruction == "bgezal":    
			reg1 = conv.convert_register_number(self.params[0])
			if self.program.get_register(reg1) >= 0:
				self.program.set_register(31, pc + Instruction.SIZE)
				return label_dict[self.params[1]]
			else:
				return pc + Instruction.SIZE

		elif self.instruction == "bgtz":      
			reg1 = conv.convert_register_number(self.params[0])
			if self.program.get_register(reg1) > 0:
				return label_dict[self.params[1]]
			else:
				return pc + Instruction.SIZE

		elif self.instruction == "blez":      
			reg1 = conv.convert_register_number(self.params[0])
			if self.program.get_register(reg1) <= 0:
				return label_dict[self.params[1]]
			else:
				return pc + Instruction.SIZE

		elif self.instruction == "bltz":      
			reg1 = conv.convert_register_number(self.params[0])
			if self.program.get_register(reg1) < 0:
				return label_dict[self.params[1]]
			else:
				return pc + Instruction.SIZE

		elif self.instruction == "bltzal":    
			reg1 = conv.convert_register_number(self.params[0])
			if self.program.get_register(reg1) < 0:
				self.program.set_register(31, pc + Instruction.SIZE)
				return label_dict[self.params[1]]
			else:
				return pc + Instruction.SIZE

		elif self.instruction == "bne":       
			reg1 = conv.convert_register_number(self.params[0])
			reg2 = conv.convert_register_number(self.params[1])
			if self.program.get_register(reg1) != self.program.get_register(reg2):
				return label_dict[self.params[2]]
			else:
				return pc + Instruction.SIZE

		elif self.instruction == "div":       
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			self.program.set_hi(s % t)
			self.program.set_lo(s // t)
			return pc + Instruction.SIZE

		# elif self.instruction == "divu":      
		# 	return ("000000sssssttttt0000000000011011", "R")

		elif self.instruction == "j":         
			return int(label_dict[self.params[0]])

		elif self.instruction == "jal":       
			return_addr = pc + Instruction.SIZE
			self.program.set_register(31, return_addr)
			return label_dict[self.params[0]]

		elif self.instruction == "jr":        
			return self.program.get_register(conv.convert_register_number(self.params[0]))

		# elif self.instruction == "lb":        
		# 	return ("100000ssssstttttiiiiiiiiiiiiiiii", "")
		# elif self.instruction == "lui":       
		# 	return ("001111-----tttttiiiiiiiiiiiiiiii", "")

		elif self.instruction == "lw":        
			p0 = conv.convert_register_number(self.params[0])
			reg, offset = conv.convert_regmem(self.params[1])
			p1 = conv.convert_register_number(reg)
			addr = self.program.get_register(p1) + int(offset)
			x = self.program.get_stack().load_word(addr)
			self.program.set_register(p0, x)
			return pc + Instruction.SIZE

		elif self.instruction == "mfhi":      
			p0 = conv.convert_register_number(self.params[0])
			self.program.set_register(p0, self.program.get_hi())
			return pc + Instruction.SIZE

		elif self.instruction == "mflo":      
			p0 = conv.convert_register_number(self.params[0])
			self.program.set_register(p0, self.program.get_lo())
			return pc + Instruction.SIZE

		elif self.instruction == "mult":      
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			s = self.program.get_register(p0)
			t = self.program.get_register(p1)
			d = s * t

			bin_d = format(d, '#066b')
			bin_hi = bin_d[:32]
			bin_lo = bin_d[32:]

			self.program.set_hi(int(bin_hi,2))
			self.program.set_lo(int(bin_lo,2))
			return pc + Instruction.SIZE

		# elif self.instruction == "multu":     
		# 	return ("000000sssssttttt0000000000011001", "")


		elif self.instruction == "noop":      
			return pc + Instruction.SIZE

		elif self.instruction == "or":        
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = conv.convert_register_number(self.params[2])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			d = s | t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE

		elif self.instruction == "ori":          
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = int(self.params[2])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			d = s | t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE

		# elif self.instruction == "sb":        
		# 	return ("101000ssssstttttiiiiiiiiiiiiiiii", "")

		# elif self.instruction == "sll":
			
		# 	return ("000000ssssstttttdddddhhhhh000000")

		# elif self.instruction == "sllv":      
		# 	return ("000000ssssstttttddddd-----000100")
		
		# elif self.instruction == "slt":       
		# 	return ("000000ssssstttttddddd00000101010", "")
		
		# elif self.instruction == "slti":      
		# 	return ("001010ssssstttttiiiiiiiiiiiiiiii", "")
		
		# elif self.instruction == "sltiu":     
		# 	return ("001011ssssstttttiiiiiiiiiiiiiiii", "")
		
		# elif self.instruction == "sltu":      
		# 	return ("000000ssssstttttddddd00000101011", "")
		
		# elif self.instruction == "sltu":      
		# 	return ("000000ssssstttttddddd00000101011", "")
		
		# elif self.instruction == "sra":       
		# 	return ("000000-----tttttdddddhhhhh000011")
		
		# elif self.instruction == "srl":       
		# 	return ("000000-----tttttdddddhhhhh000010")
		
		# elif self.instruction == "srlv":      
		# 	return ("000000ssssstttttddddd00000000110", "")

		elif self.instruction == "sub":
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = conv.convert_register_number(self.params[2])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			d = s - t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE

		# elif self.instruction == "subu":      
		# 	return ("000000ssssstttttddddd00000100011", "")

		elif self.instruction == "sw":        
			p0 = conv.convert_register_number(self.params[0])
			p1, offset = conv.convert_regmem(self.params[1])
			addr = self.program.get_register(conv.convert_register_number(p1)) + int(offset)
			val = self.program.get_register(p0)
			x = self.program.get_stack().store_word(addr, val)
			return pc + Instruction.SIZE

		# elif self.instruction == "syscall":   
		# 	return ("000000--------------------001100", "")

		elif self.instruction == "xor":       
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = conv.convert_register_number(self.params[2])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			d = s ^ t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE

		elif self.instruction == "xori":      
			p0 = conv.convert_register_number(self.params[0])
			p1 = conv.convert_register_number(self.params[1])
			p2 = int(self.params[2])
			s = self.program.get_register(p1)
			t = self.program.get_register(p2)
			d = s ^ t
			self.program.set_register(p0, d)
			return pc + Instruction.SIZE
