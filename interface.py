# USES TABS FOR INDENTATION
import tkinter as tk

def initialize(self, master, root):
	tk.Frame.__init__(self, master)
	self.pack()
	self.create_widgets()
	# default configuration of window
	root.resizable(0,0)
	root.geometry("1050x500")
	root.wm_title("MIPS Simulation")
	
	
def create_menu(self, root):
	self.menu = tk.Menu(self)
	root["menu"] = self.menu
	
	file_menu = tk.Menu(self.menu)
	file_menu.add_command(label = "Open",
		command = self.load_input_file)
	file_menu.add_command(label = "Exit", command = root.destroy)
	self.menu.add_cascade(menu = file_menu, label = "File")

def lock_text(self):
	self.input_text["state"] = "disabled"
	self.bin_text["state"] = "disabled"
	self.stack_text["state"] = "disabled"
	self.register_text["state"] = "disabled"

def unlock_text(self):
	self.input_text["state"] = "normal"
	self.bin_text["state"] = "normal"
	self.stack_text["state"] = "normal"
	self.register_text["state"] = "normal"

def create_text_boxes(self):
	self.input_text = tk.Text(self, width = 25, height = 33)
	self.input_text["background"] = "grey"
	self.input_text.grid(column = 10, row = 0)
		
	self.bin_text = tk.Text(self, width = 35, height = 33)
	self.bin_text["background"] = "grey"
	self.bin_text.grid(column = 15, row = 0)
	
	self.stack_text = tk.Text(self, width = 25, height = 33)
	self.stack_text["background"] = "grey"
	self.stack_text.grid(column = 20, row = 0)

	self.register_text = tk.Text(self, width = 25, height = 33)
	self.register_text["background"] = "grey"
	self.register_text.grid(column = 25, row = 0)
	
def create_control(self):
	# Control Panel
	self.control_panel = tk.Frame(self, width=400, height=800)
	button_panel = tk.Frame(self.control_panel)
	
	self.control_panel.grid(column = 1, row = 0)
	
	# Slider
	self.speed_slider = tk.Scale(self.control_panel,
		orient="horizontal")
	self.speed_slider["from"] = 1
	self.speed_slider["to"] = 60
	self.speed_slider.grid(column=0, row=0)
	
	# Buttons
	button_panel.grid(column=0,row=2, columnspan=2)
	
	self.step_button = tk.Button(button_panel, text="Step",
		command=self.step_once, state = "disabled")
	self.step_button.grid(column=0, row=0)
	
	self.run_button = tk.Button(button_panel, text="Run",
		command=self.run_prog, state = "disabled")
	self.run_button.grid(column = 1, row = 0)	
	
	self.stop_button = tk.Button(button_panel, text="Stop",
		command=self.stop_prog, state = "disabled")
	self.stop_button.grid(column = 0, row = 1)
		
	self.reset_button = tk.Button(button_panel, text="Reset",
		command=self.reset, state = "disabled")
	self.reset_button.grid(column = 1, row = 1)
	
def update_bin(self):
	print(">Updating binary")
	for line in self.program.machine_code:
		self.bin_text.insert("end", str(line) + "\n")

def update_stack(self):
	print(">Updating stack")
	self.stack_text.delete("1.0", "end")
	stack = self.program.get_stack()
	contents = stack.get_contents()
	for item in contents:
		output = str(hex(item)) + ":\t" + str(contents[item])
		self.stack_text.insert("end", output)
		if(self.program.get_register(29) == item):
			self.stack_text.insert("end", "\t<--pc")
		self.stack_text.insert("end", "\n")
	
def update_registers(self):
	print(">Updating registers")
	self.register_text.delete("1.0", "end")
	registers = self.program.get_all_registers()
	self.register_text["state"] = "normal"
	regnum = 0
	for register in registers:
		output = "$" + str(regnum) + ":\t" + str(register) + "\n"
		self.register_text.insert("end", output)
		regnum += 1

