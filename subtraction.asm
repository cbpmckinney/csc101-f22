;Assume that the two numbers are in $FD and $FE.
;We want to compute the difference.

11FD    LDR R1, $FD
12FE    LDR R2, $FE
23FF    LDR R3, #FF
2401    LDR R4, #01
9523    XOR R5, R2, R3
5545    ADD R5, R4, R5 ;R5 has the negative of R2
5615    ADD R6, R1, R5 ;Computes A + (-B)
36FF    STR R6, $FF
C000    HLT

11FD12FE23FF240195235545561536FFC000