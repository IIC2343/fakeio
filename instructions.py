ADD =  r"^ADD\s+[aAbB],[aAbB]|\d+$"
SUB =  r"^SUB\s+[aAbB],[aAbB]|\d+$"
AND =  r"^AND\s+[aAbB],[aAbB]|\d+$"
OR =   r"^OR\s+[aAbB],[aAbB]|\d+$"
XOR =  r"^XOR\s+[aAbB],[aAbB]|\d+$"
NOT =  r"^NOT\s+[aA],[aAbB]$"
MOV =  r"^MOV\s+[aAbB],[aAbB]|\d+$|\([AAbB]\)$"
IN =   r"^IN\s+[aAbB],[aAbB]|\d+$"
OUT =  r"^OUT\s+[aAbB]|\d+,[aAbB]$"

REGEX = [ADD, SUB, AND, OR, XOR, NOT, MOV, IN, OUT]