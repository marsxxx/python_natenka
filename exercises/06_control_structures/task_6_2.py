# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input("Введите ip-адрес в формате Х.Х.Х.Х: ")
octets = ip.split(".")

for i in range(4):
    octets[i]=int(octets[i])

if octets[0] > 0 and octets[0] < 224:
    print ("unicast")

elif octets[0] > 223 and octets[0] < 240:
    print ("multicast")

elif octets[0] == 255 and octets[1] == 255 and octets[2] == 255 and octets[3] == 255:
    print ("local broadcast")

elif octets[0] == 0 and octets[1] == 0 and octets[2] == 0 and octets[3] == 0:
    print ("unassigned")

else: print("unused")



#print (octets)