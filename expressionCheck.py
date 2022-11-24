import globalVariable as gv
from itertools import cycle


# Kategori Expression:
# 1. Compare (setelah variable ada operator compare)
# 2. Assign (setelah variable ada operator assign)
# 3. Uner (sebelum sebuah variable ada operator uner (!))
# 4. Operasi (diantara variable/angka/boolean ada operator aritmatik atau binary)


matofword = [["none", "random"],
             ["nau", "_assign_"],
             ["naufal", "wadidaw", "random"],
             ["_variable_", "_assign_", "_variable_"]]


line = ["naufal", "wadidaw", "_compare_"]


def isOperator(word):
    return word == "_arith_" or word == "_compare_" or word == "_logic_" or word == "_bitwise_"

def isOperan(word):
    return word == "_variable_" or word == "_number_"

def isPrefixOp(word):
    return word == "!" or word == "~"

def isPremidOp(word):
    return word == "-"

def isPrepostOp(word):
    return word == "++" or word == "--"


def validity(line):

    valid = True
    
    for i in range (len(line)):

        if(isOperan(line[i]) and isOperan(line[i+1])): # kalau ada operan dengan elemen selanjutnya operan
            valid = False
            break
            
        #elif(isPrefixOp(line[i])):


        elif(isOperan(line[i]) and isOperator(line[i+1])): # jika ada operan dengan elemen selanjutnya operator
            j = i
            operan = False

            for j in range(i, len(line)):
                # print(line[j])
                
                operan = not operan
                if(operan):
                    # print("cek operan")
                    if (isOperan(line[j])): # kalau elemen pertama langsung operator maka salah
                        valid = True
                    else:
                        valid = False
                else: # disini gaboleh ada operan
                    if (isOperan(line[j])):
                        valid = False
                    elif(isOperator(line[j])): # false biar kalau operator nya adalah elemen terakhir, gaboleh
                        valid = False
                    else:
                        break
                # print(valid)
            break
        elif (isOperator(line[i])): #jika ada operator tanpa variable
            valid = False
            break

    return valid
        

def expressionCheck(matofword):

    valid = True

    for line in matofword:
        valid = valid and validity(line)
    
    return valid


print(expressionCheck(matofword))