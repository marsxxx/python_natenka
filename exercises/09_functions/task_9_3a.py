# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map (config_filename):     #функция при вызове будет ожидать конфигурационный файл, как аргумент

    access = {}     #словарь для интерфейсов в режиме access
    trunk = {}      #словарь для интерфейсов в режиме trunk

    with open(config_filename) as f:        #открываем файл для чтения
        config = f.read().split('\n')       #считываем весь файл в одну строку, разделяем её на строки по переносу строки и образуется список из строк конфига
        #print(config)
        for stroka in config:               #для каждой строки конфига
            if 'FastEthernet' in stroka:    #если это строка про порт, то
                port = stroka.replace('interface ','')      #запоминаем интерфейс
            elif 'mode access' in stroka:   #если встретился интерфейс с режимом access, то
               access[port] = 1             #сразу записываме его в словарь со значением влан 1
            elif 'access vlan' in stroka:   #а если встретилась строка про access vlan, то она перепишет значение этого порта в словаре
               access_str = stroka.split()          #запоминаем её и разделяем на список из слов
               access[port] = int(access_str[-1])   #в словарь access вносим запись с интерфейсом = vlan
            elif 'trunk allowed vlan' in stroka:    #а если строка про trunk vlan, то
                trunk_str = stroka.split('vlan ')   #отделяем все вланы
                trunk_str = trunk_str[-1].split(',')        #все вланы разделяем
                trunk_vlans = []            #заготовка списка для вланов как числа
                for vlan in trunk_str:      #каждый влан в списке
                    vlan_int=int(vlan)      #преобразуем в число
                    trunk_vlans.append(vlan_int)   #собираем всё в список
                trunk[port] = trunk_vlans   #в словарь trunk вносим запись с интерфейсом = vlans
        print (f'Ports in access mode {access}')    #для наглядности
        print (f'Ports in trunk mode {trunk}')      #для наглядности
    result = (access, trunk)            #добавляем словари в кортеж
    return (result)                     #функция возвращает кортеж из двух словарей
get_int_vlan_map("config_sw2.txt")      #вызов функции