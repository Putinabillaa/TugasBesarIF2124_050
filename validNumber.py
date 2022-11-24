import globalVariable


def numberCheck(word):
    notbegin = '0123456789'
    valid = True
    if (word[0] == '0'):
        if (len(word) > 1):
            valid = False
    else:
        found = False
        for i in range(1, len(word)):
            if (valid):
                if (word[i] == '.'):
                    if (found):
                        valid = False
                    else:
                        found = True
                        i += 1
                        if (not(word[i] in notbegin)):
                            valid = False
                elif (word[i] in notbegin):
                    valid = True
                else:
                    valid = False
    return valid


def isNumber(list_word):
    list_word_done = []
    digits = '0123456789'
    for word in list_word:
        if (word[0] in digits):
            if (numberCheck(word)):
                list_word_done.append('_number_')
            else:
                globalVariable.acc = False
        else:
            list_word_done.append(word)

    if (globalVariable.acc):
        return list_word_done
    else:
        return -1
