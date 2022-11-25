def CYK(grammar, arrofword):
    if(len(arrofword) != 0):
        CYKtable = [[[] for i in range(len(arrofword))] for j in range(len(arrofword))]
        for i in range(len(arrofword)):
            term = arrofword[i]
            for nonterm in grammar:
                if([term] in grammar[nonterm]):
                    CYKtable[i][i].append(nonterm)
        for i in range(1, len(arrofword)):
            for j in range(len(arrofword) - i):
                for k in range(j, i + j):
                    for nonterm in grammar:
                        for prod in grammar[nonterm]:
                            if(len(prod) != 1):
                                if((prod[0] in CYKtable[j][k]) and (prod[1] in CYKtable[k + 1][i + j]) 
                                    and (nonterm not in CYKtable[j][i + j])): CYKtable[j][i + j].append(nonterm)  
        if('START' in CYKtable[0][len(arrofword) - 1]): return True
        else : return False
    else: return True