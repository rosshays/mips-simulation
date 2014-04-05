import tkinter as tk

def initialize(self, master, root):
	tk.Frame.__init__(self, master)
	self.pack()
	self.create_widgets()
	# default configuration of window
	root.resizable(0,0)
	root.geometry("900x400")
	root.wm_title("MIPS Simulation")
	
def create_menu(self, root):
	self.menu = tk.Menu(self)
	root["menu"] = self.menu
	
def create_file(self, root):
	file_menu = tk.Menu(self.menu)
	file_menu.add_command(label = "Open",
		command = self.load_input_file)
	file_menu.add_command(label = "Exit", command = root.destroy)
	self.menu.add_cascade(menu = file_menu, label = "File")
	
def lock_text(self):
	self.input_text["state"] = "disabled"
	self.bin_text["state"] = "disabled"
	self.stack_text["state"] = "disabled"

def create_input(self,):
	self.input_text = tk.Text(self, width = 32)
	self.input_text["background"] = "grey"
		
def create_bin(self):
	self.bin_text = tk.Text(self, width = 32)
	self.bin_text["background"] = "grey"
	
def create_stack(self):
	self.stack_text = tk.Text(self, width = 32)
	self.stack_text["background"] = "white"
        
def create_control(self):
	# Control Panel
	self.control_panel = tk.Frame(self, width=400, height=800)
	button_panel = tk.Frame(self.control_panel)
	
	# Slider
	self.speed_slider = tk.Scale(self.control_panel,
		orient="horizontal")
	self.speed_slider["from"] = 1
	self.speed_slider["to"] = 60
	
	# Buttons
	self.step_button = tk.Button(button_panel, text="Step",
		command=self.step_once)
	self.run_button = tk.Button(button_panel, text="Run",
		command=self.run_prog)
	self.stop_button = tk.Button(button_panel, text="Stop",
		command=self.stop_prog)
	
	return button_panel

def adjust_layout(self):
	self.grid(column = 0, row = 0)
	self.control_panel.grid(column = 1, row = 0)
	self.input_text.grid(column = 10, row = 0)
	self.bin_text.grid(column = 15, row = 0)
	self.stack_text.grid(column = 20, row = 0)
    
def arrange_control(self, button_panel):
	self.speed_slider.grid(column=0, row=0)
	button_panel.grid(column=0,row=1, columnspan=3)
	self.step_button.grid(column=0, row=1)
	self.run_button.grid(column = 1, row = 1)
	self.stop_button.grid(column = 2, row = 1)
	
def update_bin(self):
	for line in self.program.machine_code:
		self.bin_text.insert("end", line)
		self.bin_text.insert("end", "\n")
