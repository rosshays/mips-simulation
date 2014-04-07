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
		self.labels = {}
		self.pc = 0
		self.memory = stack.Stack()

		counter = 0
		for line in source:
			inst = conv.convert_line(line, counter, self.labels)
			if inst != None:
				new_instruction = ins.Instruction(self, inst)
				self.machine_code.append(inst)
				self.instructions.append(new_instruction)
				counter += ins.Instruction.SIZE
			
	def step_once(self):
		inst = self.instructions[self.pc / 4]
		self.pc = inst.execute(self.pc, self.labels)

	def reset(self):
		self.registers = [0] * 32
		self.pc = 0
		self.memory = stack.Stack()


	def get_all_registers(self):
		return self.registers

	def get_register(self, reg):
		regi = int(reg)
		if(regi < 32 and regi >= 0):
			return self.registers[regi]
		else:
			print("Error: invalid register")

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
