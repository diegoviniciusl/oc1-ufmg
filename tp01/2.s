#Funcao para calcular se o numero e primo
Prime:
	addi x5, x0, 1
	ble x10, x5, ReturnFalse
    addi x6, x0, 2
    Loop:
    	bge x6, x10, ReturnTrue
    	rem x7, x10, x6
        beq x7, x0, ReturnFalse
        addi x6, x6, 1
        jal x0, Loop

#Funcao para definir o retorno como verdadeiro (1)
ReturnTrue:
	addi x10, x0, 1
    jal x0, Exit

#Funcao para definir o retorno como falso (0)
ReturnFalse:
	add x10, x0, x0
    jal x0, Exit

Exit:
