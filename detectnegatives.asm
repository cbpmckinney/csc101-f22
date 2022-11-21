; Load $FE into memory, check whether it is negative or not
; If negative, put #01 in $FF, otherwise put #00 in $FF
; 1000 0000
; 1111 1011
; AND our number against 1000 0000, we get exactly two possible answers
; 1000 0000 or 0000 0000

00  11FE    LDR R1, $FE
02  2280    MOV R2, #80
04  8321    AND R3, R2, R1
06  4020    CPY R2, R0 ; or, do MOV R0,#00
08  B30E    BEQ R3, isnegative

notnegative:
0A  2400    MOV R4, #00
0C  B010    BEQ R0, end

isnegative:
0E  2401    MOV R4, #01
end:
10  34FF    STR R4, $FF
12  C000    HLT    

old version: 11FE228083214020B310240034FFC000240134FFC000
new version: 11FE228083214020B30E2400B010240134FFC000


