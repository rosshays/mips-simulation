# Produces ten factorial
addi $s0, $zero, 10
addi $s1, $zero, 1
addi $s2, $zero, 1

loopstart:
	beq $zero, $s0, endloop
	mult $s2, $s0
	mflo $s2
	sub $s0, $s0, $s1
	j loopstart
endloop:
