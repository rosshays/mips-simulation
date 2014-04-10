# Use a procedure to get the sum of two numbers
# 2056 + 630 = 2686

# entry point of program
addi $s0, $zero, 2056
addi $s1, $zero, 630

# store in arguement registers
add $a0, $zero, $s0
add $a1, $zero, $s1

# make the function call
jal add_func

# move answer into $s2
add $s2, $zero, $t0

# prevent instruction from running again
j exit

# expects a number in $a0 and $a1
# result will be stored in $t0
add_func:	
add $t0, $a0, $a1
jr $ra
	
exit: