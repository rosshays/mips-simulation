# Fun with the stack!!
addi $s0, $zero, 5
addi $s1, $zero, 7
add $s2, $zero, $sp
addi $s3, $zero, 0

addi $sp, $sp, -4
sw $s0, 0($sp)
loopstart1:
	beq $zero, $s1, endloop1
	add $s0, $s0, $s1
	addi $sp, $sp, -4
	sw $s0, 0($sp)
	addi $s1, $s1, -1
	j loopstart1
endloop1:
loopstart2:
	beq $sp, $s2, endloop2
	lw $s1, 0($sp)
	addi $sp, $sp, 4
	add $s3, $s3, $s1
	j loopstart2
endloop2:
