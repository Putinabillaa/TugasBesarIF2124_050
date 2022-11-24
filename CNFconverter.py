import copy
import string


def isNonTerminal(sym):
    for char in sym:
        if char not in (string.ascii_uppercase):
            return False
    return True

def isTerminal(sym):
    return not isNonTerminal(sym)

def readProdRule(CFGFile):
    CFG = {}
    with open(CFGFile, 'r') as f:
        lines = []
        listlinesfromfile = f.read().split('\n')
        for linefromfile in listlinesfromfile:
            separate = linefromfile.split(' -> ')
            if(len(separate) == 2):
                lines.append(separate)
        for line in lines:
            lhs = line[0].replace(" ", "")
            splitprods = [line[1].split(" ")]
            rhs = []
            for splitprod in splitprods:
                rhs.append(
                        [" " if word == "__space__"  
                        else "\n" if word == "__new_line__" 
                        else word
                        for word in splitprod 
                        ]
                    )
            CFG.update({lhs: rhs})
    return CFG

def simplify(CFG):
    # simplify redundant symbol
    for lhs_sym in CFG:
        listprod = CFG[lhs_sym]
        stop = False
        while (stop == False):
            stop = True
            for prod in listprod:
                if(isNonTerminal(prod[0]) and len(prod) == 1):
                    listprod.remove(prod)
                    replacedprod = copy.deepcopy([
                                    prod for prod in CFG[prod[0]]
                                    if prod not in listprod
                                ])
                    listprod.extend(replacedprod)
                    stop = False
                    break
    return CFG
def singleProd(CFG):
    # eliminate non single production
    rules = {}
    for lhs in CFG:
        products = CFG[lhs]
        idx = 1
        for i in range(len(products)):
            while (len(products[i]) > 2):
                rules.update({f"{lhs}_NONTERM_{idx}": [[products[i][0], products[i][1]]]})
                products[i] = products[i][1:]
                products[i][0] = f"{lhs}_NONTERM_{idx}"
                idx += 1
    CFG.update(rules)
    return CFG   

def CNFconverter(dir):
    return singleProd(simplify(readProdRule(dir)))

print(CNFconverter('testcnfconverter.txt'))  

