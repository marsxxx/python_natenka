# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

mode = input("Введите режим работы интерфейса (access/trunk): ")
inter = input("Введите тип и номер интерфейса: ")

askaccess = "Введите номер VLAN: "
asktrunk = "Введите разрешенные VLANы: "

askvlan = { #создали словарь для вопросов о вводе, в зависимости от выбранного мода
    "access": askaccess,
    "trunk": asktrunk
}

vlan = input(askvlan[mode]) #

access = "\n".join(access_template) #преобразовали список в строку
trunk = "\n".join(trunk_template)

modes = {   #создали словари, для вариантов вывода в зависимости от ввода
    "access": access,
    "trunk": trunk
}

print("interface {}".format(inter))
print (modes[mode].format(vlan))    #вывели список из словоря по вводу пользователя и подставили vlan