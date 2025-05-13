# https://kompege.ru/variant?kim=25099988
# 24
"""from re import *
s = open('files/24_горбачев7.txt').readline()
numb = r'(?:0|[1-6][0-6]*)'
reg = rf'{numb}(\+{numb})*(\*{numb})*'
reg = rf'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m))  # 37
print(m)"""
