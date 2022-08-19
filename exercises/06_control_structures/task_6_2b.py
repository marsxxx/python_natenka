# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
work = False #переменная означающая, что скрипт можно выполнять дальше
while (work == False):
    ip = input("Введите ip-адрес в формате Х.Х.Х.Х: ")
    octets = ip.split(".")  #разделили ip на октеты

    if len(octets)<4 or len(octets)>4:
        print ("Неправильный IP-адрес")
    else:
        work = True
        try:
            for i in range(4):
                octets[i]=int(octets[i])
        except ValueError:
            print("Неправильный IP-адрес")
            work = False
        if work == True:    #если прошлые проверки не прервали скрипт
                for i in range(4):
                    if 0<=octets[i]<=255:
                        pass    #если октет в диапазоне - ничего не делаем
                    else:
                        print ("Неправильный IP-адрес")
                        work = False
                        break   #перываем скрипт если значение не в диапазоне

if work == True: #если прошлые проверки не прервали скрипт
    if octets[0] > 0 and octets[0] < 224:
        print ("unicast")

    elif octets[0] > 223 and octets[0] < 240:
        print ("multicast")

    elif octets[0] == 255 and octets[1] == 255 and octets[2] == 255 and octets[3] == 255:
        print ("local broadcast")

    elif octets[0] == 0 and octets[1] == 0 and octets[2] == 0 and octets[3] == 0:
        print ("unassigned")

    else: print("unused")
else: pass