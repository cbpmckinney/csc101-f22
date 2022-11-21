; add two numbers by incrementing one of them
; and decrementing the other until the other 
; hits zero
; two inputs are in $FD and $FE
; store answer in $FF

00  11FD    LDR R1, $FD
02  12FE    LDR R2, $FE
04  2000    MOV R0, #00
06  2301    MOV R3, #01
08  24FF    MOV R4, #FF

loop:
0A  B212    BEQ R2, end
0C  5113    ADD R1, R1, R3  ;incr R1
0E  5224    ADD R2, R2, R4  ;decr R2
10  B00A    BEQ R0, loop

end:
12  31FF    STR R1, $FF
14  C000    HLT

11FD12FE2000230124FFB21251135224B00A31FFC000