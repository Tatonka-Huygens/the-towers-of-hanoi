# Characters transformation program
# Luis Manyari Yong



from random import randint
import math
import time



#        [ (x,chr(x)) for x in range(16384) ]




def myConcat(L):
    current = ''
    for x in L:
        current = current + x
    return current






def list2dict(L, keylist): return { keylist[i]:L[i] for i in range(len(L)) }

def my_function_composition(f,g): return { list(f.keys())[x]:g[x] for x in range(len(g)) }


def convert_to_S1(L): return [ chr(randint(11030,11033)) if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_S2(L): return [ chr(randint(11026,11029)) if L[x]=='*' else ['0','1'][randint(0,1)] for x in range(len(L)) ]

def convert_to_S3(L): return [ chr(8721) if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_S4(L): return [ chr(9608) if L[x]=='*' else ' ' for x in range(len(L)) ]


def convert_to_S5(L): return [ chr(9650) if L[x]=='*' else chr(randint(10241,10495)) for x in range(len(L)) ]

def convert_to_S6(L): return [ chr(randint(10063,10066)) if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_S7(L): return [ chr(randint(9824,9831)) if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_S8(L): return [ chr(9608) if L[x]=='*' else [chr(8944),chr(8945)][randint(0,1)] for x in range(len(L)) ]

def convert_to_S9(L): return [ chr(11035) if L[x]=='*' else chr(11036) for x in range(len(L)) ]

def convert_to_S10(L): return [ chr(randint(8621,8985)) if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_S11(L): return [ [chr(10062),chr(9989)][randint(0,1)] if L[x]=='*' else ['0','1'][randint(0,1)] for x in range(len(L)) ]

def convert_to_S12(L): return [ chr(9775) if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_S13(L): return [ [chr(9208),chr(9209),chr(9210),chr(9197),chr(9198),chr(9199)][randint(0,5)] if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_S14(L): return [ chr(11035) if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_S15(L): return [ chr(randint(11035,11036)) if L[x]=='*' else ' ' for x in range(len(L)) ]

def convert_to_Sonar(L): return [ chr(10739) if L[x]=='*' else chr(randint(10241,10495)) for x in range(len(L)) ]


A_let =     [ [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ','*',' ',' ','*',' ',' ',' '],
              [ ' ',' ',' ','*',' ',' ','*',' ',' ',' '],
              [ ' ',' ','*',' ',' ',' ',' ','*',' ',' '],
              [ ' ',' ','*','*','*','*','*','*',' ',' '],
              [ ' ','*',' ',' ',' ',' ',' ',' ','*',' '],
              [ ' ','*',' ',' ',' ',' ',' ',' ','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'] ]




B_let =     [ [ '*','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*','*','*','*','*','*','*','*','*',' '] ]



C_let =     [ [ ' ',' ',' ','*','*','*','*','*','*','*'],
              [ ' ',' ','*',' ',' ',' ',' ',' ',' ',' '],
              [ ' ','*',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ','*',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ','*',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ','*','*','*','*','*','*','*'] ]



D_let =     [ [ '*','*','*','*','*','*','*',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ','*','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ','*','*'],
              [ '*',' ',' ',' ',' ',' ',' ','*','*',' '],
              [ '*','*','*','*','*','*','*',' ',' ',' '] ]


E_let =       [ [ '*','*','*','*','*','*','*','*','*','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*'] ]



F_let =      [ [ '*','*','*','*','*','*','*','*','*','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '] ]



G_let =     [ [ ' ',' ',' ','*','*','*','*','*','*',' '],
              [ ' ',' ','*',' ',' ',' ',' ',' ',' ','*'],
              [ ' ','*',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ','*','*','*','*','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ','*',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ','*',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ',' ','*','*','*','*','*','*',' '] ]



H_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*','*','*','*','*','*','*','*','*','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'] ]


I_let =     [ [ '*','*','*','*','*','*','*','*','*','*'],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*'] ]


J_let =     [ [ ' ','*','*','*','*','*','*','*','*',' '],
              [ ' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ '*','*','*','*','*','*',' ',' ',' ',' '] ]



K_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ','*','*'],
              [ '*',' ',' ',' ',' ',' ','*','*',' ',' '],
              [ '*',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ '*',' ',' ','*','*',' ',' ',' ',' ',' '],
              [ '*','*','*',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ','*','*',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ','*','*',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ','*','*'] ]



L_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*'] ]


M_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*','*',' ',' ',' ',' ',' ',' ','*','*'],
              [ '*',' ','*',' ',' ',' ',' ','*',' ','*'],
              [ '*',' ',' ','*',' ',' ','*',' ',' ','*'],
              [ '*',' ',' ',' ','*','*',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'] ]



N_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*','*',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ','*',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ','*',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ','*',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ','*',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ','*',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ','*',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ','*','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'] ]


O_let =     [ [ ' ','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ','*','*','*','*','*','*','*','*',' '] ]



P_let =     [ [ '*','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '] ]


Q_let =     [ [ ' ','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ','*',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ','*',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ','*',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ','*',' '],
              [ ' ','*','*','*','*','*','*','*',' ','*'] ]



R_let =     [ [ '*','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ','*',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ','*',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'] ]



S_let =     [ [ ' ','*','*','*','*','*','*','*','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ','*','*','*','*','*','*','*','*',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ','*','*','*','*','*','*','*','*',' '] ]



Sa_let =     [ [ '*',' ',' ','*','*','*','*','*','*',' '],
              [ '*',' ','*',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ','*',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ','*',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ','*','*','*','*','*','*',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ','*',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ',' ','*','*','*','*','*','*',' '] ]



T_let =     [ [ '*','*','*','*','*','*','*','*','*','*'],
              [ '*',' ',' ',' ','*','*',' ',' ',' ','*'],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '] ]



U_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ','*','*','*','*','*','*','*','*',' '] ]




V_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ','*',' ',' ',' ',' ',' ',' ','*',' '],
              [ ' ','*',' ',' ',' ',' ',' ',' ','*',' '],
              [ ' ',' ','*',' ',' ',' ',' ','*',' ',' '],
              [ ' ',' ','*',' ',' ',' ',' ','*',' ',' '],
              [ ' ',' ',' ','*',' ',' ','*',' ',' ',' '],
              [ ' ',' ',' ','*',' ',' ','*',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '] ]



W_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ '*',' ',' ',' ','*','*',' ',' ',' ','*'],
              [ '*',' ',' ',' ','*','*',' ',' ',' ','*'],
              [ '*',' ',' ',' ','*','*',' ',' ',' ','*'],
              [ '*',' ',' ',' ','*','*',' ',' ',' ','*'],
              [ '*',' ',' ','*',' ',' ','*',' ',' ','*'],
              [ ' ','*',' ','*',' ',' ','*',' ','*',' '],
              [ ' ',' ','*','*',' ',' ','*','*',' ',' '] ]




X_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ','*',' ',' ',' ',' ',' ',' ','*',' '],
              [ ' ',' ','*',' ',' ',' ',' ','*',' ',' '],
              [ ' ',' ',' ','*',' ',' ','*',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ','*',' ',' ','*',' ',' ',' '],
              [ ' ',' ','*',' ',' ',' ',' ','*',' ',' '],
              [ ' ','*',' ',' ',' ',' ',' ',' ','*',' '],
              [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'] ]



Y_let =     [ [ '*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ','*',' ',' ',' ',' ',' ',' ','*',' '],
              [ ' ',' ','*',' ',' ',' ',' ','*',' ',' '],
              [ ' ',' ',' ','*',' ',' ','*',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*',' ',' ',' ',' '] ]



Z_let =     [ [ '*','*','*','*','*','*','*','*','*','*'],
              [ ' ',' ',' ',' ',' ',' ',' ',' ','*',' '],
              [ ' ',' ',' ',' ',' ',' ',' ','*',' ',' '],
              [ ' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
              [ ' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*',' ',' ',' ',' ',' '],
              [ ' ',' ',' ','*',' ',' ',' ',' ',' ',' '],
              [ ' ',' ','*',' ',' ',' ',' ',' ',' ',' '],
              [ ' ','*',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*'] ]


space_let = [ [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] ]



h_spc_let = [ [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' '] ]













LUCHO =     [ [ ' ',' ',' ',' ',' ',' ',' ',' ','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ',' ','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ',' ','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' '],
              [ ' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' '],
              [ ' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*',' ','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' '],
              [ '*','*','*','*','*','*','*','*','*','*','*',' ',' ','*','*','*','*','*',' ',' ',' ',' ','*','*',' ',' ',' ',' ','*'],
              [ '*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ','*','*','*','*','*',' ',' ',' ','*','*',' ',' ',' ',' ','*'],
              [ '*','*','*','*','*','*','*','*','*','*','*',' ',' ','*',' ','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ','*'],
              [ ' ',' ','*','*','*','*','*','*','*','*','*',' ',' ','*',' ','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ','*','*'],
              [ ' ','*','*','*','*','*','*','*','*','*','*',' ',' ','*',' ','*',' ','*','*','*','*','*','*','*','*','*','*','*',' '],
              [ ' ','*','*','*','*','*','*','*','*','*','*',' ',' ','*',' ','*',' ','*','*','*','*','*','*','*','*','*','*',' ','*'],
              [ ' ','*','*','*','*','*','*','*','*','*','*',' ',' ','*',' ','*',' ','*',' ','*','*','*','*','*','*','*','*',' ','*'],
              [ ' ','*','*','*','*','*','*','*','*','*','*',' ',' ','*',' ','*',' ','*',' ','*','*','*','*','*','*','*','*','*',' '],
              [ ' ','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' ','*','*','*','*',' ','*',' ',' '],
              [ ' ','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' ','*','*','*',' ','*',' ',' ',' '],
              [ ' ','*','*','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' ','*','*',' ',' ','*','*'],
              [ ' ','*','*','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' ','*',' ','*','*','*',' '],
              [ ' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' ','*',' ','*',' '],
              [ ' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' ','*',' ','*',' '],
              [ ' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' ','*',' '],
              [ ' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' ','*',' '],
              [ ' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' '],
              [ ' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ','*',' ','*',' ','*',' ','*',' '],
              [ ' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*'],
              [ ' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*'],
              [ ' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*'],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*'],
              [ ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']]











# n = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','space',][randint(0,26)]




alpha01 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','TOWER']


letters = [ A_let,B_let,C_let,D_let,E_let,F_let,G_let,H_let,I_let,J_let,K_let,L_let,M_let,N_let,O_let,P_let,Q_let,R_let,S_let,T_let,U_let,V_let,W_let,X_let,Y_let,Z_let,space_let ]



f01 = list2dict(list(range(len(alpha01))),alpha01)

g01 = list2dict(letters,list(range(len(letters))))


kdict01 = my_function_composition(f01,g01)



def rtk():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(convert_to_S4(R_let[x])),myConcat(convert_to_S4(E_let[x])),myConcat(convert_to_S4(L_let[x])),
        myConcat(convert_to_S4(E_let[x])),myConcat(convert_to_S4(A_let[x])),myConcat(convert_to_S4(S_let[x])),
        myConcat(convert_to_S4(E_let[x])))
        time.sleep(.05)
    print() 
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S4(T_let[x])),myConcat(convert_to_S4(H_let[x])),myConcat(convert_to_S4(E_let[x])))
        time.sleep(.05)
    print()
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S4(K_let[x])),myConcat(convert_to_S4(R_let[x])),myConcat(convert_to_S4(A_let[x])),myConcat(convert_to_S4(K_let[x])),myConcat(convert_to_S4(E_let[x])),myConcat(convert_to_S4(N_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)


def tkks():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(convert_to_S4(T_let[x])),myConcat(convert_to_S4(H_let[x])),myConcat(convert_to_S4(E_let[x])))
        time.sleep(.05)
        print()
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S4(K_let[x])),myConcat(convert_to_S4(R_let[x])),myConcat(convert_to_S4(A_let[x])),myConcat(convert_to_S4(K_let[x])),myConcat(convert_to_S4(E_let[x])),myConcat(convert_to_S4(N_let[x])))
        time.sleep(.05)
    print()
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S4(K_let[x])),myConcat(convert_to_S4(R_let[x])),myConcat(convert_to_S4(Y_let[x])),myConcat(convert_to_S4(P_let[x])),myConcat(convert_to_S4(T_let[x])),
             myConcat(convert_to_S4(O_let[x])),myConcat(convert_to_S4(S_let[x])),myConcat(convert_to_S4(Y_let[x])),myConcat(convert_to_S4(S_let[x])),myConcat(convert_to_S4(T_let[x])),myConcat(convert_to_S4(E_let[x])),myConcat(convert_to_S4(M_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)



def ttt():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(convert_to_S3(T_let[x])),myConcat(convert_to_S3(I_let[x])),myConcat(convert_to_S3(C_let[x])))
        time.sleep(.05)
    print()   
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S3(T_let[x])),myConcat(convert_to_S3(A_let[x])),myConcat(convert_to_S3(C_let[x])))
        time.sleep(.05)
    print()
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S3(T_let[x])),myConcat(convert_to_S3(O_let[x])),myConcat(convert_to_S3(E_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)




def toh():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.005)
    for x in range(len(A_let)):
        print('  ',myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(T_let[x])),' ',myConcat(convert_to_S13(H_let[x])),' ',myConcat(convert_to_S13(E_let[x])))
        time.sleep(.005)
    print()
    #time.sleep(1)
    for x in range(len(A_let)):
        print(myConcat(h_spc_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(T_let[x])),' ',myConcat(convert_to_S13(O_let[x])),' ',myConcat(convert_to_S13(W_let[x])),' ',myConcat(convert_to_S13(E_let[x])),' ',myConcat(convert_to_S13(R_let[x])),' ',myConcat(convert_to_S13(S_let[x])))
        time.sleep(.005)
    print()
    #time.sleep(1)
    for x in range(len(A_let)):
        print(myConcat(h_spc_let[x]),myConcat(h_spc_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(O_let[x])),' ',myConcat(convert_to_S13(F_let[x])))
        time.sleep(.005)
    print()
    #time.sleep(1)
    for x in range(len(A_let)):
        print(' ',myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(H_let[x])),' ',myConcat(convert_to_S13(A_let[x])),' ',myConcat(convert_to_S13(N_let[x])),' ',myConcat(convert_to_S13(O_let[x])),' ',myConcat(convert_to_S13(I_let[x])))
        time.sleep(.005)
    #time.sleep(1)

def toh_s():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.005)
    for x in range(len(A_let)):
        print('   ',myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(L_let[x])),' ',myConcat(convert_to_S13(A_let[x])),' ',myConcat(convert_to_S13(S_let[x])))
        time.sleep(.005)
    print()
    #time.sleep(1)
    for x in range(len(A_let)):
        print(myConcat(h_spc_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(T_let[x])),' ',myConcat(convert_to_S13(O_let[x])),' ',myConcat(convert_to_S13(R_let[x])),' ',myConcat(convert_to_S13(R_let[x])),' ',myConcat(convert_to_S13(E_let[x])),' ',myConcat(convert_to_S13(S_let[x])))
        time.sleep(.005)
    print()
    #time.sleep(1)
    for x in range(len(A_let)):
        print('   ',myConcat(h_spc_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(D_let[x])),' ',myConcat(convert_to_S13(E_let[x])))
        time.sleep(.005)
    print()
    #time.sleep(1)
    for x in range(len(A_let)):
        print(' ',myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(H_let[x])),' ',myConcat(convert_to_S13(A_let[x])),' ',myConcat(convert_to_S13(N_let[x])),' ',myConcat(convert_to_S13(O_let[x])),' ',myConcat(convert_to_S13(I_let[x])))
        time.sleep(.005)
    #time.sleep(1)


def hmn():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S3(H_let[x])),myConcat(convert_to_S3(A_let[x])),myConcat(convert_to_S3(N_let[x])),
        myConcat(convert_to_S3(G_let[x])),myConcat(convert_to_S3(M_let[x])),myConcat(convert_to_S3(A_let[x])),
        myConcat(convert_to_S3(N_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)


def sonar():
    for x in range(len(A_let)):
        print('       ',myConcat(convert_to_Sonar(S_let[x])),myConcat(convert_to_Sonar(O_let[x])),myConcat(convert_to_Sonar(N_let[x])),
        myConcat(convert_to_Sonar(A_let[x])),myConcat(convert_to_Sonar(R_let[x])))
        time.sleep(.05)


def lot():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S3(L_let[x])),myConcat(convert_to_S3(I_let[x])),myConcat(convert_to_S3(G_let[x])),
        myConcat(convert_to_S3(H_let[x])),myConcat(convert_to_S3(T_let[x])),myConcat(convert_to_S3(S_let[x])),myConcat(space_let[x]),
        myConcat(convert_to_S3(O_let[x])),myConcat(convert_to_S3(U_let[x])),myConcat(convert_to_S3(T_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)



def invInd():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S3(I_let[x])),myConcat(convert_to_S3(N_let[x])),myConcat(convert_to_S3(V_let[x])),
        myConcat(convert_to_S3(E_let[x])),myConcat(convert_to_S3(R_let[x])),myConcat(convert_to_S3(S_let[x])),myConcat(convert_to_S3(E_let[x])),myConcat(space_let[x]),
        myConcat(convert_to_S3(I_let[x])),myConcat(convert_to_S3(N_let[x])),myConcat(convert_to_S3(D_let[x])),myConcat(convert_to_S3(E_let[x])),myConcat(convert_to_S3(X_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)



def dp():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S3(D_let[x])),myConcat(convert_to_S3(O_let[x])),
        myConcat(convert_to_S3(T_let[x])),myConcat(space_let[x]),myConcat(convert_to_S3(P_let[x])),myConcat(convert_to_S3(R_let[x])),myConcat(convert_to_S3(O_let[x])),
        myConcat(convert_to_S3(D_let[x])),myConcat(convert_to_S3(U_let[x])),myConcat(convert_to_S3(C_let[x])),myConcat(convert_to_S3(T_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)

   



def lck():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S7(L_let[x])),myConcat(convert_to_S7(U_let[x])),
        myConcat(convert_to_S7(C_let[x])),myConcat(convert_to_S7(H_let[x])),myConcat(convert_to_S7(O_let[x])),myConcat(convert_to_S7(Sa_let[x])))
        time.sleep(.05)
    print()
    for x in range(len(A_let)):  
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S4(C_let[x])),myConcat(convert_to_S4(A_let[x])),myConcat(convert_to_S4(L_let[x])),myConcat(convert_to_S4(C_let[x])),
        myConcat(convert_to_S4(U_let[x])),myConcat(convert_to_S4(L_let[x])),myConcat(convert_to_S4(U_let[x])),myConcat(convert_to_S4(S_let[x])))
        time.sleep(.05)
    print()
    for x in range(len(A_let)):  
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S10(K_let[x])),myConcat(convert_to_S10(R_let[x])),myConcat(convert_to_S10(A_let[x])),
        myConcat(convert_to_S10(list(reversed(K_let[x])))),myConcat(convert_to_S10(list(reversed(E_let[x])))),myConcat(convert_to_S10(list(reversed(R_let[x])))))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)

   


def tatonka():
    print()
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S13(T_let[x])),myConcat(convert_to_S13(A_let[x])),
        myConcat(convert_to_S13(T_let[x])),myConcat(convert_to_S13(O_let[x])),myConcat(convert_to_S13(N_let[x])),myConcat(convert_to_S13(K_let[x])),myConcat(convert_to_S13(A_let[x])),myConcat(convert_to_S13(Sa_let[x])))
        time.sleep(.05)
    for x in LUCHO:
        print('                       ',myConcat(convert_to_S9(x))+myConcat(reversed(convert_to_S9(x))))
        time.sleep(.05)




def lkks():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(convert_to_S13(L_let[x])),myConcat(convert_to_S13(U_let[x])),
        myConcat(convert_to_S13(C_let[x])),myConcat(convert_to_S13(H_let[x])),myConcat(convert_to_S13(O_let[x])),myConcat(convert_to_S13(Sa_let[x])))
        time.sleep(.05)
    print()
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S9(K_let[x])),myConcat(convert_to_S9(R_let[x])),
        myConcat(convert_to_S9(A_let[x])),myConcat(convert_to_S9(K_let[x])),myConcat(convert_to_S9(E_let[x])),myConcat(convert_to_S9(N_let[x])))
        time.sleep(.05)
    print()
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(space_let[x]),myConcat(space_let[x]),myConcat(convert_to_S12(K_let[x])),myConcat(convert_to_S12(R_let[x])),myConcat(convert_to_S12(Y_let[x])),myConcat(convert_to_S12(P_let[x])),myConcat(convert_to_S12(T_let[x])),
        myConcat(convert_to_S12(O_let[x])),myConcat(convert_to_S12(S_let[x])),myConcat(convert_to_S12(Y_let[x])),myConcat(convert_to_S12(S_let[x])),myConcat(convert_to_S12(T_let[x])),myConcat(convert_to_S12(E_let[x])),myConcat(convert_to_S12(M_let[x])))
        time.sleep(.05)
    print()
    time.sleep(.05)
    print()
    time.sleep(.05)
    print()
    time.sleep(.05)
    print()
    time.sleep(.05)
    print()
    time.sleep(.05)










def orS():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(convert_to_S3(O_let[x])),myConcat(convert_to_S3(R_let[x])),myConcat(space_let[x]),
        myConcat(convert_to_S3(S_let[x])),myConcat(convert_to_S3(E_let[x])),myConcat(convert_to_S3(A_let[x])),
        myConcat(convert_to_S3(R_let[x])),myConcat(convert_to_S3(C_let[x])),myConcat(convert_to_S3(H_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)





def andS():
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]),myConcat(convert_to_S3(A_let[x])),myConcat(convert_to_S3(N_let[x])),myConcat(convert_to_S3(D_let[x])),myConcat(space_let[x]),
        myConcat(convert_to_S3(S_let[x])),myConcat(convert_to_S3(E_let[x])),myConcat(convert_to_S3(A_let[x])),
        myConcat(convert_to_S3(R_let[x])),myConcat(convert_to_S3(C_let[x])),myConcat(convert_to_S3(H_let[x])))
        time.sleep(.05)
    for x in range(len(A_let)):
        print(myConcat(space_let[x]))
        time.sleep(.05)








def pAll():
    for x in range(len(alpha01)):
        for y in range(len(kdict01[alpha01[x]])):print(myConcat(convert_to_S2(kdict01[alpha01[x]][y])))
        print()



def pLetter(x):
    x = x.upper()
    for y in range(len(kdict01[x])):print(myConcat(convert_to_S2(kdict01[x][y])))
    print()

   

 



def enterMessage(string): return [ string[x] for x in range(len(string)) ]





msg1 = 'A PREP COURSE FOR THE MONTH LONG WORLD CUP SOCCER TOURNAMENT  A WORLDWIDE PHENOMENON TO BE PLAYED IN THE UNITED STATES FOR THE FIRST TIME BEGINNING IS AVAILABLE IN A SET OF THREE HOME VIDEOS EACH OF THE THREE VOLUMES BY POLYGRAM VIDEO'

def message(msg1):
    msg1 = msg1.upper()
    msg = enterMessage(msg1)
    for x in range(len(msg)):
        for y in range(len(kdict01[msg[x]])):print(myConcat(convert_to_S9(kdict01[msg[x]][y])))
        print()
        time.sleep(.5)




def message2(msg1):
    msg1 = msg1.upper()
    msg = enterMessage(msg1)
    for x in range(len(kdict01['A'])):print((myConcat(convert_to_S9(kdict01[msg[0]][x]+kdict01[msg[1]][x]+kdict01[msg[2]][x]+kdict01[msg[3]][x]+
                                                                    kdict01[msg[4]][x]+kdict01[msg[5]][x]+kdict01[msg[6]][x]+kdict01[msg[7]][x]+
                                                                    kdict01[msg[8]][x]+kdict01[msg[9]][x]+kdict01[msg[10]][x]+kdict01[msg[11]][x]+
                                                                    kdict01[msg[12]][x]+kdict01[msg[13]][x]+kdict01[msg[14]][x]+kdict01[msg[15]][x]))))
