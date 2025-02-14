# https://education.yandex.ru/ege/task/a257199f-ea64-4568-9f3c-b5c869a1bef9
"""Известно, что не широковещательный IP-адрес 137.219.220.63 принадлежит сети.
Какое максимальное количество единиц может быть в её маске?"""
"""from ipaddress import *

ip = ip_address('137.219.220.63')

for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    if ip != net[-1]:  # это не последний адрес сети (не широковещательный)
        print(mask)"""

# Вариант #7 Шастин
"""два узла, находящиеся в одной сети, имеют [Р-адреса 200.154.190.12 и 200.154.184.0. Укажите наибольшее
возможное количество единиц в маске этой сети. Учтите, что два адреса в любой подсети зарезервированы: адрес
всей подсети и широковещательный адрес."""

"""from ipaddress import *

ip = ip_address('200.154.190.12')

for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    if ip != net[-1] and ip_address('200.154.184.0') != net[-1]:
        print(mask)"""


# https://education.yandex.ru/ege/task/d1f1a287-0c17-4137-af60-9c544ea60589

"""from ipaddress import *

for mask in range(1, 33):
    net = ip_network(f'111.91.192.0/{mask}', 0)
    if ip_address('111.91.200.28') in net:
        print(32 - mask)  # 12"""


# 17632

"""from ipaddress import *

net = ip_network('112.160.0.0/255.240.0.0', 0)
c = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 5 == 0:
        c += 1
print(c)   # 215766"""
# 18955

"""from ipaddress import *
ip_1 = ip_address('200.154.190.12')
ip_2 = ip_address('200.154.184.0')
for mask in range(32, -1, -1):
    net1 = ip_network(f'200.154.190.12/{mask}', 0)
    net2 = ip_network(f'200.154.184.0/{mask}', 0)
    if net1 == net2 and ip_1 not in [net1[0], net1[-1]] and ip_2 not in [net1[0], net1[-1]]:
        print(mask)  # 20
        break"""

# 19748
"""from ipaddress import *

ip_1 = ip_address('157.220.185.237')
ip_2 = ip_address('157.220.184.230')
c = 0

for mask in range(32, -1, -1):
    if c > 0:
        print(c)  # 9
        break
    c = 0
    net1 = ip_network(f'{ip_1}/{mask}', 0)
    net2 = ip_network(f'{ip_2}/{mask}', 0)
    if net1 == net2 and ip_1 not in [net1[0], net1[-1]] and ip_2 not in [net1[0], net1[-1]]:
        for ip in net1:
            b = f'{ip:b}'
            if b.count('1') == 15:
                c += 1"""