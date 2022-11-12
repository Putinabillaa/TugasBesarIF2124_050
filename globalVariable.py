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
js_logicOp = ('&&', '||', '!')
js_assignBitwiseOp = ('<<=', '>>=', '>>>=', '&=', '^=', '|=')
js_bitwiseOp = ('&', '|', '~', '^', '<<', '>>', '>>>')
js_assignArithOp = ('=', '+=', '-=', '*=', '/=', '%=', '**=')
js_arithOp = ('+', '-', '*', '**', '/', '%', '++', '--')
js_symbol = (';', ',')
js_brackets = ('(', ')', '{', '}')
replacedsymbol = ('_comment_', '_arith_', '_assign_', '_compare_', '_logic_', '_bitwise_',
                  '_commonOpen_', '_commonClose_', '_curlyOpen_', '_curlyClose_', '_number_', '_variable_')
