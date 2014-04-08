import program as mips
import tkinter as tk
import conversion as conv
import instruction as ins
from tkinter import filedialog
import time


class MIPSApplication(tk.Frame):

	def __init__(self, master = None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.create_widgets()
		# default configuration of window
		root.resizable(0,0)
		root.geometry("1200x600")
		root.wm_title("MIPS Simulator")
		self.job = None

	def create_widgets(self):
		# create menu
		self.menu = tk.Menu(self)
		root["menu"] = self.menu
		# add file menu
		file_menu = tk.Menu(self.menu)
		file_menu.add_command(label = "Open", command = self.load_input_file)
		file_menu.add_command(label = "Exit", command = root.destroy)
		self.menu.add_cascade(menu = file_menu, label = "File")
		
		# create grid layout for progam
		self.grid(column = 0, row = 0)
		
		# create text areas
		self.input_text = tk.Text(self, width = 43, height = 35)
		self.input_text["background"] = "grey"
		self.input_text.grid(column = 10, row = 0)
		self.bin_text = tk.Text(self, width = 42, height = 35)
		self.bin_text["background"] = "grey"
		self.bin_text.grid(column = 15, row = 0)
		self.stack_text = tk.Text(self, width = 24, height = 35)
		self.stack_text["background"] = "grey"
		self.stack_text.grid(column = 20, row = 0)
		self.register_text = tk.Text(self, width = 19, height = 35)
		self.register_text["background"] = "grey"
		self.register_text.grid(column = 25, row = 0)

		# lock text areas
		self.lock_text()

		# create controls
		# Control Panel
		self.control_panel = tk.Frame(self, width=400, height=800)
		button_panel = tk.Frame(self.control_panel)
		self.control_panel.grid(column = 1, row = 0)
		# Slider
		self.speed_slider = tk.Scale(self.control_panel, orient="horizontal")
		self.speed_slider["from"] = 1
		self.speed_slider["to"] = 60
		self.speed_slider.grid(column=0, row=0)
		# Buttons
		button_panel.grid(column=0,row=2, columnspan=2)
		self.step_button = tk.Button(button_panel, text="Step", command=self.step_once, state = "disabled")
		self.step_button.grid(column=0, row=0)
		self.run_button = tk.Button(button_panel, text="Run", command=self.run_prog, state = "disabled")
		self.run_button.grid(column = 1, row = 0)	
		self.stop_button = tk.Button(button_panel, text="Stop", command=self.stop_prog, state = "disabled")
		self.stop_button.grid(column = 0, row = 1)
		self.reset_button = tk.Button(button_panel, text="Reset", command=self.reset, state = "disabled")
		self.reset_button.grid(column = 1, row = 1)

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

	def get_file(self):
		filename = tk.filedialog.askopenfilename()
		if filename == "": return

		# allow editing on our text fields and wipe them
		self.input_text["state"] = "normal"
		self.bin_text["state"] = "normal"
		self.input_text.delete("1.0", "end")
		self.bin_text.delete("1.0", "end")
		
		return filename
		
	def get_lines(self, filename):
		# create a list to contain the lines
		lines = []

		# iterate through all the lines in filename
		with open(filename) as f:
			for line in f:
				lines.append(line)
		return lines

	def update_input(self, lines):
		print(">Updating input")
		i = 0
		for line in lines:
			content = str(i) + ":\t" + str(line)
			self.input_text.insert("end", content)
			i += 1

	def update_bin(self):
		print(">Updating binary")
		i = 0
		for line in self.program.machine_code:
			content = str(hex(i)) + ":\t" + str(line)
			self.bin_text.insert("end", content + "\n")
			i += 4

	def update_stack(self):
		print(">Updating stack")
		self.stack_text.delete("1.0", "end")
		stack = self.program.get_stack()
		contents = stack.get_contents()
		sp = self.program.get_register(29)
		if not(sp in contents):
			stack.store_word(sp, "-----")
		sorted_stack = sorted(contents, reverse = True)
		for item in sorted_stack:
			output = str(hex(item)) + ":\t" + str(contents[item])
			self.stack_text.insert("end", output)
			if(sp == item):
				self.stack_text.insert("end", "\t<--$sp")
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
		self.register_text.insert("end", "$HI:\t" + str(self.program.get_hi()) + "\n")
		self.register_text.insert("end", "$LO:\t" + str(self.program.get_lo()) + "\n")

	def step_once(self):
		print(">Stepping once")
		self.reset_button["state"] = "normal"
		self.program.step_once()
		self.unlock_text()
		self.update_stack()
		self.update_registers()
		self.lock_text()
	
	def run_prog(self):
		print(">Running program")
		self.reset_button["state"] = "normal"
		self.stop_button["state"] = "normal"
		self.step_once()
		if not self.program.is_finished():
			self.job = root.after(1000//self.speed_slider.get(), self.run_prog)
		else:
			self.job = None
		
	def stop_prog(self):
		print(">Stopping program")
		self.stop_button["state"] = "disabled"
		if self.job is not None:
			root.after_cancel(self.job)
			self.job = None
		
	def reset(self):
		print(">Resetting simulator")
		self.reset_button["state"] = "disabled"
		self.stop_button["state"] = "disabled"
		self.program.reset()
		self.unlock_text()
		self.update_stack()
		self.update_registers()
		self.lock_text()

	def load_input_file(self):
		filename = self.get_file()
		if filename == None: return
		lines = self.get_lines(filename)
		self.program = mips.Program(lines)
		self.unlock_text()
		self.update_input(lines)
		self.update_bin()
		self.update_stack()
		self.update_registers()
		self.lock_text()
		self.step_button["state"] = "normal"
		self.run_button["state"] = "normal"


root = tk.Tk()
app = MIPSApplication(master = root)
app.mainloop()
