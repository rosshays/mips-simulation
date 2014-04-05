import tkinter as tk

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
			self.input_text.insert("end", line)
			lines.append(line)
	
	return lines
