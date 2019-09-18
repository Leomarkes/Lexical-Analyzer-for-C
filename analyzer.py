arq = open('programa.c')

tokens = {'if': 0, 'else': 0, 'for': 0, 'while': 0, 'do': 0, 'switch': 0, 'case': 0, 'var': 0,
          'func': 0, 'num': 0, 'ATR': 0, 'LT': 0, 'LE': 0, 'EQ': 0, 'NE': 0, 'GT': 0, 'GE': 0}

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

c = arq.read(1)
while c:
    if c in ['(', ')', ';', '{', '}', ' ', '\n', '\t']:
        pass
    elif c == 'i':
        c = arq.read(1)
        if c == 'f':
            c = arq.read(1)
            if c in [' ', '(']:
                tokens['if'] += 1
            else:
                while c and (c not in [' ', ';', ')', '(']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
        else:
            while c and (c not in [' ', ';', ')', '(']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
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
                            while c and (c not in [' ', ';', ')', '(']):
                                c = arq.read(1)
                            if c == '(':
                                tokens['func'] += 1
                            else:
                                tokens['var'] += 1
                    else:
                        while c and (c not in [' ', ';', ')', '(']):
                            c = arq.read(1)
                        if c == '(':
                            tokens['func'] += 1
                        else:
                            tokens['var'] += 1
                else:
                    while c and (c not in [' ', ';', ')', '(']):
                        c = arq.read(1)
                    if c == '(':
                        tokens['func'] += 1
                    else:
                        tokens['var'] += 1
            else:
                while c and (c not in [' ', ';', ')', '(']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
        else:
            while c and (c not in [' ', ';', ')', '(']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
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
                        while c and (c not in [' ', ';', ')', '(']):
                            c = arq.read(1)
                        if c == '(':
                            tokens['func'] += 1
                        else:
                            tokens['var'] += 1
                else:
                    while c and (c not in [' ', ';', ')', '(']):
                        c = arq.read(1)
                    if c == '(':
                        tokens['func'] += 1
                    else:
                        tokens['var'] += 1
            else:
                while c and (c not in [' ', ';', ')', '(']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
        else:
            while c and (c not in [' ', ';', ')', '(']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
    elif c == 'f':
        c = arq.read(1)
        if c == 'o':
            c = arq.read(1)
            if c == 'r':
                c = arq.read(1)
                if c in [' ', '(']:
                    tokens['for'] += 1
                else:
                    while c and (c not in [' ', ';', ')', '(']):
                        c = arq.read(1)
                    if c == '(':
                        tokens['func'] += 1
                    else:
                        tokens['var'] += 1
            else:
                while c and (c not in [' ', ';', ')', '(']):
                    c = arq.read(1)
                if c == '(':
                    tokens['func'] += 1
                else:
                    tokens['var'] += 1
        else:
            while c and (c not in [' ', ';', ')', '(']):
                c = arq.read(1)
            if c == '(':
                tokens['func'] += 1
            else:
                tokens['var'] += 1
    elif c == '>':
        c = arq.read(1)
        if c == '=':
            tokens['GE'] += 1
        else:
            tokens['GT'] += 1
    elif c == '<':
        c = arq.read(1)
        if c == '=':
            tokens['LE'] += 1
        else:
            tokens['LT'] += 1
    elif c == '!':
        c = arq.read(1)
        if c == '=':
            tokens['NE'] += 1
    elif c == '=':
        c = arq.read(1)
        if c == '=':
            tokens['EQ'] += 1
        else:
            tokens['ATR'] += 1
    elif c in digits:
        c = arq.read(1)
        while c in digits:
            c = arq.read(1)
        if c == '.':
            c = arq.read(1)
            while c in digits:
                c = arq.read(1)
            tokens['num'] += 1
        if c in [' ', '\n',  ';'] or not c:
            tokens['num'] += 1
    else:
        while c and (c not in [' ', ';', ')', '(']):
            c = arq.read(1)
        if c == '(':
            tokens['func'] += 1
        else:
            tokens['var'] += 1
    c = arq.read(1)
print(tokens)
