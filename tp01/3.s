.data
array: .word 27, 16, 20, 49, 39, 48, 38, 7, 5, 19

.text
Main:
    beq x10, x0, SetArrayPosition #Definindo a primeira posicao do array caso ele nao seja enviado no registrador x10
    beq x11, x0, SetArraySize #Definindo o tamanho do array como 10 caso ele nao seja enviado no registrador x11
    jal x0, InsertionSort
    
SetArrayPosition:
	la x10, array
    
SetArraySize:
	addi x11, x0, 10
    
#Funcao de insertion sort
InsertionSort:
    addi x5, x0, 1 #x5 = 1, que e o valor de i
	#Primeiro Loop (for)
    FirstLoop:
    	#Armazenando arr[i] na key (x28), e criando j (x6) como i (x5) - 1
        slli x6, x5, 2
        add x7, x10, x6
        lw x28, 0(x7)
        addi x6, x5, -1
        #Armazenando arr[j] em x29
        slli x7, x6, 2
        add x7, x10, x7
        lw x29, 0(x7)
        #Validando as condicoes do while antes de entrar no while
        blt x6, x0, JumpLoop #Saindo do loop
        bge x28, x29, JumpLoop #Saindo do loop
        #Segundo Loop (while)
        SecondLoop:
        	#Atualizando arr[j + 1] com arr[j] e decrescendo j
            sw x29, 4(x7)
            addi x6, x6, -1
            slli x7, x6, 2
            add x7, x10, x7
            lw x29, 0(x7)
            #Validando as condicoes do while
            blt x6, x0, JumpLoop #Saindo do loop
            bge x28, x29, JumpLoop #Saindo do loop
            jal x0, SecondLoop #Voltando para o segundo loop (while) caso a condição ainda seja verdadeira
        #Funcao para armazenar em arr[j + 1] o valor da key (x28)
        JumpLoop:
            sw x28, 4(x7)
            addi x5, x5, 1
            blt x5, x11, FirstLoop #Voltando para o primeiro loop (for) caso a condição ainda seja verdadeira