#!/usr/bin/env python3
vlan = input('Enter vlan: ')
interface = input('Enter interface: ')

template1 = ['interface {}',
            'switchport mode access',
            'switchport access vlan {}',
            'switchport nonegotiate',
            'spanning-tree portfast',
            'spanning-tree bpduguard enable']

print('\n' + '-' * 30)
print('\n'.join(template1).format(interface, vlan)) #с помощью join преобразуем список в строку, чтобы можно было использовать format