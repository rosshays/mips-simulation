import mips_sim as mips
import tkinter as tk
from tkinter import filedialog

class MIPSApplication(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        # default configuration of window
        root.resizable(0,0)
        root.geometry("1400x800")
        root.wm_title("MIPS Simulation")

    def create_widgets(self):
        # create the menu bar used by the program
        self.menu = tk.Menu(self)
        root["menu"] = self.menu
        # create the file menu entry
        file_menu = tk.Menu(self.menu)
        file_menu.add_command(label = "Open", command = self.load_input_file)
        file_menu.add_command(label = "Exit", command = root.destroy)
        self.menu.add_cascade(menu = file_menu, label = "File")

        # create the text display for the compiled mips code and the input file
        self.input_text = tk.Text(self)
        self.bin_text = tk.Text(self)
        # configure the settings for the text areas
        self.input_text["background"] = "grey"
        self.bin_text["background"] = "grey"
        self.input_text["state"] = "disabled"
        self.bin_text["state"] = "disabled"

        # create the control panel
        self.control_panel = tk.Frame(self, width=400, height=800)
        button_panel = tk.Frame(self.control_panel)

        # create the simulation speed slider
        self.speed_slider = tk.Scale(self.control_panel, orient="horizontal")
        self.speed_slider["from"] = 1
        self.speed_slider["to"] = 60
        # create the buttons for step, run, stop
        self.step_button = tk.Button(button_panel, text="Step", command=self.step_once)
        self.run_button = tk.Button(button_panel, text="Run")
        self.stop_button = tk.Button(button_panel, text="Stop")

        # Layout everything the way it should be
        self.grid(column = 0, row = 0)
        self.control_panel.grid(column = 1, row = 0)
        self.input_text.grid(column = 10, row = 0)
        self.bin_text.grid(column = 15, row = 0)

        # arrange the control panel
        self.speed_slider.grid(column=0, row=0)
        button_panel.grid(column=0,row=1, columnspan=3)
        self.step_button.grid(column=0, row=1)
        self.run_button.grid(column = 1, row = 1)
        self.stop_button.grid(column = 2, row = 1)

    def step_once(self):
        print("hey")

    def load_input_file(self):
        filename = tk.filedialog.askopenfilename()
        if filename == "": return

        # allow editing on our text fields and wipe them
        self.input_text["state"] = "normal"
        self.bin_text["state"] = "normal"
        self.input_text.delete("1.0", "end")
        self.bin_text.delete("1.0", "end")

        # create a list to contain the lines (used later for the simulation)
        lines = []

        # iterate through all the lines in filename
        with open(filename) as f:
            for line in f:
                self.input_text.insert("end", line)
                lines.append(line)
        
        # create a new program for the mips simulation
        self.program = mips.Program(lines)

        # now we need to get the converted form of the input text from progam
        for line in self.program.machine_code:
            self.bin_text.insert("end", line)
            self.bin_text.insert("end", "\n")

        # lock the text fields again so they are not altered
        self.input_text["state"] = "disabled"
        self.bin_text["state"] = "disabled"

root = tk.Tk()
app = MIPSApplication(master = root)
app.mainloop()