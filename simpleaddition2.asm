;   init X = 5;
;   init Y = 3;
;   while Y not 0 do;
;       incr X;
;       decr Y;
;   end;

00  11FD    LDR R1, $FD
02  12FE    LDR R2, $FE
04  2301    MOV R3, #01
06  24FF    MOV R4, #FF
08  2000    MOV R0, #00

loop:
0A  B212    BEQ R2, finished
0C  5113    ADD R1, R1, R3  ; incr X
0E  5224    ADD R2, R2, R4  ; decr Y
10  B00A    BEQ R0, loop    ; unconditional branch gwahahahha

finished:
12  31FF    STR R1, $FF
14  C000    HLT

11FD12FE230124FF2000B21251135224B00A31FFC000