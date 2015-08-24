#!/usr/bin/env python

import re

# http://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression
prog = re.compile(r'M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

numeral = raw_input()

if numeral == 'MMMM':
    print 'False'
else:
    result = prog.match(numeral)

    if result:
        print 'True'
    else:
        print 'False'
