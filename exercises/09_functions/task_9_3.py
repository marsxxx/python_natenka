# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

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
            elif 'access vlan' in stroka:   #а если строка про access vlan, то
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

get_int_vlan_map("config_sw1.txt")      #вызов функции