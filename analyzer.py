# This function define if the word is a function or a variable
def varfunc(cc):
    while cc and (cc not in [' ', ';', ')', '(', '=', '!', '<', '>', '+', '-', '/', '%', '*', '\n']):
        cc = arq.read(1)
    if cc == '(':
        tokens['func'] += 1
    else:
        tokens['var'] += 1
    if cc in ['=', '!', '<', '>']:
        attrbcomp(cc)
    if cc in ['+', '-', '*', '/', '%']:
        operators(cc)

# This is a assessor function to analyse operators
# Also check if exists a number, char, string or variable after the operator
def operators(cc):
    a = 0
    if cc == '+':
        while cc in ['+', '=']:
            cc = arq.read(1)
            if cc in ['+', '=']:
                operations['increment'] += 1
                a = 1
        if a != 1:
            operations['sum'] += 1
    elif cc == '-':
        while cc in ['-', '=']:
            cc = arq.read(1)
            if cc in ['-', '=']:
                operations['decrement'] += 1
                a = 1
        if a != 1:
            operations['sub'] += 1
    elif cc == '/':
        while cc in ['/', '=']:
            cc = arq.read(1)
        operations['div'] += 1
    elif cc == '*':
        while cc in ['*', '=']:
            cc = arq.read(1)
        operations['mult'] += 1
    elif cc == '%':
        while cc in ['%', '=']:
            cc = arq.read(1)
        operations['mod'] += 1
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
        return
    if cc == "'":
        cc = arq.read(1)
        while cc and cc is not "'":
            cc = arq.read(1)
        tokens['char'] += 1
        return
    if cc == '"':
        cc = arq.read(1)
        while cc and cc is not '"':
            cc = arq.read(1)
        tokens['string'] += 1
        return
    if cc not in [' ', '\t', '\n', ')', '(', '{', '}', ';']:
        varfunc(cc)

# This is a assessor function to analyse attributors and comparators
# Also check if exists a number, char, string or variable after the attributor or comparator
def attrbcomp(cc):
    if cc == '>':
        cc = arq.read(1)
        if cc == '=':
            tokens['GE'] += 1
            return
        else:
            tokens['GT'] += 1
    elif cc == '<':
        cc = arq.read(1)
        if cc == '=':
            tokens['LE'] += 1
            return
        else:
            tokens['LT'] += 1
    elif cc == '!':
        cc = arq.read(1)
        if cc == '=':
            tokens['NE'] += 1
            return
    elif cc == '=':
        cc = arq.read(1)
        if cc == '=':
            tokens['EQ'] += 1
            return
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
        return
    if cc == "'":
        cc = arq.read(1)
        while cc and cc is not "'":
            cc = arq.read(1)
        tokens['char'] += 1
        return
    if cc == '"':
        cc = arq.read(1)
        while cc and cc is not '"':
            cc = arq.read(1)
        tokens['string'] += 1
        return
    if cc not in [' ', '\t', '\n']:
        varfunc(cc)


# This is a function to analyse the variables types
def typescanner(cc, type):
    if type == 1:
        cc = arq.read(1)
        while cc and cc not in [' ', ';', ')', '(', '=', '!', '<', '>']:
            cc = arq.read(1)
        vars['int'] += 1
    if type == 2:
        cc = arq.read(1)
        while cc and cc not in [' ', ';', ')', '(', '=', '!', '<', '>']:
            cc = arq.read(1)
        vars['char'] += 1
    if type == 3:
        cc = arq.read(1)
        while cc and cc not in [' ', ';', ')', '(', '=', '!', '<', '>']:
            cc = arq.read(1)
        vars['float'] += 1


arq = open('program.c')

# Tokens list
tokens = {'if': 0, 'else': 0, 'for': 0, 'while': 0, 'do': 0, 'switch': 0, 'case': 0, 'var': 0,
          'func': 0, 'char': 0, 'string': 0, 'num': 0, 'ATR': 0, 'LT': 0, 'LE': 0, 'EQ': 0, 'NE': 0, 'GT': 0, 'GE': 0}

# Numbers list
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Vars types list
vars = {'int': 0, 'char': 0, 'float': 0}

# Operators list
operations = {'sum': 0, 'sub': 0, 'div': 0, 'mult': 0, 'mod': 0, 'increment': 0, 'decrement': 0}

# Read de first character
c = arq.read(1)
while c:
    if c in ['(', ')', ';', '{', '}', ' ', '\n', '\t']:
        pass
    # If the line is a include, comment or the main, pass
    elif c == '#':
        while c and c != '\n':
            c = arq.read(1)
    elif c == "/":
        c = arq.read(1)
        if c == "/":
            while c and c != '\n':
                c = arq.read(1)
    elif c == 'v':
        c = arq.read(1)
        if c == 'o':
            c = arq.read(1)
            if c == 'i':
                c = arq.read(1)
                if c == 'd':
                    c = arq.read(1)
                    if c == ' ':
                        pass
                else:
                    varfunc(c)
            else:
                varfunc(c)
        else:
            varfunc(c)
    elif c == 'm':
        c = arq.read(1)
        if c == 'a':
            c = arq.read(1)
            if c == "i":
                c = arq.read(1)
                if c == 'n':
                    c = arq.read(1)
                    if c in [' ', '(']:
                        while c and c != "{":
                            c = arq.read(1)
                    else:
                        varfunc(c)
                else:
                    varfunc(c)
            else:
                varfunc(c)
        else:
            varfunc(c)
    # This is the blocks to analyse keywords such as if, for, while, etc
    # If the word isn't a keyword, call the function to analyse variables and functions
    elif c == 'i':
        c = arq.read(1)
        if c == 'f':
            c = arq.read(1)
            if c in [' ', '(']:
                tokens['if'] += 1
            # Starts with "if", but isn't if
            else:
                varfunc(c)
        # Starts with "i", but is a "int" variable
        elif c == 'n':
            c = arq.read(1)
            if c == 't':
                c = arq.read(1)
                if c == ' ':
                    typescanner(c, 1)
                else:
                    varfunc(c)
            else:
                varfunc(c)
        # Starts with "i", but isn't "if" or "int"
        else:
            varfunc(c)
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
                        varfunc(c)
                else:
                    varfunc(c)
            else:
                varfunc(c)
        else:
            varfunc(c)
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
                            varfunc(c)
                    else:
                        varfunc(c)
                else:
                    varfunc(c)
            else:
                varfunc(c)
        else:
            varfunc(c)
    elif c == 'd':
        c = arq.read(1)
        if c == 'o':
            c = arq.read(1)
            if c in [' ', '{']:
                tokens['do'] += 1
            else:
                varfunc(c)
        else:
            varfunc(c)
    elif c == 'f':
        c = arq.read(1)
        if c == 'o':
            c = arq.read(1)
            if c == 'r':
                c = arq.read(1)
                if c in [' ', '(']:
                    tokens['for'] += 1
                else:
                    varfunc(c)
            else:
                varfunc(c)
        elif c == 'l':
            c = arq.read(1)
            if c == 'o':
                c = arq.read(1)
                if c == 'a':
                    c = arq.read(1)
                    if c == 't':
                        c = arq.read(1)
                        if c == ' ':
                            typescanner(c, 3)
                        else:
                            varfunc(c)
                    else:
                        varfunc(c)
                else:
                    varfunc(c)
            else:
                varfunc(c)
        else:
            varfunc(c)
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
                                varfunc(c)
                        else:
                            varfunc(c)
                    else:
                        varfunc(c)
                else:
                    varfunc(c)
            else:
                varfunc(c)
        else:
            varfunc(c)
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
                        varfunc(c)
                else:
                    varfunc(c)
            else:
                varfunc(c)
        elif c == 'h':
            c = arq.read(1)
            if c == 'a':
                c = arq.read(1)
                if c == 'r':
                    c = arq.read(1)
                    if c == ' ':
                        typescanner(c, 2)
                    else:
                        varfunc(c)
                else:
                    varfunc(c)
            else:
                varfunc(c)
        else:
            varfunc(c)
    # The character is an operator
    elif c in ['-', '+', '/', '*', '%']:
        operators(c)
    # The character is a attributor, comparator, ' or "
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
        varfunc(c)
    c = arq.read(1)
print(tokens)
print(vars)
print(operations)
