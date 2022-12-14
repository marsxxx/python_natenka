# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
result = open(argv[2],'w')

with open(argv[1]) as f:
    for line in f:
        if line.startswith('!') or ignore[0] in line or ignore[1] in line or ignore[2] in line:
            pass
        else:
            a = line.rstrip() + '\n'
            result.write(a)
result.close()