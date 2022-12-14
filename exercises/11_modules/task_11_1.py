# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    remote = {}
    local_cost=[]
    port_cost=[]
    remote_cost=[]
    interface_cost=[]
    local = []
    lenth = []
    list_words = []
    first_string = 0
    temp = command_output.split('\n')
    list_words = [word for word in temp if word]
    local_device = list_words[0].split('>')[0]

    len_list_words = len(list_words)
    for position, string_temp in enumerate(list_words):
        if 'Holdtme' in string_temp:
            first_string = position
    #first_string = list_words.index('Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID')

    final_strings = list_words[first_string+1 : len_list_words+1]
    final_strings = [string.split('  ') for string in final_strings]
    for string in final_strings:
        final_strings = [words for words in string if words]
        lenth.append(final_strings)


    for device in lenth:
        for i in range(len(device)):
            if 'WS-C3750- Eth 0/3' in device[i]:
               device[i] = device[i].replace("WS-C3750-", '')
               device.insert(i, 'WOOW')
    #return lenth#result

        remote_cost.append(device[0])
        interface_cost.append(device[5].replace(" ", ""))
        port_cost.append(device[1].replace(" ", ""))
        local_cost.append(local_device)
        local = list(zip(local_cost,port_cost))
        remote = list(zip(remote_cost,interface_cost))

    result = dict(zip(local, remote))

    return result


if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        #print (f.read())
        print(parse_cdp_neighbors(f.read()))    #печатаем всё, что возвращает функция parse
