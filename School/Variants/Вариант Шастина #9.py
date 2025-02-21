# 2
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (not((not x) or y) or (y == z) or (not w))
#                 if not f:
#                     print(x, y, z, w, f)
# 0 0 1 1 False
# 0 1 0 1 False
# 1 1 0 1 False
# wzyx

# 5
"""r_mx = 0
for i in range(500):
    n = oct(i)[2:]
    if int(n) % 2 == 0:
        for num in '1357':
            n = n.replace(num, '2')
    else:
        n = n.replace(n[0], '3').replace(n[-1], '3')
    r = int(n, 8)
    if r < 300:
        r_mx = max(r_mx, r)
print(r_mx)  # 294"""