
;      1111 1001
;  AND 1000 0000
;      1000 0000

;      0000 0000
; ANDing a number against 10000000 gives either 00000000 or 10000000
;
; Load number from $FE, then if it's negative, put #01 in $FF; otherwise put #00 in $FF

00  11FE    LDR R1, $FE
02  2280    MOV R2, #80
04  8312    AND R3, R1, R2
06  4020    CPY R2, R0
08  B310    BEQ R3, isnegative

notnegative:
0A  2400    MOV R4, #00
0C  34FF    STR R4, $FF
0E  C000    HLT

isnegative:
10  2401    MOV R4, #01
12  34FF    STR R4, $FF
14  C000    HLT

11FE228083124020B310240034FFC000240134FFC000
