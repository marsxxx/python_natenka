#!/usr/bin/env python3
from sys import argv    #модуль работает с аргументами скрипта
name = argv[0]          #имя скрипта
vlan = argv[1]          #первый аргумент, который через пробел после запускаемого файла
interface = argv[2]     #второй аргумент
template1 = ['switchport mode access',
            'switchport access vlan {}',
            'switchport nonegotiate',
            'spanning-tree portfast',
            'spanning-tree bpduguard enable']
print('\nscript {}\n'.format(name))
print('\n'.join(template1).format(vlan))
print('interface {}'.format(interface))