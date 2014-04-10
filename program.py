import conversion as conv
import instruction as ins
import stack

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
		self.registers[29] = 0x1000
		self.labels = {}
		self.pc = 0
		self.memory = stack.Stack(self.registers[29])
		self.hi = 0
		self.lo = 0

		counter = 0

		# build the label dictionary ahead of time
		addr_counter = 0
		for line in source:
			# remove comments and whitespace
			tokens = line.split("#")[0].split()
			tokens = [i.split(",")[0].lstrip().rstrip() for i in tokens]
			i = 0
			while i < len(tokens):
				if tokens[i].find(":") != -1:
					self.labels[tokens[i][:-1]] = addr_counter
					tokens.pop(i)
				else:
					i += 1
			if len(tokens) > 0:
				addr_counter += ins.Instruction.SIZE

		# now create instructions
		line_counter = 0
		for line in source:
			inst = conv.convert_line(line, counter, self.labels)
			if inst != None:
				new_instruction = ins.Instruction(self, line, line_counter)
				self.machine_code.append(inst)
				self.instructions.append(new_instruction)
				counter += ins.Instruction.SIZE
			line_counter += 1
		self.inst_count = counter // 4

			
	def is_finished(self):
		return self.pc // 4 >= self.inst_count

	def step_once(self):
		inst = self.instructions[self.pc // 4]
		self.pc = inst.execute(self.pc, self.labels)

	def reset(self):
		self.registers = [0] * 32
		self.registers[29] = 0x1000
		self.pc = 0
		self.memory = stack.Stack(self.registers[29])
		self.hi = 0
		self.lo = 0


	def get_all_registers(self):
		return self.registers

	def get_register(self, reg):
		regi = int(reg)
		if(regi < 32 and regi >= 0):
			return self.registers[regi]
		else:
			print("Error: invalid register")

	def set_hi(self, value):
		self.hi = value

	def get_hi(self):
		return self.hi

	def set_lo(self, value):
		self.lo = value

	def get_lo(self):
		return self.lo

	def set_register(self, reg, value):
		regi = int(reg)
		if(regi < 32 and regi > 0):
			self.registers[regi] = value
		elif regi == 0:
			pass
		else:
			print("Error: invalid register")
			
	def get_stack(self):
		return self.memory

	def get_memory(self, reg, offset):
		pass

	def set_memory(self, reg, offset, value):
		pass
