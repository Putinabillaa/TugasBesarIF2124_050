import globalVariable 
from itertools import cycle
import sys
import validVariable
import validNumber

# Kategori Expression:
# 1. Compare (setelah variable ada operator compare)
# 2. Assign (setelah variable ada operator assign)
# 3. Uner (sebelum sebuah variable ada operator uner (!))
# 4. Operasi (diantara variable/angka/boolean ada operator aritmatik atau binary)


matofword = [["none", "random", "halo"],  # kontrol
             ["_assign_",  "_variable_", "_arith_", "_variable_"],
             ["_variable_", "_assign_", "_variable_", "_arith_",
                 "_variable_"],  # cek variable sendiri
             ["naufal", "wadidaw", "random", "_variable_", "_compare_",
                 "_compare_", "_variable_"],  # cek variable dan operator biasa
             ["random", "_prefixOp_", "_variable_"],  # cek prefix
             ["_premidOp_", "_variable_", "_premidOp_", "_variable_"],  # true
             ["random", "_prepostOp_", "_variable_"],  # true
             ["_variable_", "_prepostOp_", "random", "halo"],  # true
             ["_notOp_", "_variable_"]]  # true


def isOperator(word):
    return word == "_arith_" or word == "_compare_" or word == "_logic_" or word == "_bitwise_" or word == "_premidOp_"


def isOperan(word):
    return word == "_variable_" or word == "_number_" or word == "true" or word == "false" or word == "null"


def isPrefixOp(word):
    return word == "_prefixOp_"


def isPremidOp(word):
    return word == "_premidOp_"


def isPrepostOp(word):
    return word == "_prepostOp_"


def isNotOp(word):
    return word == "_notOp_"


def checkInfix(line, index):
    j = index
    operan = False
    for j in range(index, len(line)):
        # print(line[j])

        operan = not operan
        if(operan):
            # print("cek operan")
            if (isOperan(line[j])):  # kalau elemen pertama langsung operator maka salah
                valid = True
            else:
                valid = False
        else:  # disini gaboleh ada operan
            if (isOperan(line[j])):
                valid = False
            # false biar kalau operator nya adalah elemen terakhir, gaboleh
            elif(isOperator(line[j])):
                valid = False
            else:
                break
        # print(valid)
    return valid, j


def validity(line):

    valid = True
    found = False
    j = 0
    i = 0

    for i in range(len(line)):

        if(isOperan(line[i])):  # jika ada operan dengan elemen selanjutnya operator

            if(i != len(line)-1):
                if(isOperator(line[i+1])):  # cek apa ada operator di next element

                    valid, j = checkInfix(line, i)
                    # print(valid)
                    if(valid):
                        found = True
                    break

                elif (isOperan(line[i+1])):  # kalau malah ada operan jd salah
                    valid = False
                    if(valid):
                        found = True
                    break

                # kalau habis variabel ada prepostOp
                elif (isPrepostOp(line[i+1])):
                    valid = True
                    if(valid):
                        found = True
                    break

        elif (isPrefixOp(line[i])):  # cek pas ada operan prefix
            if(i != len(line)-1):
                if(isOperan(line[i+1])):
                    valid, j = checkInfix(line, i+1)
                else:
                    valid = False
            else:
                valid = False

            if(valid):
                found = True

            break

        elif (isPremidOp(line[i])):  # op yang bisa didepan atau di tengah
            if(i != len(line)-1):
                if(isOperan(line[i+1])):
                    valid, j = checkInfix(line, i+1)
                else:
                    valid = False
            else:
                valid = False

            if(valid):
                found = True

            break

        elif(isPrepostOp(line[i])):
            if(i != len(line)-1):
                if(isOperan(line[i+1])):
                    valid, j = checkInfix(line, i+1)
                else:
                    valid = False
            else:
                valid = False

            if(valid):
                found = True

            break

        elif (isNotOp(line[i])):
            if(i != len(line)-1):
                if(isOperan(line[i+1])):
                    valid, j = checkInfix(line, i+1)
                else:
                    valid = False
            else:
                valid = False

            if(valid):
                found = True

            break

        elif (isOperator(line[i])):  # jika ada operator tanpa variable
            valid = False
            break

    return valid, i, j, found


def elimExpression(start, line):
    change = ["_arith_", "_compare_", "_logic_", "_bitwise_", "_premidOp_",
              "_variable_", "_number_", "_prefixOp_", "_premidOp_", "_prepostOp_", "_notOp_"]
    assign = False

    line.insert(start, '_expression_')

    for i in range(len(line)-1):  # cek kalo ada assignment
        if(line[i] == '_variable_'):
            if(i != len(line)-1):
                if(line[i+1] == "_assign_" or line[i+1] == '_equalSign_'):
                    print(" line yang ditinjau",line[i+1])
                    assign = True
                    break

    for change in change:
        while(line.count(change)):
            line.remove(change)

    if(assign):
        # kalo ada assignment balikin variabel sebelumnya
        line.insert(i, "_variable_")


def expressionCheck(matofword):

    valid = True
    lineError = 1

    for line in matofword:
        validtemp, idAwal, idAKhir, found = validity(line)
        valid = valid and validtemp
        if(valid):
            lineError += 1

        if(found):
            elimExpression(idAwal, line)
    
    return matofword, valid, lineError

# FOR DEBUGGING FROM FILE INPUT

# def ReadyToParse(file):
#     # Mengubah isi file menjadi array of sentence tiap baris
#     file = file.split('\n')
#     arr = []
#     # Proses tiap baris mengubah multiline comments menjadi _comment_
#     found = False
#     for line in file:
#         if (globalVariable.acc):
#             # Mengubah semicolon menjadi _semicolon
#             line = line.replace(';', ' _semicolon_')
#             # Mengubah multiline comments menjadi _comment_
#             idxMultiOpen = line.find('/*')
#             if (idxMultiOpen != -1 or found):
#                 found = True
#                 idxMultiClose = line.find('*/')
#                 if (idxMultiClose == -1):
#                     line = line.replace(line[0:], '_comment_')
#                 else:
#                     line = line.replace(line[0:], '_comment_')
#                     found = False
#             else:  # idxMultiOpen == -1 and not found
#                 idxMultiClose = line.find('*/')
#                 if (idxMultiClose == -1):
#                     found = False
#                 else:
#                     globalVariable.acc = False

#             # Mengubah singleline comments menjadi _comment_
#             if (globalVariable.acc):
#                 idxSingle = line.find('//')
#                 if (idxSingle != -1):
#                     line = line.replace(
#                         line[0:], "_comment_")

#             # Mengubah bracket
#             for brackets in globalVariable.js_brackets:
#                 if (brackets == '('):
#                     line = line.replace(brackets, ' _commonOpen_ ')
#                 if (brackets == ')'):
#                     line = line.replace(brackets, ' _commonClose_')
#                 if (brackets == '{'):
#                     line = line.replace(brackets, ' _curlyOpen_')
#                 if (brackets == '}'):
#                     line = line.replace(brackets, ' _curlyClose_')
#                 if (brackets == '['):
#                     line = line.replace(brackets, ' _squareOpen_')
#                 if (brackets == ']'):
#                     line = line.replace(brackets, ' _squareClose_')

#             # Mengubah keyword operator
#             for operator in globalVariable.js_compareOp:
#                 line = line.replace(operator, ' _compare_')
#             for operator in globalVariable.js_assignLogicOp:
#                 line = line.replace(operator, ' _assign_')
#             for operator in globalVariable.js_logicOp:
#                 line = line.replace(operator, ' _logic_')
#             for operator in globalVariable.js_assignBitwiseOp:
#                 line = line.replace(operator, ' _assign_')
#             for operator in globalVariable.js_bitwiseOp:
#                 line = line.replace(operator, ' _bitwise_')
#             for operator in globalVariable.js_assignArithOp:
#                 line = line.replace(operator, ' _assign_')
#             for operator in globalVariable.js_arithOp:
#                 line = line.replace(operator, ' _arith_')
#             for operator in globalVariable.js_assignDeclare :
#                 line = line.replace(operator, ' _equalSign_')

#             # Mengubah tipe data
#             # Mengubah keyword number menjadi '_string_'
#             idxStringOpen = line.find("'")
#             if (idxStringOpen != -1):
#                 idxStringClose = line.find("'", idxStringOpen+1)
#                 if (idxStringClose == -1):
#                     globalVariable.acc = False
#                 else:
#                     line = line.replace(
#                         line[idxStringOpen:idxStringClose+1], ' _string_')
#             else:  # idxstringOpen == -1
#                 idxStringClose = line.find("'")
#                 if (idxStringClose != -1):
#                     globalVariable.acc = False

#             idxStringOpen = line.find('"')
#             if (idxStringOpen != -1):
#                 idxStringClose = line.find('"', idxStringOpen+1)
#                 if (idxStringClose == -1):
#                     globalVariable.acc = False
#                 else:
#                     line = line.replace(
#                         line[idxStringOpen:idxStringClose+1], ' _string_')
#             else:  # idxstringOpen == -1
#                 idxStringClose = line.find('"')
#                 if (idxStringClose != -1):
#                     globalVariable.acc = False

#             # Mengubah keyword object menjadi '_object_'
#             # ''' BELOM NIH '''

#             # Mengubah isi file menjadi array of array of word
#             if (line != ''):
#                 line = line.split()

#             # Mengubah keyword number menjadi '_number_'
#             line = validNumber.isNumber(line)

#             # Mengubah kata yang tidak ada dalam keyword menjadi _variable_
#             if (globalVariable.acc):
#                 line = validVariable.isVariable(
#                     line, globalVariable.replacedsymbol, globalVariable.js_grammar)

#             arr.append(line)
#             globalVariable.rowError += 1
#     return arr


# dir = 'test/' + str('inputAcc.js')
# file = open(dir, "r")
# file = str(file.read())

# arr_line = file.split('\n')

# arrMain = ReadyToParse(file)

# for row in arrMain:
#     print(*row)

# print()

# result, valid, idLine = expressionCheck(arrMain)

# for row in result:
#     print(*row)