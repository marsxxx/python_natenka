# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#f = open ('ospf.txt', 'r+')
#print(f.read())
#['O', '10.0.24.0/24', '[110/41]', 'via', '10.0.13.3,', '3d18h,', 'FastEthernet0/0']

with open('ospf.txt') as f:
    for line in f:

        new_line = line.split()
        prefix = new_line[1]
        metric = new_line[2].replace(']','').replace('[','')
        next_hop = new_line[4].replace(',','')
        last_update = new_line[5].replace(',','')
        interface = new_line[6]

        #print (new_line)
        print('{:22}{}'.format("Prefix", prefix))
        print('{:22}{}'.format("AD/Metric", metric))
        print('{:22}{}'.format("Next-Hop", next_hop))
        print('{:22}{}'.format("Last update", last_update))
        print('{:22}{}'.format("Outbound Interface", interface))
