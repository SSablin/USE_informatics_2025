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

# Крылов Вариант 12
"""В терминологии сетей ТСРДР маской сети называют двоичное число, которое
показывает, какая часть 1Р-адреса узла сети относится к адресу сети, а какая —
к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной
конъюнкции к заданному адресу узла и маске сети.
Сеть задана 1Р•адресом 191.239.130.3 и маской сети 255.255.A.0, где А — некоторое
допустимое для записи маски число. Определите минимальное значение А, для
которого для всех 1Р-адресов этой сети в двоичной записи 1Р-адреса суммарное
количество единиц в девых двух байтах не менее суммарного количества единиц
в правых двух байтах.
В ответе укажите только число."""
# Осипов Данила Сергеевич
"""from ipaddress import *

for x in range(16, 25):
    net = ip_network(f'191.239.130.3/{x}', 0)
    f = True
    for i in net:
        ip = bin(int(i))[2:]
        if ip[:16].count('1') >= ip[16:].count('1'):
            pass
        else:
            f = False
            break
    if f:
        print(int(f'{str(1) * (x - 16)}{str(0) * (8 - (x - 16))}', 2))
        print(net.netmask)  # 224
        break"""
# Ерофеев Ваня
"""from ipaddress import *

for x in range(16, 25):
    net = ip_network(f'191.239.130.3/{x}', 0)
    if all([bin(int(i))[2:][:16].count('1') >= bin(int(i))[2:][16:].count('1') for i in net]):
        print(x - 16)
        print(net.netmask)
        break"""
# DeepSeek
"""from ipaddress import *

# Перебираем возможные значения A (от 0 до 255)
for A in range(256):
    # Формируем маску сети
    mask = f'255.255.{A}.0'

    try:
        # Создаём сеть с заданным IP-адресом и маской
        net = IPv4Network(f'191.239.130.3/{mask}', strict=False)

        # Проверяем условие для всех IP-адресов сети
        condition_met = True
        for ip in net:
            # Преобразуем IP-адрес в 32-битное двоичное представление
            binary = ''.join(f'{byte:08b}' for byte in ip.packed)

            # Разделяем на левые и правые байты
            left_bytes = binary[:16]  # Первые два байта
            right_bytes = binary[16:]  # Последние два байта

            # Считаем количество единиц
            left_ones = left_bytes.count('1')
            right_ones = right_bytes.count('1')

            # Проверяем условие
            if left_ones < right_ones:
                condition_met = False
                break

        # Если условие выполнено для всех IP-адресов, выводим A и завершаем
        if condition_met:
            print(A)
            break
    except ValueError:
        # Пропускаем некорректные маски
        continue"""

# №18445 Сергей Горбачев
"""from ipaddress import *

k = 0
net = ip_network('140.116.194.0/255.255.240.0', 0)
for ip in net:
    b = f'{ip:b}'
    if b[7] == '0' and b[15] == '0' and b[23] == '0' and b[31] == '0':
        k += 1
        print(k, ip)
print(k)"""

# МЦКО 10 класс 2025
"""from ipaddress import *
c = 0
net = ip_network('192.168.112.170/255.255.255.224', 0)
for ip in net.hosts():
    c += 1
    if ip == ip_address('192.168.112.170'):
        print(c)
        break"""

# № 21747 (Уровень: Базовый)
"""from ipaddress import *

res = []
for mask in range(33):
    net = ip_network(f'84.23.84.23/{mask}', 0)
    if net.network_address == ip_address('84.23.84.0'):
        byte = [int(x) for x in str(net.netmask).split('.')]
        res.append([sum(byte[2:]), net.netmask])
print(max(res))  # 479"""
"""	

№ 22467

(Л. Шастин) В терминологии сетей TCP/IP маской сети называют двоичное число, 
которое показывает, какая часть IP-адреса узла сети относится к адресу сети, 
а какая – к адресу узла в этой сети. 
Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети. 
Широковещательным адресом называется специализированный адрес, в котором на месте нулей в маске стоят единицы. 
Адрес сети и широковещательный адрес не могут быть использованы для адресации сетевых устройств. 
Сеть определена неизвестным адресом сети и содержит в себе узел с IP-адресом 192.214.116.184. 
Известно, что в двоичной записи адреса этой сети содержится кратное 5 количество единиц. 
Сколько масок могут задавать такую сеть? В ответе укажите только число."""

# 13 №22467
from ipaddress import *

ip = ip_address('192.214.116.184')
c = 0
for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    b = f'{net[0]:b}'
    if b.count('1') % 5 == 0:
        if net[0] < ip < net[-1]:
            c += 1
print(c)  # 5
