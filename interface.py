import tkinter as tk

def initialize(self, master, root):
	tk.Frame.__init__(self, master)
	self.pack()
	self.create_widgets()
	# default configuration of window
	root.resizable(0,0)
	root.geometry("1400x800")
	root.wm_title("MIPS Simulation")	
	
def create_menu(self, root):
	self.menu = tk.Menu(self)
	root["menu"] = self.menu
	
def create_file(self, root):
	file_menu = tk.Menu(self.menu)
	file_menu.add_command(label = "Open", command = self.load_input_file)
	file_menu.add_command(label = "Exit", command = root.destroy)
	self.menu.add_cascade(menu = file_menu, label = "File")
	
def lock_text(self):
	self.input_text["state"] = "disabled"
	self.bin_text["state"] = "disabled"

def create_input(self, color):
	self.input_text = tk.Text(self)
	self.input_text["background"] = color
		
def create_bin(self, color):
	self.bin_text = tk.Text(self)
	self.bin_text["background"] = color
        
def create_control(self):
	# Control Panel
	self.control_panel = tk.Frame(self, width=400, height=800)
	button_panel = tk.Frame(self.control_panel)
	
	# Slider
	self.speed_slider = tk.Scale(self.control_panel, orient="horizontal")
	self.speed_slider["from"] = 1
	self.speed_slider["to"] = 60
	
	# Buttons
	self.step_button = tk.Button(button_panel, text="Step", command=self.step_once)
	self.run_button = tk.Button(button_panel, text="Run")
	self.stop_button = tk.Button(button_panel, text="Stop")
	
	return button_panel

def adjust_layout(self):
	self.grid(column = 0, row = 0)
	self.control_panel.grid(column = 1, row = 0)
	self.input_text.grid(column = 10, row = 0)
	self.bin_text.grid(column = 15, row = 0)
    
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
