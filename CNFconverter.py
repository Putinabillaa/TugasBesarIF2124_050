import copy
import string


def isNonTerminal(sym):
  if len(sym) == 1: 
    return False
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
        for linefromfiile in listlinesfromfile:
            separate = linefromfiile.split(' -> ')
            if(len(separate) == 2):
                lines.append(separate)
        for line in lines:
            lhs = line[0].replace(" ", "")
            rhs = []
            rhs.append(
                    [" " if word == "__space__"  
                    else "\n" if word == "__new_line__" 
                    else word
                    for word in line 
                    ]
                )
            CFG.update({lhs: rhs})
    return CFG

def simplify(CFG):
    # simplify redundant symbol
    for lhs_sym in CFG:
        listprod = CFG[lhs_sym]
        stop = False
        while (not stop):
            i = 0
            stop = True
            stop2 = False
            while(i < len(listprod) and not stop2):
                if(isNonTerminal(listprod[i][0]) and len(listprod[i][0]) == 1):
                    listprod.remove(listprod[i])
                    replacedprod = copy.deepcopy([
                                    prod for prod in CFG[listprod[i][0]]
                                    if prod not in listprod
                                ])
                    listprod.extend(replacedprod)
                    stop = False
                    stop2 = True
                i += 1
    return CFG

def singleProd(CFG):
    # eliminate non single production
    rules = {}
    for lhs in CFG:
        terminals = []
        products = CFG[lhs]
        listnonsingleprod = [prod for prod in products if len(prod) > 1]
        for nonsingleprod in listnonsingleprod:
            for sym in nonsingleprod:
                if (isTerminal(sym) and sym not in terminals): terminals.append(sym)
            for i in range(len(terminals)):
                rules.update({f"{lhs}_TERM_{i+1}": [[terminals[i]]]})
                for j in range(len(products)):
                    if (len(products[j]) > 1):
                        for k in range(len(products[j])):
                            if (products[j][k] == terminals[i]):
                                products[j][k] = products[j][k].replace(terminals[i], f"{lhs}_TERM_{i+1}") 
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

print(CNFconverter('testcnfconverter.txt')       )  

