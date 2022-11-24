# Global variabel untuk validasi
global acc
acc = True

global rowError
rowError = 0

# Tuple keyword di JavaScript
js_grammar = ('break', 'const', 'case', 'catch', 'continue', 'default', 'delete', 'else', 'false', 'finally',
              'for', 'function', 'if', 'let', 'null', 'return', 'switch', 'throw', 'try', 'true', 'var', 'while')
js_compareOp = ('==', '===', '!=', '!==', '>', '<', '>=', '<=', '?')
js_assignLogicOp = ('&&=', '||=', '??=')
js_logicOp = ('&&', '||')  # pindahin ! ke prefix
js_assignBitwiseOp = ('<<=', '>>=', '>>>=', '&=', '^=', '|=')
js_bitwiseOp = ('&', '|', '~', '^', '<<', '>>', '>>>')  # pindahin ~ ke prefix
js_assignArithOp = ('+=', '-=', '*=', '/=', '%=', '**=')
js_assignDeclare = ('=')
# pindahin - ke premidfix, ++ -- ke prepost
js_arithOp = ('+', '*', '**', '/', '%')
js_symbol = (';', ',', ':', '.')
js_brackets = ('(', ')', '{', '}', '[', ']')
js_prefixOp = ('~')  # op yang letaknya harus di depan
js_notOp = ('!')  # op yang letaknya harus di depan cuman bisa di variabel
js_premidfixOp = ('-')  # op yang letaknya bisa di depan / tengah
js_prepostfixOp = ('++', '--')  # op yang letaknya bisa di depan / belakang
replacedsymbol = ('_comment_', '_arith_', '_assign_', '_compare_', '_logic_', '_bitwise_',
                  '_commonOpen_', '_commonClose_', '_curlyOpen_', '_curlyClose_', '_number_', '_variable_',
                  '_prefixOp_', '_notOp_', '_premidOp_', '_prepostOp_', '_expression_', '_string_', '_semicolon_', '_equalSign_')
