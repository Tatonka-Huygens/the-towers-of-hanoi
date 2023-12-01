
# spreadsheet_encoding

from numbers_to_words import *
from numeros_a_palabras import *
#from string_integer_interconversion import *
#from findtime import *
import functools


def ss_decode_col_id(col: str) -> int:
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)



def int_to_ss_col_id(x: int) -> str:
    s = []
    while True:
        if x%26==0 and x<=702:           
            s.append('Z')
            x //= 27
        elif x%26==0 and x>=728:
            x = x - 26
            s.append('Z')
            x //= 26
        else:
            s.append(chr(ord('@') + x % 26))
            x //= 26
        if x == 0:
            break       
    return ''.join(reversed(s))
        

""" @find_time
def run_range(n):
    for x in range(n):
        print(ss_decode_col_id(int_to_ss_col_id(x+1)),' ',int_to_ss_col_id(x+1), end='   ')
        print_num_in_words(x+1,' ',' ')
        print(' ' * len(int_to_string(x+1)) + ' ' * len(int_to_ss_col_id(x+1)), end='      ')
        imprimir_numeros_en_palabras(x+1,' ',' ')
         """




