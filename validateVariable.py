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

def variableCheck(word):
    letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    letters_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    signs = '_$'
    begin = letters_lowercase+letters_uppercase+signs
    notbegin = begin+digits

    valid = False
    for i in range(0, len(word)):
        if ((i == 0) and (word[i] in begin)):
            valid = True
        elif ((i > 0) and word[i] in notbegin):
            valid = True
        else:
            valid = False

    return valid


def isVariable(list_word, replacedsymbol, js_grammar):
    list_word_done = []
    declare = False
    for word in list_word:
        # Using var, let, or const
        if (declare):
            if (variableCheck):
                list_word_done.append('_variable_')
            declare = False
        elif (word == 'var' or word == 'let' or word == 'const'):
            declare = True
        elif ((word in replacedsymbol) or (word in js_grammar)) :
            list_word_done.append(word)
        else :
            if (variableCheck):
                list_word_done.append('_variable_')
    
    return list_word_done
