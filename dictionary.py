# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import utils

args = sys.argv[1:]

if utils.dssize(args) == 0:
    print('Usage: dictionary [key] | dictionary --help | dictionary --version')
else:
    key = ' '.join(args)

    if key == '--version':
        version = '''dictionary (<<OS>>) 1.0
Copyright (C) 2015 Dássone Yotamo - ddd
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.'''

        print(version)
        exit()

    if key == '--help':
        help = '''Under construction.'''

        print(help)
        exit()

    fd = open('dic.cd', 'r')

    fflag =  False

    for x in fd:
       temp_str = x[:-1]

       if temp_str.lower() == key.lower(): # [:-1] because this string in \n-ended. lower() for being icase ...
            fflag = True
            print('Result found for: %s' % (temp_str,))
            break

    if not fflag:
        print('Results not found for: %s' % (key))
        fd.seek(0)

        c = 0

        for y in utils.get_keys(fd):
            if utils.analyze_str(key.lower(), y.lower()):
                print('Did you mean: %s?' % (y,))
    else:
        for x in fd:
            if x[0] == '\t' or x == '\n':
                print(x, end='')
            else:
                break

    fd.close()

