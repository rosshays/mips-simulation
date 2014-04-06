import mips_sim as mips
import tkinter as tk
import interface as ui
import load_file as lf
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
        ui.update_stack(self)
        ui.update_registers(self)
    
    def run_prog(self):
        print(">Running program")
        ui.update_stack(self)
        ui.update_registers(self)
		
    def stop_prog(self):
	    print(">Stopping program")
	    
    def reset(self):
        print(">Resetting simulator")

    def load_input_file(self):
        filename = lf.get_file(self)
        lines = lf.get_lines(self, filename)
        self.program = mips.Program(lines)
        ui.update_bin(self)
        ui.update_stack(self)
        ui.update_registers(self)
        ui.lock_text(self)


root = tk.Tk()
app = MIPSApplication(master = root)
app.mainloop()
