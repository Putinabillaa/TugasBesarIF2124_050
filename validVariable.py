'''
4 Ways to Declare a JavaScript Variable:
1. Using var
2. Using let
3. Using const
4. Using nothing

The general rules for constructing names for variables (unique identifiers) are:
a. Names can contain letters, digits, underscores, and dollar signs.
b. Names must begin with a letter.
c. Names can also begin with $ and _ (but we will not use it in this tutorial).
d. Names are case sensitive (y and Y are different variables).
e. Reserved words (like JavaScript keywords) cannot be used as names.

Sumber : https://www.w3schools.com/js/js_variables.asp
'''
import globalVariable


def variableCheck(word):
    letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    letters_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    signs = '_$'
    begin = letters_lowercase+letters_uppercase+signs
    notbegin = begin+digits

    for i in range(0, len(word)):
        if ((i == 0) and (word[i] in begin)):
            valid = True
        elif ((i > 0) and (word[i] in notbegin)):
            valid = True
        else:
            valid = False
    return valid


def isVariable(list_word, replacedsymbol, js_grammar):
    list_word_done = []
    for word in list_word:
        if (globalVariable.acc):
            if ((word in replacedsymbol) or (word in js_grammar)):
                list_word_done.append(word)
            else:
                if (variableCheck(word)):
                    list_word_done.append('_variable_')
                else:
                    globalVariable.acc = False

    if (globalVariable.acc):
        return list_word_done
    else:
        return -1
