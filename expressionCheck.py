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

def isOperator(word):
    return word == "_arith_" or word == "_compare_" or word == "_logic_" or word == "_bitwise_" or word == "_premidOp_"


def isOperan(word):
    return word == "_variable_" or word == "_number_" or word == "true" or word == "false" or word == "null" or word == "_string_"


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

   
    change = ["_arith_", "_compare_", "_logic_", "_bitwise_", "_premidOp_", "_string_",
              "_variable_", "_number_", "_prefixOp_", "_premidOp_", "_prepostOp_", "_notOp_",
              "true","false", "null" ]
    assign = False

    line.insert(start, '_expression_')

    for change in change:
        while(line.count(change)):
            line.remove(change)

            
    #print(line)
    for i in range(len(line)):  # cek kalo ada assignment
        if(line[i] == "_assign_" or line[i] == '_equalSign_'):
            assign = True
            break

    if(assign):
        # kalo ada assignment balikin variabel sebelumnya
        #print(i)
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
