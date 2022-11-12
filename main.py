import sys
import validateVariable as validvar

# Tuple keyword di JavaScript
js_grammar = ('break', 'const', 'case', 'catch', 'continue', 'default', 'delete', 'else', 'false', 'finally',
              'for', 'function', 'if', 'let', 'null', 'return', 'switch', 'throw', 'try', 'true', 'var', 'while')
js_compareOp = ('==', '===', '!=', '!==', '>', '<', '>=', '<=', '?')
js_assignLogicOp = ('&&=', '||=', '??=')
js_logicOp = ('&&', '||', '!')
js_assignBitwiseOp = ('<<=', '>>=', '>>>=', '&=', '^=', '|=')
js_bitwiseOp = ('&', '|', '~', '^', '<<', '>>', '>>>')
js_assignArithOp = ('=', '+=', '-=', '*=', '/=', '%=', '**=')
js_arithOp = ('+', '-', '*', '**', '/', '%', '++', '--')
js_symbol = (';', ',')
js_brackets = ('(', ')', '{', '}')
replacedsymbol = ('_comment_', '_arith_', '_assign_', '_compare_', '_logic_', '_bitwise_',
                  '_commonOpen_', '_commonClose_', '_curlyOpen_', '_curlyClose_', '_number_', '_variable_')


def beingReadyToCheck(file):
    # Mengubah multiline comments menjadi _next_
    found = True
    while (found):
        idxMultiOpen = file.find('/*')
        if (idxMultiOpen != -1):
            idxMultiClose = file.find('*/')
            file = file.replace(
                file[idxMultiOpen:idxMultiClose+2], "_comment_")
        else:
            found = False

    # Mengubah singleline comments menjadi _next_
    found = True
    while (found):
        idxSingle = file.find('//')
        if (idxSingle != -1):
            idxSingleClose = file.find('\n', idxSingle+1)
            file = file.replace(file[idxSingle:idxSingleClose], "_comment_")
        else:
            found = False

    # Mengganti newline dengan string kosong
    file = file.replace('\n', ' ')

    # Mengubah bracket
    for brackets in js_brackets:
        if (brackets == '('):
            file = file.replace(brackets, ' _commonOpen_ ')
        if (brackets == ')'):
            file = file.replace(brackets, ' _commonClose_ ')
        if (brackets == '{'):
            file = file.replace(brackets, ' _curlyOpen_ ')
        if (brackets == '}'):
            file = file.replace(brackets, ' _curlyClose_ ')

    # Mengubah keyword operator
    for operator in js_compareOp:
        file = file.replace(operator, ' _compare_ ')
    for operator in js_assignLogicOp:
        file = file.replace(operator, ' _assign_ ')
    for operator in js_logicOp:
        file = file.replace(operator, ' _logic_ ')
    for operator in js_assignBitwiseOp:
        file = file.replace(operator, ' _assign_ ')
    for operator in js_bitwiseOp:
        file = file.replace(operator, ' _bitwise_ ')
    for operator in js_assignArithOp:
        file = file.replace(operator, ' _assign_ ')
    for operator in js_arithOp:
        file = file.replace(operator, ' _arith_ ')

    # Mengubah keyword number
    ''' BELOM NIH '''

    # Mengubah isi file menjadi array of word
    if (file != ''):
        arrayOfWord = file.split()

    # Mengubah kata yang tidak ada dalam keyword menjadi _variable_
    file_ready = validvar.isVariable(arrayOfWord, replacedsymbol, js_grammar)

    return file_ready

# PROGRAM UTAMA


# Membuka file Node.js
fileName = sys.argv[1]
dir = 'test/' + str(fileName)
file = open(dir, "r")
file = str(file.read())

# Mulai proses parsing
readyFile = beingReadyToCheck(file)
print(readyFile)
