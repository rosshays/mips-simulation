# Adds integers 0 to 10
# (Correct result is $s2 = 55)
addi $s0, $zero, 10
addi $s1, $zero, 1
addi $s2, $zero, 0

loopstart: 
	bltz $s0, endloop
	add $s2, $s2, $s0
	sub $s0, $s0, $s1
	j loopstart
endloop:
