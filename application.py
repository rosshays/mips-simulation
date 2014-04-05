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
        ui.create_file(self, root)
        
        ui.create_input(self)
        ui.create_bin(self)
        ui.create_stack(self)
        ui.lock_text(self)
        
        button_panel = ui.create_control(self)
        
        ui.adjust_layout(self)
        ui.arrange_control(self, button_panel)

    def step_once(self):
        print(">Stepping once")
    
    def run_prog(self):
	    print(">Running program")
		
    def stop_prog(self):
	    print(">Stopping program")

    def load_input_file(self):
        filename = lf.get_file(self)
        lines = lf.get_lines(self, filename)
        self.program = mips.Program(lines)
        ui.update_bin(self)
        ui.lock_text(self)


root = tk.Tk()
app = MIPSApplication(master = root)
app.mainloop()
