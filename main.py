import sys
import globalVariable
import validVariable
import validNumber


def ReadyToParse(file):
    # Mengubah isi file menjadi array of sentence tiap baris
    file = file.split('\n')
    arr = []
    # Proses tiap baris mengubah multiline comments menjadi _comment_
    found = False
    for line in file:
        if (globalVariable.acc):
            # Mengubah semicolon menjadi _semicolon
            line = line.replace(';', ' _semicolon_')

            # Mengubah multiline comments menjadi _comment_
            idxMultiOpen = line.find('/*')
            if (idxMultiOpen != -1 or found):
                found = True
                idxMultiClose = line.find('*/')
                if (idxMultiClose == -1):
                    line = line.replace(line[0:], '_comment_')
                else:
                    line = line.replace(line[0:], '_comment_')
                    found = False
            else:  # idxMultiOpen == -1 and not found
                idxMultiClose = line.find('*/')
                if (idxMultiClose == -1):
                    found = False
                else:
                    globalVariable.acc = False

            # Mengubah singleline comments menjadi _comment_
            if (globalVariable.acc):
                idxSingle = line.find('//')
                if (idxSingle != -1):
                    line = line.replace(
                        line[0:], "_comment_")

            # Mengubah bracket
            for brackets in globalVariable.js_brackets:
                if (brackets == '('):
                    line = line.replace(brackets, ' _commonOpen_ ')
                if (brackets == ')'):
                    line = line.replace(brackets, ' _commonClose_')
                if (brackets == '{'):
                    line = line.replace(brackets, ' _curlyOpen_')
                if (brackets == '}'):
                    line = line.replace(brackets, ' _curlyClose_')
                if (brackets == '['):
                    line = line.replace(brackets, ' _squareOpen_')
                if (brackets == ']'):
                    line = line.replace(brackets, ' _squareClose_')

            # Mengubah keyword operator
            for operator in globalVariable.js_compareOp:
                line = line.replace(operator, ' _compare_')
            for operator in globalVariable.js_assignLogicOp:
                line = line.replace(operator, ' _assign_')
            for operator in globalVariable.js_logicOp:
                line = line.replace(operator, ' _logic_')
            for operator in globalVariable.js_assignBitwiseOp:
                line = line.replace(operator, ' _assign_')
            for operator in globalVariable.js_bitwiseOp:
                line = line.replace(operator, ' _bitwise_')
            for operator in globalVariable.js_assignArithOp:
                line = line.replace(operator, ' _assign_')
            for operator in globalVariable.js_arithOp:
                line = line.replace(operator, ' _arith_')

            # Mengubah tipe data
            # Mengubah keyword number menjadi '_string_'
            idxStringOpen = line.find("'")
            if (idxStringOpen != -1):
                idxStringClose = line.find("'", idxStringOpen+1)
                if (idxStringClose == -1):
                    globalVariable.acc = False
                else:
                    line = line.replace(
                        line[idxStringOpen:idxStringClose+1], ' _string_')
            else:  # idxstringOpen == -1
                idxStringClose = line.find("'")
                if (idxStringClose != -1):
                    globalVariable.acc = False

            idxStringOpen = line.find('"')
            if (idxStringOpen != -1):
                idxStringClose = line.find('"', idxStringOpen+1)
                if (idxStringClose == -1):
                    globalVariable.acc = False
                else:
                    line = line.replace(
                        line[idxStringOpen:idxStringClose+1], ' _string_')
            else:  # idxstringOpen == -1
                idxStringClose = line.find('"')
                if (idxStringClose != -1):
                    globalVariable.acc = False

            # Mengubah keyword object menjadi '_object_'
            # ''' BELOM NIH '''

            # Mengubah isi file menjadi array of array of word
            if (line != ''):
                line = line.split()

            # Mengubah keyword number menjadi '_number_'
            line = validNumber.isNumber(line)

            # Mengubah kata yang tidak ada dalam keyword menjadi _variable_
            if (globalVariable.acc):
                line = validVariable.isVariable(
                    line, globalVariable.replacedsymbol, globalVariable.js_grammar)

            arr.append(line)
            globalVariable.rowError += 1
    return arr


# PROGRAM UTAMA
# Splash screen
print()
print()
print("      ██╗ █████╗ ██╗   ██╗ █████╗ ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗  ")
print("      ██║██╔══██╗██║   ██║██╔══██╗██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝  ")
print("      ██║███████║██║   ██║███████║███████╗██║     ██████╔╝██║██████╔╝   ██║     ")
print(" ██   ██║██╔══██║╚██╗ ██╔╝██╔══██║╚════██║██║     ██╔══██╗██║██╔═══╝    ██║     ")
print(" ╚█████╔╝██║  ██║ ╚████╔╝ ██║  ██║███████║╚██████╗██║  ██║██║██║        ██║     ")
print("  ╚════╝ ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝     ")
print()
print("                              ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗   ")
print("                              ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗  ")
print("                              ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝  ")
print("                              ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗  ")
print("                              ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║  ")
print("                              ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝  ")
print()
print()

# Membuka file Node.js
fileName = sys.argv[1]
dir = 'test/' + str(fileName)
file = open(dir, "r")
file = str(file.read())

arrMain = ReadyToParse(file)

# Cek Expression



# Mulai proses parsing
'''
if (globalVariable.acc):
    arr_file = ReadyToParse(file)
    arr_file_ready = []
    for i in range(0, len(arr_file)):
        arr_file_ready += arr_file[i] + ['_newline_']
    globalVariable.acc, arr_file_parsed = CYK(
        CNFconverter("grammar.txt"), arr_file_ready)
    globalVariable.rowError = 0
    if (not(globalVariable.acc)):
        for word in arr_file_parsed:
            if (word == '_flag_'):
                break
            elif (word == '_newline_'):
                globalVariable.rowError += 1
'''

# Output program
if (globalVariable.acc):
    print("Accepted")
else:
    error = arr_file[globalVariable.rowError-1]
    error = error.replace(' ', '')
    print("Syntax Error")
    print("Terjadi kesalahan pada line " + str(globalVariable.rowError) +
          ' :"' + error + '"')
