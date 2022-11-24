import sys
import globalVariable
import validVariable


def ReadyToParse(file):
    # Mengubah isi file menjadi array of sentence tiap baris
    file = file.split('\n')
    arr = []
    # Proses tiap baris mengubah multiline comments menjadi _comment_
    found = False
    for line in file:
        if (globalVariable.acc):
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

            # Mengubah singleline comments menjadi _next_
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
            # Mengubah keyword number menjadi '_number_'
            # ''' BELOM NIH '''
            # Mengubah keyword number menjadi '_string_'
            # ''' BELOM NIH '''
            # Mengubah keyword boolean menjadi '_boolean_'
            # ''' BELOM NIH '''
            # Mengubah keyword object menjadi '_object_'
            # ''' BELOM NIH '''
            # Pemrosesan null

            # Mengubah isi file menjadi array of array of word
            if (line != ''):
                line = line.split()

            # Mengubah kata yang tidak ada dalam keyword menjadi _variable_
            line = validVariable.isVariable(
                line, globalVariable.replacedsymbol, globalVariable.js_grammar)

            arr.append(line)
            globalVariable.rowError += 1

    return arr


# PROGRAM UTAMA
# Membuka file Node.js
fileName = sys.argv[1]
dir = 'test/' + str(fileName)
file = open(dir, "r")
file = str(file.read())

arr_file = file.split('\n')

# Mulai proses parsing
# if (globalVariable.acc)

# Output program
if (globalVariable.acc):
    print("Accepted")
else:
    error = arr_file[globalVariable.rowError-1]
    error = error.replace(' ', '')
    print("Syntax Error")
    print("Terjadi kesalahan pada line " + str(globalVariable.rowError) +
          ' :"' + error + '"')
