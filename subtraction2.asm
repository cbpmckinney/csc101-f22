; Compute difference of $FD and $FE

11FD    LDR R1, $FD
12FE    LDR R2, $FE
2301    LDR R3, #01
24FF    LDR R4, #FF
9524    XOR R5, R2, R4
5553    ADD R5, R5, R3 ;Register 5 contains the negative of what's in Register 2
5615    ADD R6, R1, R5 ;This computes first number minus second number
36FF    STR R6, $FF
C000    HLT

11FD12FE230124FF95245553561536FFC000
