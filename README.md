# MIPS Simulator

## Introduction
The MIPS Simulator aims to provide a simple interface to allow MIPS programs to be tested on many platforms. The program is written in Python (v3.4) and has no further dependencies. An important thing to understand is that this program does not attempt to fully implement MIPS, but rather interprets a subset of MIPS instructions for quick testing.
To use this program, you must first have a valid MIPS program and the appropriate version of Python installed. Once these prerequisites are met, you may run the program through Python. You may then load a file as described in the next section, view the compiled machine code, and run the program.

## User Interface
The MIPS Simulator user interface has 5 main components that one must be familiar with. From left to right there is the control panel, the input display, the machine code display, the stack display, and the register display. While not a component, there is also a menu bar which is used to load input MIPS source code files through the File  Open dialog. Another options is provided in the File menu to allow users to close the simulator entirely through the File  Exit option.

### Control Panel:
The control panel allows you to set how the loaded program is running. It contains a slider which contains the updates performed per second when the program is left in running mode, a step button that allows a program to be stepped through line by line for closer inspection, a run button which freely runs the program, a stop button which ceases a program if it is in running mode, and finally a reset button that returns a loaded program to its default state (clears registers, reverts program counter to the first line of the program, etc.).

### Input Display:
The input display will always contain the input source code of the currently loaded program. This allows easy comparison between the machine code and input code, and helps to clarify what point a program is at in its execution. While a program is loaded, the next line to be run will be highlighted in the Input Display.

### Machine Code Display: 
The machine code display will show the binary representation of the source code loaded for a MIPS program. Comments and empty lines will be stripped out, and the line number shown in the Input Display are replaced with hexadecimal addresses that show the address of that instruction in program memory. While a program is loaded, the next line to be run will be highlighted in the Machine Code Display.

### Stack Display: 
The stack display shows any value in memory as it is stored in the stack of the loaded program. This display also indicates the value in the stack currently referenced by the stack pointer register ($sp). By default, the stack pointer is initialized to an arbitrary, high location in memory.

### Register Display: 
The register display will always show the data contained in the registers of a loaded program. In addition to the typically registers (numbered 0-31), it also displays the values contained in the $HI and $LO registers, which are used in multiplication and division.

## Limitations
Given that the MIPS simulator was designed to run a subset of MIPS, some features have been omitted. The results of loading a program with unsupported instructions are undefined. The features/instructions that are unsupported are as follows: unsigned operations are not permitted, floating point operations are not permitted.
Furthermore, the stack implemented by the simulator does not perfectly mimic a real-world stack. Rather than storing the program contents and the stack in the same contiguous portion of memory, the stack is allocated separately. While this does allow the same basic interactions normally seen with a stack, it does not have the ability to fail in all cases a real stack would. For example, the stack will never overflow as it has no hard limit on size, it merely depends on the memory of the machine the simulator is running on.
