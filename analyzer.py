# Assessor function to analyse attributors and comparators
# if the whitespace between this characters and variables is missing
# also check if exists a number, char or string after the attributor or comparator
def attrbcomp(cc):
    if cc == '>':
        cc = arq.read(1)
        if cc == '=':
            tokens['GE'] += 1
        else:
            tokens['GT'] += 1
    elif cc == '<':
        cc = arq.read(1)
        if cc == '=':
            tokens['LE'] += 1
        else:
            tokens['LT'] += 1
    elif cc == '!':
        cc = arq.read(1)
        if cc == '=':
            tokens['NE'] += 1
    elif cc == '=':
        cc = arq.read(1)
        if cc == '=':
            tokens['EQ'] += 1
        else:
            tokens['ATR'] += 1
    if cc in digits:
        cc = arq.read(1)
        while cc in digits:
            cc = arq.read(1)
        if cc == '.':
            cc = arq.read(1)
            while cc in digits:
                cc = arq.read(1)
            tokens['num'] += 1
        if cc in [' ', '\n', ';'] or not cc:
            tokens['num'] += 1
    if cc == "'":
        cc = arq.read(1)
        while cc and cc is not "'":
            cc = arq.read(1)
        tokens['char'] += 1
    if cc == '"':
        cc = arq.read(1)
        while cc and cc is not '"':
            cc = arq.read(1)
        tokens['string'] += 1


arq = open('program.c')

# Tokens list
tokens = {'if': 0, 'else': 0, 'for': 0, 'while': 0, 'do': 0, 'switch': 0, 'case': 0, 'var': 0,
          'func': 0, 'char': 0, 'string': 0, 'num': 0, 'ATR': 0, 'LT': 0, 'LE': 0, 'EQ': 0, 'NE': 0, 'GT': 0, 'GE': 0}

# Numbers list
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Read de first character
c = arq.read(1)
while c:
    if c in ['(', ')', ';', '{', '}', ' ', '\n', '\t']:
        pass
    # block to analyse keywords such as if, for, while, etc and variables or function's calls
    elif c == 'i':
        c = arq.read(1)
        if c == 'f':
            c = arq.read(1)
            if c in [' ', '(']:
                tokens['if'] += 1
            # Starts with "if", but isn't if
            else:
                # Loop until find the final character of the variable or the function's call
                while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
                # If the character is a comparator or attributor, call the assessor function
                if c in ['=', '!', '<', '>']:
                    attrbcomp(c)
        # Starts with "i", but isn't if
        else:
            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
            if c in ['=', '!', '<', '>']:
                attrbcomp(c)
    elif c == 'e':
        c = arq.read(1)
        if c == 'l':
            c = arq.read(1)
            if c == 's':
                c = arq.read(1)
                if c == 'e':
                    c = arq.read(1)
                    if c in [' ', '(', '{', '\n', '\t']:
                        tokens['else'] += 1
                    else:
                        while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                            c = arq.read(1)
                        if c == '(':
                            tokens['func'] += 1
                        else:
                            tokens['var'] += 1
                        if c in ['=', '!', '<', '>']:
                            attrbcomp(c)
                else:
                    while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                        c = arq.read(1)
                    if c == '(':
                        tokens['func'] += 1
                    else:
                        tokens['var'] += 1
                    if c in ['=', '!', '<', '>']:
                        attrbcomp(c)
            else:
                while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
                if c in ['=', '!', '<', '>']:
                    attrbcomp(c)
        else:
            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
            if c in ['=', '!', '<', '>']:
                attrbcomp(c)
    elif c == 'w':
        c = arq.read(1)
        if c == 'h':
            c = arq.read(1)
            if c == 'i':
                c = arq.read(1)
                if c == 'l':
                    c = arq.read(1)
                    if c == 'e':
                        c = arq.read(1)
                        if c in [' ', '(']:
                            tokens['while'] += 1
                        else:
                            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                                c = arq.read(1)
                            if c == '(':
                                tokens['func'] += 1
                            else:
                                tokens['var'] += 1
                            if c in ['=', '!', '<', '>']:
                                attrbcomp(c)
                    else:
                        while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                            c = arq.read(1)
                        if c == '(':
                            tokens['func'] += 1
                        else:
                            tokens['var'] += 1
                        if c in ['=', '!', '<', '>']:
                            attrbcomp(c)
                else:
                    while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                        c = arq.read(1)
                    if c == '(':
                        tokens['func'] += 1
                    else:
                        tokens['var'] += 1
                    if c in ['=', '!', '<', '>']:
                        attrbcomp(c)
            else:
                while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
                if c in ['=', '!', '<', '>']:
                    attrbcomp(c)
        else:
            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
            if c in ['=', '!', '<', '>']:
                attrbcomp(c)
    elif c == 'd':
        c = arq.read(1)
        if c == 'o':
            c = arq.read(1)
            if c in [' ', '{']:
                tokens['do'] += 1
            else:
                while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
                if c in ['=', '!', '<', '>']:
                    attrbcomp(c)
        else:
            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
            if c in ['=', '!', '<', '>']:
                attrbcomp(c)
    elif c == 'f':
        c = arq.read(1)
        if c == 'o':
            c = arq.read(1)
            if c == 'r':
                c = arq.read(1)
                if c in [' ', '(']:
                    tokens['for'] += 1
                else:
                    while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                        c = arq.read(1)
                    if c == '(':
                        tokens['func'] += 1
                    else:
                        tokens['var'] += 1
                    if c in ['=', '!', '<', '>']:
                        attrbcomp(c)
            else:
                while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
                if c in ['=', '!', '<', '>']:
                    attrbcomp(c)
        else:
            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
            if c in ['=', '!', '<', '>']:
                attrbcomp(c)
    elif c == 's':
        c = arq.read(1)
        if c == 'w':
            c = arq.read(1)
            if c == 'i':
                c = arq.read(1)
                if c == 't':
                    c = arq.read(1)
                    if c == 'c':
                        c = arq.read(1)
                        if c == 'h':
                            c = arq.read(1)
                            if c in [' ', '(']:
                                tokens['switch'] += 1
                            else:
                                while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                                    c = arq.read(1)
                                if c == '(':
                                    tokens['func'] += 1
                                else:
                                    tokens['var'] += 1
                                if c in ['=', '!', '<', '>']:
                                    attrbcomp(c)
                        else:
                            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                                c = arq.read(1)
                            if c == '(':
                                tokens['func'] += 1
                            else:
                                tokens['var'] += 1
                            if c in ['=', '!', '<', '>']:
                                attrbcomp(c)
                    else:
                        while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                            c = arq.read(1)
                        if c == '(':
                            tokens['func'] += 1
                        else:
                            tokens['var'] += 1
                        if c in ['=', '!', '<', '>']:
                            attrbcomp(c)
                else:
                    while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                        c = arq.read(1)
                    if c == '(':
                        tokens['func'] += 1
                    else:
                        tokens['var'] += 1
                    if c in ['=', '!', '<', '>']:
                        attrbcomp(c)
            else:
                while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
                if c in ['=', '!', '<', '>']:
                    attrbcomp(c)
        else:
            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
            if c in ['=', '!', '<', '>']:
                attrbcomp(c)
    elif c == 'c':
        c = arq.read(1)
        if c == 'a':
            c = arq.read(1)
            if c == 's':
                c = arq.read(1)
                if c == 'e':
                    c = arq.read(1)
                    if c == ' ':
                        tokens['case'] += 1
                    else:
                        while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                            c = arq.read(1)
                        if c == '(':
                            tokens['func'] += 1
                        else:
                            tokens['var'] += 1
                        if c in ['=', '!', '<', '>']:
                            attrbcomp(c)
                else:
                    while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                        c = arq.read(1)
                    if c == '(':
                        tokens['func'] += 1
                    else:
                        tokens['var'] += 1
                    if c in ['=', '!', '<', '>']:
                        attrbcomp(c)
            else:
                while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
                if c in ['=', '!', '<', '>']:
                    attrbcomp(c)
        else:
            while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
            if c in ['=', '!', '<', '>']:
                attrbcomp(c)
    # when the whitespace between this characters and variables exists
    elif c in ['=', '!', '<', '>', '"', "'"]:
        attrbcomp(c)
    # block to analyse numbers
    elif c in digits:
        c = arq.read(1)
        while c in digits:
            c = arq.read(1)
        if c == '.':
            c = arq.read(1)
            while c in digits:
                c = arq.read(1)
            tokens['num'] += 1
        if c in [' ', '\n', ';', ')', '(', '=', '!', '<', '>', '"', "'"] or not c:
            tokens['num'] += 1
        if c in ['=', '!', '<', '>']:
            attrbcomp(c)
    else:
        while c and (c not in [' ', ';', ')', '(', '=', '!', '<', '>', '"', "'"]):
            c = arq.read(1)
        if c == '(':
            tokens['func'] += 1
        else:
            tokens['var'] += 1
        if c in ['=', '!', '<', '>', '"', "'"]:
            attrbcomp(c)
    c = arq.read(1)
print(tokens)
