#Funcao para calcular o OHM
OMH:
    beq x10, x0, Voltage
    beq x11, x0, Resistance
    beq x12, x0, Current

#Funcao para calcular a voltagem
Voltage:
    beq x11, x0, SetZero
    beq x12, x0, SetZero
    mul x10, x11, x12
    jal x0, Exit

#Funcao para calcular a resistencia
Resistance:
    beq x10, x0, SetZero
    beq x12, x0, SetZero
    div x10, x10, x12
    jal x0, Exit

#Funcao para calcular a corrente
Current:
    beq x10, x0, SetZero
    beq x11, x0, SetZero
    div x10, x10, x11
    jal x0, Exit

#Funcao para definir zero no registrador de retorno
SetZero:
    add x10, x0, x0
    jal x0, Exit

Exit: 

