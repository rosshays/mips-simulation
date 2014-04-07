# USES 4 SPACES FOR INDENTATION
import mips_sim as mips
import tkinter as tk
import interface as ui
import load_file as lf
import instruction as ins
from tkinter import filedialog


class MIPSApplication(tk.Frame):

	def __init__(self, master = None):
		ui.initialize(self, master, root)

	def create_widgets(self):
		ui.create_menu(self, root)
		
		self.grid(column = 0, row = 0)
		
		ui.create_text_boxes(self)
		ui.lock_text(self)
		ui.create_control(self)

	def step_once(self):
		print(">Stepping once")
		self.reset_button["state"] = "normal"
		if(len(self.program.instructions) != 0):
			inst = self.program.instructions.pop(0)
			inst.execute()
		ui.unlock_text(self)
		ui.update_stack(self)
		ui.update_registers(self)
		ui.lock_text(self)
	
	def run_prog(self):
		print(">Running program")
		self.stop_button["state"] = "normal"
		self.reset_button["state"] = "normal"
		for inst in self.program.instructions:
			inst.execute()
			ui.unlock_text(self)
			ui.update_stack(self)
			ui.update_registers(self)
			ui.lock_text(self)
		
	def stop_prog(self):
		print(">Stopping program")
		self.stop_button["state"] = "disabled"
		
	def reset(self):
		print(">Resetting simulator")
		self.reset_button["state"] = "disabled"
		self.stop_button["state"] = "disabled"

	def load_input_file(self):
		filename = lf.get_file(self)
		lines = lf.get_lines(self, filename)
		self.program = mips.Program(lines)
		ui.unlock_text(self)
		ui.update_bin(self)
		ui.update_stack(self)
		ui.update_registers(self)
		ui.lock_text(self)
		self.step_button["state"] = "normal"
		self.run_button["state"] = "normal"


root = tk.Tk()
app = MIPSApplication(master = root)
app.mainloop()
