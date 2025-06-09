# 24 №22448
from re import finditer
s = open('files/24_22448.txt').readline()
num_ch = r'[1-9]*[2468]'
num_nch = r'[1-9]*[13579]'
reg_ch = rf'([A-Z]+{num_ch})+[A-Z]+({num_ch}[A-Z]+)+'
reg_nch = rf'([A-Z]+{num_nch})+[A-Z]+({num_nch}[A-Z]+)+'
reg = rf'(?=({reg_ch}|{reg_nch}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(m)
print(len(m))  # 167

# 26 №22567
f = open('files/26_22567.txt')
n, r, v = map(int, f.readline().split())
# кол-во оазисов, расстояние от старта до конца, макс может пройти
# f = ('10 20', '19 9', '15 11', '40 20', '31 5', '41 10', '30 10')
# n, r, v = 7, 50, 20

data = [list(map(int, s.split())) for s in f]
data.sort()
# расстояние от начала до оазиса, запас воды
x = 0
fuel = v
k, mn_oasis = 0, float('inf')
while x + fuel < r:
    a = []
    for oasis in data:
        if x < oasis[0] <= x + fuel:
            l = oasis[0] - x
            potential_fuel = min(fuel - l + oasis[1], v)
            a.append([l + potential_fuel, oasis[0], oasis[1]])
            if oasis[0] + potential_fuel >= r:
                mn_oasis = min(oasis[0], mn_oasis)
                print(oasis)
    best_oasis = max(a)
    fuel = min(fuel - (best_oasis[1] - x) + best_oasis[2], v)
    x = best_oasis[1]
    k += 1
print(k, mn_oasis)
# 330 7939364
