# The Towers of Hanoi - 4 Pegs
# Copyright 2023 Luis (LUCHO) Manyari


import time, random
from datetime import datetime
from pascal_triangle import generate_pascal_triangle
from numbers_to_words import *
from numeros_a_palabras import *
from snake_string import snake_string_pythonic
from random import randint
from spreadsheet_encoding import *
from char_transform import toh, toh_s



def myConcat(L):
    current = ''
    for x in L:
        current = current + x
    return current



def find_time(original_function):
    def inner_function(*args, **kwargs):
        start_time = datetime.now()
        result = original_function(*args, **kwargs)
        end_time = datetime.now()

        if move_lang == '1':
            printFramedSentences(ring_length+30,f' Tiempo Total = {end_time - start_time} ')
        else:
            printFramedSentences(ring_length+25,f' Total Time = {end_time - start_time} ')

        return result
    return inner_function



def showInstructions():
    print('''

                                                   THE TOWERS OF HANOI
        
         ╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
         ║                                                                                                     ║
         ║             ║                        ║                        ║                        ║            ║
         ║             ║                    ████████                     ║                        ║            ║
         ║             ║                   ██████████                    ║                        ║            ║
         ║             ║                  ████████████                   ║                        ║            ║
         ║             ║                 ██████████████                  ║                        ║            ║
         ║             ║                ████████████████                 ║                        ║            ║
         ║             ║               ██████████████████                ║                        ║            ║
         ║             ║              ████████████████████               ║                        ║            ║
         ║             ║             ██████████████████████              ║                        ║            ║
         ╚═════════════╚════════════════════════╚════════════════════════╚════════════════════════╚════════════╝

                                                  


        Invented by the French mathematician Edouard Lucas in 1883. We are given a tower of eight disks, initially
        stacked in decreasing size on one of three pegs. The objective is to transfer the entire tower to one of
        the other pegs, moving only one disk at a time and never moving a larger one onto a smaller.

        We know that the solution to this recurrence is: 2 to the power of n - 1,  where n is the number of disks.

        Also, by mathematical induction, we know that we have to move n-1 smaller disks from the initial peg to the
        spare peg, then move the larger disk from the initial peg to the destination peg; finally, move n-1 disks
        from the spare peg to the destination peg.

        With this piece of information we can build a recursive algorithm to solve the problem. I used the
        following algorithm to obtain the moves:
                                                >>> def printMove(fr, to):
                                                ...     print('Move from ' + str(fr) + ' to ' + str(to))
                                                ...
                                                >>> def Towers_4(n, fr, to, spare1, spare2):
                                                ...     if n == 1:
                                                ...         printMove(fr, to)
                                                ...     else:
                                                ...         Towers_4(n-1, fr, spare1, to, spare2)
                                                ...         Towers_4(1, fr, to, spare1, spare2)
                                                ...         Towers_4(n-1, spare1, to, spare2, fr)
                                                ...
                                                >>>
                                                >>> Towers_4(3, 1, 2, 3, 4)
                                                Move from 1 to 2
                                                Move from 1 to 3
                                                Move from 2 to 3
                                                Move from 1 to 2
                                                Move from 3 to 4
                                                Move from 3 to 2
                                                Move from 4 to 2
                                                >>>
                                               
        A fast human would finish the puzzle ( 8 Disks ) in about four minutes.
        ''')

    print()
    print()       
    print()
    print()       
    printFramedSentences(47,' Press "enter" to continue... ')
    print()
    input()




    printFramedSentences(47,' Disk Generator Function ')
    print('''
>>> generate_disks(50)
                                                          ████████                                                   1
                                                         ██████████                                                  2
                                                        ████████████                                                 3
                                                       ██████████████                                                4
                                                      ████████████████                                               5
                                                     ██████████████████                                              6
                                                    ████████████████████                                             7
                                                   ██████████████████████                                            8
                                                  ████████████████████████                                           9
                                                 ██████████████████████████                                          10
                                                ████████████████████████████                                         11
                                               ██████████████████████████████                                        12
                                              ████████████████████████████████                                       13
                                             ██████████████████████████████████                                      14
                                            ████████████████████████████████████                                     15
                                           ██████████████████████████████████████                                    16
                                          ████████████████████████████████████████                                   17
                                         ██████████████████████████████████████████                                  18
                                        ████████████████████████████████████████████                                 19
                                       ██████████████████████████████████████████████                                20
                                      ████████████████████████████████████████████████                               21
                                     ██████████████████████████████████████████████████                              22
                                    ████████████████████████████████████████████████████                             23
                                   ██████████████████████████████████████████████████████                            24
                                  ████████████████████████████████████████████████████████                           25
                                 ██████████████████████████████████████████████████████████                          26
                                ████████████████████████████████████████████████████████████                         27
                               ██████████████████████████████████████████████████████████████                        28
                              ████████████████████████████████████████████████████████████████                       29
                             ██████████████████████████████████████████████████████████████████                      30
                            ████████████████████████████████████████████████████████████████████                     31
                           ██████████████████████████████████████████████████████████████████████                    32
                          ████████████████████████████████████████████████████████████████████████                   33
                         ██████████████████████████████████████████████████████████████████████████                  34
                        ████████████████████████████████████████████████████████████████████████████                 35
                       ██████████████████████████████████████████████████████████████████████████████                36
                      ████████████████████████████████████████████████████████████████████████████████               37
                     ██████████████████████████████████████████████████████████████████████████████████              38
                    ████████████████████████████████████████████████████████████████████████████████████             39
                   ██████████████████████████████████████████████████████████████████████████████████████            40
                  ████████████████████████████████████████████████████████████████████████████████████████           41
                 ██████████████████████████████████████████████████████████████████████████████████████████          42
                ████████████████████████████████████████████████████████████████████████████████████████████         43
               ██████████████████████████████████████████████████████████████████████████████████████████████        44
              ████████████████████████████████████████████████████████████████████████████████████████████████       45
             ██████████████████████████████████████████████████████████████████████████████████████████████████      46
            ████████████████████████████████████████████████████████████████████████████████████████████████████     47
           ██████████████████████████████████████████████████████████████████████████████████████████████████████    48
          ████████████████████████████████████████████████████████████████████████████████████████████████████████   49
         ██████████████████████████████████████████████████████████████████████████████████████████████████████████  50
>>>
        ''')

    print()
    printFramedSentences(47,' Press "enter" to continue... ')
    print()        
    input()





    printFramedSentences(47,' Maximum of 29 disks on 4 Pegs ')
    print()
    print()       
    print()
    print()        
    print()        
    print()
    print()        
    print()
    print()        
    print()         
    print()

    T1 = generate_disks(29)
    rn = randint(1,4)
    if rn == 1:
        pt(29,1,2,3,4)
    elif rn == 2:
        pt(29,2,1,3,4)
    elif rn == 3:
        pt(29,3,2,1,4)
    elif rn == 4:
        pt(29,4,2,1,3)

    print()
    print()   
    print()
    print()        
    print()       
    print()
    print()        
    print()
    print()         
    print()
    printFramedSentences(47,' Press "enter" to continue... ')
    print()          
    input()

    printFramedSentences(20,' Spreadsheet Encoding Algorithm And Converting Numbers to Words Algorithm ')
    print()
    for i in range(1,55):
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        x = randint(1,[(999999999),(99999999),(9999999),(999999),(99999),(9999),(999),(99)][randint(0,7)])
        print(f'( {extraSpace}{i} )',int_to_ss_col_id(x),x, end=' ')
        print_num_in_words(x,'','')


    print()
    printFramedSentences(47,' Press "enter" to continue... ')
    print()         
    input()



def showInstructions_s():
    print('''

                                                   LAS TORRES DE HANOI
        
         ╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
         ║                                                                                                     ║
         ║             ║                        ║                        ║                        ║            ║
         ║             ║                    ████████                     ║                        ║            ║
         ║             ║                   ██████████                    ║                        ║            ║
         ║             ║                  ████████████                   ║                        ║            ║
         ║             ║                 ██████████████                  ║                        ║            ║
         ║             ║                ████████████████                 ║                        ║            ║
         ║             ║               ██████████████████                ║                        ║            ║
         ║             ║              ████████████████████               ║                        ║            ║
         ║             ║             ██████████████████████              ║                        ║            ║
         ╚═════════════╚════════════════════════╚════════════════════════╚════════════════════════╚════════════╝

                                                  


        Inventado por el matemático francés Edouard Lucas en 1883. Se nos da una torre de ocho discos, inicialmente
        apilados en tamaño decreciente en una de las tres clavijas. El objetivo es transferir toda la torre a una de
        las otras clavijas, moviendo solo un disco a la vez y nunca moviendo uno más grande a uno más pequeño.

        Sabemos que la solución a esta recurrencia es: 2 a la potencia de n - 1, donde n es el número de discos.

        Además, por inducción matemática, sabemos que tenemos que mover discos n-1 más pequeños de la clavija inicial
        a la clavija de repuesto, luego mover el disco más grande de la clavija inicial a la clavija de destino;
        finalmente, mover discos n-1 de la clavija de repuesto a la clavija de destino.

        Con esta información podemos construir un algoritmo recursivo para resolver el problema. Usé el siguiente
        algoritmo para obtener los movimientos:
                                                >>> def printMove(fr, to):
                                                ...     print('Move from ' + str(fr) + ' to ' + str(to))
                                                ...
                                                >>> def Towers_4(n, fr, to, spare1, spare2):
                                                ...     if n == 1:
                                                ...         printMove(fr, to)
                                                ...     else:
                                                ...         Towers_4(n-1, fr, spare1, to, spare2)
                                                ...         Towers_4(1, fr, to, spare1, spare2)
                                                ...         Towers_4(n-1, spare1, to, spare2, fr)
                                                ...
                                                >>>
                                                >>> Towers_4(3, 1, 2, 3, 4)
                                                Move from 1 to 2
                                                Move from 1 to 3
                                                Move from 2 to 3
                                                Move from 1 to 2
                                                Move from 3 to 4
                                                Move from 3 to 2
                                                Move from 4 to 2
                                                >>>
                                               
        Un humano rápido terminaría el rompecabezas ( 8 Discos ) en unos cuatro minutos.
        ''')

    print()
    print()        
    print()
    print()         
    printFramedSentences(47,' Presione "intro" para continuar... ')
    print()
    input()




    printFramedSentences(47,' Función del generador de discos  ')
    print('''
>>> generate_disks(50)
                                                          ████████                                                   1
                                                         ██████████                                                  2
                                                        ████████████                                                 3
                                                       ██████████████                                                4
                                                      ████████████████                                               5
                                                     ██████████████████                                              6
                                                    ████████████████████                                             7
                                                   ██████████████████████                                            8
                                                  ████████████████████████                                           9
                                                 ██████████████████████████                                          10
                                                ████████████████████████████                                         11
                                               ██████████████████████████████                                        12
                                              ████████████████████████████████                                       13
                                             ██████████████████████████████████                                      14
                                            ████████████████████████████████████                                     15
                                           ██████████████████████████████████████                                    16
                                          ████████████████████████████████████████                                   17
                                         ██████████████████████████████████████████                                  18
                                        ████████████████████████████████████████████                                 19
                                       ██████████████████████████████████████████████                                20
                                      ████████████████████████████████████████████████                               21
                                     ██████████████████████████████████████████████████                              22
                                    ████████████████████████████████████████████████████                             23
                                   ██████████████████████████████████████████████████████                            24
                                  ████████████████████████████████████████████████████████                           25
                                 ██████████████████████████████████████████████████████████                          26
                                ████████████████████████████████████████████████████████████                         27
                               ██████████████████████████████████████████████████████████████                        28
                              ████████████████████████████████████████████████████████████████                       29
                             ██████████████████████████████████████████████████████████████████                      30
                            ████████████████████████████████████████████████████████████████████                     31
                           ██████████████████████████████████████████████████████████████████████                    32
                          ████████████████████████████████████████████████████████████████████████                   33
                         ██████████████████████████████████████████████████████████████████████████                  34
                        ████████████████████████████████████████████████████████████████████████████                 35
                       ██████████████████████████████████████████████████████████████████████████████                36
                      ████████████████████████████████████████████████████████████████████████████████               37
                     ██████████████████████████████████████████████████████████████████████████████████              38
                    ████████████████████████████████████████████████████████████████████████████████████             39
                   ██████████████████████████████████████████████████████████████████████████████████████            40
                  ████████████████████████████████████████████████████████████████████████████████████████           41
                 ██████████████████████████████████████████████████████████████████████████████████████████          42
                ████████████████████████████████████████████████████████████████████████████████████████████         43
               ██████████████████████████████████████████████████████████████████████████████████████████████        44
              ████████████████████████████████████████████████████████████████████████████████████████████████       45
             ██████████████████████████████████████████████████████████████████████████████████████████████████      46
            ████████████████████████████████████████████████████████████████████████████████████████████████████     47
           ██████████████████████████████████████████████████████████████████████████████████████████████████████    48
          ████████████████████████████████████████████████████████████████████████████████████████████████████████   49
         ██████████████████████████████████████████████████████████████████████████████████████████████████████████  50
>>>
        ''')

    print()
    printFramedSentences(47,' Presione "intro" para continuar... ')
    print()        
    input()





    printFramedSentences(47,' Máximo de 29 discos en 4 clavijas ')
    print()
    print()       
    print()
    print()       
    print()       
    print()
    print()       
    print()
    print()       
    print()          
    print()       

    T1 = generate_disks(29)
    rn = randint(1,4)
    if rn == 1:
        pt(29,1,2,3,4)
    elif rn == 2:
        pt(29,2,1,3,4)
    elif rn == 3:
        pt(29,3,2,1,4)
    elif rn == 4:
        pt(29,4,2,1,3)

    print()       
    print()
    print()       
    print()
    print()       
    print()       
    print()
    print()       
    print()
    print()       
    print()
    printFramedSentences(47,' Presione "intro" para continuar... ')
    print()       
    input()

    printFramedSentences(20,' Algoritmo de codificación de hojas de cálculo y algoritmo de conversión de números en palabras ')
    print()
    for i in range(1,55):
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        x = randint(1,[(999999999),(99999999),(9999999),(999999),(99999),(9999),(999),(99)][randint(0,7)])
        print(f'( {extraSpace}{i} )',int_to_ss_col_id(x),x, end=' ')
        imprimir_numeros_en_palabras(x,'','')

    print()
    printFramedSentences(47,' Presione "intro" para continuar... ')
    print()       
    input()




def printMove(fr, to):
    counter.append(1)
    arrows_r = ['ᐳ       ','=ᐳ      ','==ᐳ     ','===ᐳ    ','====ᐳ   ','=====ᐳ  ','======ᐳ ','=======ᐳ']
    arrows_l = ['       ᐸ','      ᐸ=','     ᐸ==','    ᐸ===','   ᐸ====','  ᐸ=====',' ᐸ======','ᐸ=======']
    if move_lang=='0':
        counter2 = len(counter)
        printFramedSentences(ring_length+22,f'    {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} From Peg ={arrows_r[randint(0,7)]} {fr}    ')
        printFramedSentences(ring_length+22,f'    {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]}  To  Peg ={arrows_r[randint(0,7)]} {to}    ')
        if len(str(counter2))>=3 and str(counter2).endswith('11') or len(str(counter2))>=3 and str(counter2).endswith('12') or len(str(counter2))>=3 and str(counter2).endswith('13'):
            printFramedSentences(ring_length+22,f'={arrows_r[randint(0,7)]}  {counter2}th Movement  {arrows_l[randint(0,7)]}=')
        elif (int(counter2)>20 and str(counter2).endswith('1')) or counter2==1:
            printFramedSentences(ring_length+22,f'={arrows_r[randint(0,7)]}  {counter2}st Movement  {arrows_l[randint(0,7)]}=')
        elif (int(counter2)>20 and str(counter2).endswith('2')) or counter2==2:
            printFramedSentences(ring_length+22,f'={arrows_r[randint(0,7)]}  {counter2}nd Movement  {arrows_l[randint(0,7)]}=')
        elif (int(counter2)>20 and str(counter2).endswith('3')) or counter2==3:
            printFramedSentences(ring_length+22,f'={arrows_r[randint(0,7)]}  {counter2}rd Movement  {arrows_l[randint(0,7)]}=')
        else:
            printFramedSentences(ring_length+22,f'={arrows_r[randint(0,7)]}  {counter2}th Movement  {arrows_l[randint(0,7)]}=')
        print(myConcat([ ' ' for x in range(ring_length+21) ]),f'║={arrows_r[randint(0,7)]}',end=' ')
        print_num_in_words(len(counter),'','')
        printFramedSentences(ring_length+22,f'  Spreadsheet Encoding ={arrows_r[randint(0,7)]} {int_to_ss_col_id(len(counter))}  ')
    else:
        counter2 = len(counter)
        printFramedSentences(ring_length+26,f'    {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} De La Clavija ={arrows_r[randint(0,7)]} {fr}   ')
        printFramedSentences(ring_length+26,f'    {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]} {[chr(10005),chr(10011)][randint(0,1)]}  A La Clavija ={arrows_r[randint(0,7)]} {to}   ')
        if len(str(counter2))>=2 and str(counter2).endswith('11') or len(str(counter2))>=2 and str(counter2).endswith('12') or len(str(counter2))>=2 and str(counter2).endswith('17'):
            printFramedSentences(ring_length+26,f'={arrows_r[randint(0,7)]}   {counter2}mo Movimiento   {arrows_l[randint(0,7)]}=')
        elif str(counter2).endswith('1') or str(counter2).endswith('3'):
            printFramedSentences(ring_length+26,f'={arrows_r[randint(0,7)]}   {counter2}er Movimiento   {arrows_l[randint(0,7)]}=')
        elif str(counter2).endswith('2'):
            printFramedSentences(ring_length+26,f'={arrows_r[randint(0,7)]}   {counter2}do Movimiento   {arrows_l[randint(0,7)]}=')
        elif str(counter2).endswith('4') or str(counter2).endswith('5') or str(counter2).endswith('6'):
            printFramedSentences(ring_length+26,f'={arrows_r[randint(0,7)]}   {counter2}to Movimiento   {arrows_l[randint(0,7)]}=')
        elif str(counter2).endswith('7'):
            printFramedSentences(ring_length+26,f'={arrows_r[randint(0,7)]}   {counter2}mo Movimiento   {arrows_l[randint(0,7)]}=')
        elif str(counter2).endswith('8'):
            printFramedSentences(ring_length+26,f'={arrows_r[randint(0,7)]}   {counter2}vo Movimiento   {arrows_l[randint(0,7)]}=')
        elif str(counter2).endswith('9'):
            printFramedSentences(ring_length+26,f'={arrows_r[randint(0,7)]}   {counter2}no Movimiento   {arrows_l[randint(0,7)]}=')
        else:
            printFramedSentences(ring_length+26,f'={arrows_r[randint(0,7)]}   {counter2}mo Movimiento   {arrows_l[randint(0,7)]}=')
        print(myConcat([ ' ' for x in range(ring_length+25) ]),f'║={arrows_r[randint(0,7)]}',end=' ')
        imprimir_numeros_en_palabras(len(counter),'','')
        printFramedSentences(ring_length+26,f'  Codificación de Hojas de Cálculo ={arrows_r[randint(0,7)]} {int_to_ss_col_id(len(counter))}  ')
    printTowers(fr, to)



def Towers_4(n, fr, to, spare1, spare2):
    if n == 1:
        printMove(fr, to)
    else:
        Towers_4(n-1, fr, spare1, to, spare2)
        Towers_4(1, fr, to, spare1, spare2)
        Towers_4(n-1, spare1, to, spare2, fr)

       
       
def printTowers(fr, to):
    X[to-1] = [X[fr-1][0]] + X[to-1]
    del(X[fr-1][0])
    print()
    print('  ' + ' ' + myConcat([ ' ' for x in range(ring_length//2+1) ]) + [chr(9312),chr(9461)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(9313),chr(9462)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(9314),chr(9463)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(9315),chr(9464)][randint(0,1)])
    print('  ' + ' ' + myConcat([ ' ' for x in range(ring_length//2+1) ]) + [chr(10005),chr(10011)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(10005),chr(10011)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(10005),chr(10011)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(10005),chr(10011)][randint(0,1)])
    print('  ' + chr(9556) + myConcat([ chr(9552) for x in range(ring_length//2+1) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length//2) ]) + chr(9559))
    print('  ' + chr(9553) + myConcat([ ' ' for x in range(ring_length//2+1) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553))
    print('  ' + chr(9553) + myConcat([ ' ' for x in range(ring_length//2+1) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553))
    for x in range(len(X[0])):
        print('  '+chr(9553),myConcat(X[0][x]),myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([' ' for x in range(ring_length//2)]) +chr(9553))
    for x in range(len(X[1])):
        print('  '+chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[1][x]), myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([' ' for x in range(ring_length//2)]) + chr(9553))
    for x in range(len(X[2])):
        print('  '+chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[2][x]) + ' ' * (ring_length//2) + ' ' + chr(9553) + ' ' * (ring_length//2) + chr(9553))
    for x in range(len(X[3])):
        print('  '+chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[3][x]), chr(9553))
    print('  ' + chr(9562) + myConcat([ chr(9552) for x in range(ring_length//2+1) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length//2) ]) + chr(9565))
    if move_lang == '0':
        toh_msg1 = myConcat([chr(randint(10241,10495)) for x in range(5)])+'THE'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'TOWERS'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'OF'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'HANOI'+myConcat([chr(randint(10241,10495)) for x in range(3)])+str(len(T1))+chr(randint(10241,10495))+'DISKS'+myConcat([chr(randint(10241,10495)) for x in range(5)])
        toh_msg2 = myConcat([chr(randint(10241,10495)) for x in range(5)])+'THE'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'TOWERS'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'OF'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'HANOI'+myConcat([chr(randint(10241,10495)) for x in range(3)])+str(len(T1))+chr(randint(10241,10495))+'DISKS'+myConcat([chr(randint(10241,10495)) for x in range(5)])
        toh_msg3 = [toh_msg1,toh_msg2][randint(0,1)]
        printFramedSentences(ring_length+22,toh_msg3)
    else:
        toh_msg1 = myConcat([chr(randint(10241,10495)) for x in range(5)])+'LAS'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'TORRES'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'DE'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'HANOI'+myConcat([chr(randint(10241,10495)) for x in range(3)])+str(len(T1))+chr(randint(10241,10495))+'DISCOS'+myConcat([chr(randint(10241,10495)) for x in range(5)])
        toh_msg2 = myConcat([chr(randint(10241,10495)) for x in range(5)])+'LAS'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'TORRES'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'DE'+myConcat([chr(randint(10241,10495)) for x in range(3)])+'HANOI'+myConcat([chr(randint(10241,10495)) for x in range(3)])+str(len(T1))+chr(randint(10241,10495))+'DISCOS'+myConcat([chr(randint(10241,10495)) for x in range(5)])
        toh_msg3 = [toh_msg1,toh_msg2][randint(0,1)]
        printFramedSentences(ring_length+26,toh_msg3)
    if speed=='1':
        time.sleep(1)         #time.sleep(1)  # Close to 4 minutes for 8 disks.
    if speed=='2':
        time.sleep(0.452)     #time.sleep(0.452)  # Close to 2 minutes for 8 disks.
    if speed=='3':
        time.sleep(0.217)      #time.sleep(0.217)  # Close to 1 minute for 8 disks.
    if speed=='4':
        time.sleep(0.1)        #time.sleep(0.1)    # Close to 30 seconds for 8 disks.
    if speed=='5':
        time.sleep(0.05)      #time.sleep(0.0418) # Close to 15 seconds for 8 disks.
    if speed=='6':
        time.sleep(0)         # How fast is your CPU?

   



def pt(n,fr,to,spare1, spare2):
    PEGS = 4
    T1 = generate_disks(int(n))     
    X = build_structure(PEGS, len(T1), int(to), int(spare1), int(spare2))
    ring_length = len(X[int(fr)-1][0])
    print(' ' + chr(9556) + myConcat([ chr(9552) for x in range(ring_length//2+1) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length//2) ]) + chr(9559))
    print(' ' + chr(9553) + myConcat([ ' ' for x in range(ring_length//2+1) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553))
    print(' ' + chr(9553) + myConcat([ ' ' for x in range(ring_length//2+1) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553))
    if fr==1:
        for x in range(n):
            print(' ' + chr(9553),myConcat(X[0][x]),myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([' ' for x in range(ring_length//2)]) +chr(9553))
            time.sleep(.005)
    if fr==2:
        for x in range(n):
            print(' ' + chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[1][x]), myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([' ' for x in range(ring_length//2)]) + chr(9553))              
            time.sleep(.005)
    if fr==3:
        for x in range(n):
            print(' ' + chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[2][x]) + ' ' * (ring_length//2) + ' ' + chr(9553) + ' ' * (ring_length//2) + chr(9553))
            time.sleep(.005)
    if fr==4:
        for x in range(n):
            print(' ' + chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[3][x]), chr(9553))
            time.sleep(.005)
    print(' ' + chr(9562) + myConcat([ chr(9552) for x in range(ring_length//2+1) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length//2) ]) + chr(9565))



@find_time
def T(n, fr, to, spare1, spare2):
    print('  ' + ' ' + myConcat([ ' ' for x in range(ring_length//2+1) ]) + [chr(9312),chr(9461)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(9313),chr(9462)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(9314),chr(9463)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(9315),chr(9464)][randint(0,1)])
    print('  ' + ' ' + myConcat([ ' ' for x in range(ring_length//2+1) ]) + [chr(10005),chr(10011)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(10005),chr(10011)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(10005),chr(10011)][randint(0,1)] + myConcat([ ' ' for x in range(ring_length) ]) + [chr(10005),chr(10011)][randint(0,1)])
    print('  ' + chr(9556) + myConcat([ chr(9552) for x in range(ring_length//2+1) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9552) + myConcat([ chr(9552) for x in range(ring_length//2) ]) + chr(9559))
    print('  ' + chr(9553) + myConcat([ ' ' for x in range(ring_length//2+1) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length) ]) + ' ' + myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553))
    print('  ' + chr(9553) + myConcat([ ' ' for x in range(ring_length//2+1) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553))
    if fr==1:
        for x in range(n):
            print('  '+chr(9553),myConcat(X[0][x]),myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([' ' for x in range(ring_length//2)]) +chr(9553))
    if fr==2:
        for x in range(n):
            print('  '+chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[1][x]), myConcat([ ' ' for x in range(ring_length//2) ]) + chr(9553) + myConcat([ ' ' for x in range(ring_length) ]) + chr(9553) + myConcat([' ' for x in range(ring_length//2)]) + chr(9553))            
    if fr==3:
        for x in range(n):
            print('  '+chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[2][x]) + ' ' * (ring_length//2) + ' ' + chr(9553) + ' ' * (ring_length//2) + chr(9553))
    if fr==4:
        for x in range(n):
            print('  '+chr(9553),' ' * (ring_length//2) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length) + chr(9553) + ' ' * (ring_length//2) + myConcat(X[3][x]), chr(9553))
    print('  ' + chr(9562) + myConcat([ chr(9552) for x in range(ring_length//2+1) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length) ]) + chr(9562) + myConcat([ chr(9552) for x in range(ring_length//2) ]) + chr(9565))
    print()

   
    Towers_4(n, fr, to, spare1, spare2)
   
##    if move_lang == '0':       
##        if n==1:
##            print('To transfer',n,'Disk, from Peg',fr,'to Peg',to,', takes ', end=' ')
##            print_num_in_words(len(counter),'Movement.','Movements.')
##        else:
##            print('To transfer',n,'Disks, from Peg',fr,'to Peg',to,', takes ', end=' ')
##            print_num_in_words(len(counter),'Movement.','Movements.')
##    else:
##        if n==1:
##            print('Para transferir',n,'Disco,  de la Clavija',fr,'a la Clavija',to,', toma ', end=' ')
##            imprimir_numeros_en_palabras(len(counter),'Movimiento.','Movimientos.')
##        else:
##            print('Para transferir',n,'Discos, de la Clavija',fr,'a la Clavija',to,', toma ', end=' ')
##            imprimir_numeros_en_palabras(len(counter),'Movimiento.','Movimientos.')

    return



def generate_disks(n):
    def convert_to_num(L): return [ 1 if L[x]==1 else 0 for x in range(len(L)) ]
    def convert_to_sym(L): return [ chr(9608) if L[x]==0 else ' ' for x in range(len(L)) ]       
    f = [ x for x in range(1,201) ]
    g = [ (x+2) for x in range(8,408,2) ]
    h = { f[x]: g[x] for x in range(len(g)) }
    t1 = generate_pascal_triangle(h[n])
    T1 = []
    for x in range(9):
        del(t1[0])
    for x in range(len(t1)):
        for y in range(len(t1)-x):
            t1[x].reverse()
            t1[x].append(1)
        del(t1[x][-1])
        if (len(t1)-x)%2!=0:
            T1.append(convert_to_sym(convert_to_num(t1[x])))
    return T1



def build_structure(p, d, to, spare1, spare2):
    X = [ [T1[x] for x in range(d) ] for x in range(p) ]
    X[to-1] = []
    X[spare1-1] = []
    X[spare2-1] = []
    return X


def printFramedSentences(s,msg):
    print((' ' * s)+chr(9556)+(chr(9552) * len(msg))+chr(9559))
    print((' ' * s)+chr(9553)+myConcat([ x for x in msg ])+chr(9553))
    print((' ' * s)+chr(9562)+(chr(9552) * len(msg))+chr(9565))



lucho = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1] ]


def convert_to_symbol_1(L): return [ chr(9899) if L[x]==1 else [chr(11093),chr(10060)][randint(0,1)] for x in range(len(L)) ]

def convert_to_symbol_2(L): return [ chr(11035) if L[x]==1 else [chr(10062),chr(9989)][randint(0,1)] for x in range(len(L)) ]

def convert_to_symbol_3(L): return [ chr(9899) if L[x]==1 else chr(9994) for x in range(len(L)) ]

def convert_to_symbol_4(L): return [ chr(11035) if L[x]==1 else chr(randint(9193,9196)) for x in range(len(L)) ]

def convert_to_symbol_5(L): return [ chr(9899) if L[x]==1 else chr(11088) for x in range(len(L)) ]






msg_cr = '      Copyright 2023 Lucho Manyari Yong       '.upper()
msg_re = '            Análisis de Algoritmos            '.upper()
msg_rs = '       Ingeniería y Diseño de Software        '.upper()
msg_se = '       Software Engineering and Design        '.upper()
msg_r  = '            analysis of algorithms            '.upper()
msg_n  = '             Solution for N disks             '.upper()
msg_ns = '            Solución para N discos            '.upper()
msg_l  = '             THE TOWERS OF HANOI              '.upper()
msg_s  = '             LAS TORRES DE HANOI              '.upper()
msg_m1 = [msg_l, msg_r, msg_n][randint(0,2)]
msg_m2 = [msg_s, msg_re, msg_ns][randint(0,2)]
msg_m3 = [msg_l, msg_r, msg_n, msg_s, msg_rs, msg_re, msg_ns, msg_se][randint(0,7)]

##    print()
##    print(' ',myConcat([chr(randint(10241,10495)) for x in range(96)]))
##    for x in range(len(lucho)):
##        print(msg_m1[x],chr(randint(10241,10495))+chr(randint(10241,10495))+myConcat(style1(lucho[x]))+chr(randint(10241,10495))+chr(randint(10241,10495)),msg_m2[x])
##        time.sleep(.05)
##    print(' ',myConcat([chr(randint(10241,10495)) for x in range(96)]))
##    print()
#time.sleep(3)



def lou(n):
    style1 = [convert_to_symbol_1,convert_to_symbol_2,convert_to_symbol_3,convert_to_symbol_4,convert_to_symbol_5][randint(0,4)]
    msg = [msg_se,msg_rs][randint(0,1)]
    print(' ' * (n) + '   ' + myConcat([chr(randint(10241,10495)) for x in range(96)]))
    for x in range(len(lucho)):
        print(' ' * (n) , msg_cr[x] , chr(randint(10241,10495))+chr(randint(10241,10495))+myConcat(style1(lucho[x]))+chr(randint(10241,10495))+chr(randint(10241,10495)),msg[x])
        time.sleep(.009)
    print(' ' * (n) + '   ' + myConcat([chr(randint(10241,10495)) for x in range(96)]))




cond = ' '
while cond != 'q' or cond != 's':

    move_lang = ' '
    while move_lang not in '0 1'.split():
        for x in range(6):
            msg_m3 = [msg_l, msg_r, msg_n, msg_s, msg_rs, msg_re, msg_ns, msg_se][randint(0,7)]
            nd = x+1
            T1 = generate_disks(nd)
            rn = randint(1,4)
            if rn == 1:
                pt(nd,1,2,3,4)
                printFramedSentences((x+1)*4,msg_m3.upper())
            elif rn == 2:
                pt(nd,2,1,3,4)
                printFramedSentences((x+1)*4,msg_m3.upper())
            elif rn == 3:
                pt(nd,3,2,1,4)
                printFramedSentences((x+1)*4,msg_m3.upper())
            elif rn == 4:
                pt(nd,4,2,1,3)
                printFramedSentences((x+1)*4,msg_m3.upper())
            time.sleep(0.05)

         
        print(' Choose your Language ( 0 -> English ) , Selecciona tu Idioma ( 1 -> Castellano ) :', end=' ')
        move_lang = input()

        T1 = generate_disks(29)
    if move_lang == '0':
        toh()
        print('''
                                             THE TOWERS OF  HANOI
     ╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
     ║                                                                                                     ║
     ║             ║                        ║                        ║                        ║            ║
     ║             ║                    ████████                     ║                        ║            ║
     ║             ║                   ██████████                    ║                        ║            ║
     ║             ║                  ████████████                   ║                        ║            ║
     ║             ║                 ██████████████                  ║                        ║            ║
     ║             ║                ████████████████                 ║                        ║            ║
     ║             ║               ██████████████████                ║                        ║            ║
     ║             ║              ████████████████████               ║                        ║            ║
     ║             ║             ██████████████████████              ║                        ║            ║
     ╚═════════════╚════════════════════════╚════════════════════════╚════════════════════════╚════════════╝
         ''')

        printFramedSentences(30,' Would you like to view the instructions? (yes/no) ')
        if input().lower().startswith('y'):
            showInstructions()

        style1 = [convert_to_symbol_1,convert_to_symbol_2,convert_to_symbol_3,convert_to_symbol_4,convert_to_symbol_5][randint(0,4)]
        print()
        d1 = generate_disks(8)
        print(' ' * (len(d1)//1-8) + '   ' + myConcat([chr(randint(10241,10495)) for x in range(96)]))
        for x in range(len(lucho)):
            print(' ' * (len(d1)//1-8) , msg_cr[x] , chr(randint(10241,10495))+chr(randint(10241,10495))+myConcat(style1(lucho[x]))+chr(randint(10241,10495))+chr(randint(10241,10495)),msg_se[x])
            time.sleep(.009)
        print(' ' * (len(d1)//1-8) + '   ' + myConcat([chr(randint(10241,10495)) for x in range(96)]))
        printFramedSentences(25,msg_m1.upper())
        if len(d1)==64:
            toh_msg = ' ' * (4+(len(d1)//4)) + 'THE TOWERS OF BRAHMA'
        elif len(d1)==8:
            toh_msg = ' ' * (4+(len(d1)//4)) + 'THE TOWERS OF HANOI'
        else:
            toh_msg = ' ' * (1+(len(d1)//4)) + f'THE TOWERS OF HANOI PLUS {len(d1)-8}'
        print()
        for x in range(len(d1)):
            print(' ' * 35,myConcat(d1[x]),x+1)
            time.sleep(.009)
        print()
        print(' ' * (29 + len(d1)),'{} Disks ='.format(len(d1)),2**len(d1)-1,'Moves')
        print()
        #snake_string_pythonic(toh_msg)
        toh_msg2 = ' ' * (4+(len(d1)//4)) + 'Solution for N disks'.upper()
        #snake_string_pythonic(toh_msg2)
        disks = ' '
        while disks not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29'.split():
            print(' ' * (len(d1)+16),'How many Disks do you want to solve? (From 1 to 29) :', end=' ')
            disks = input()
        tab = ['1','2','3','4']
        fr = ' '
        while fr not in tab:
            print(' ' * (len(d1)+16),'Which peg do you want to start from? ( 1, 2, 3 or 4 ) :', end=' ')
            fr = input()
        tab.remove(fr)
        to = ' '
        while to not in tab:
            print(' ' * (len(d1)+16),f'Which peg do you want to transfer the disks to? ({tab[0]}, {tab[1]} or {tab[2]}) :', end=' ')
            to = input()
        tab.remove(to)
        spare1 = tab[0]
        spare2 = tab[1]
        speed = ' '
        while speed not in '1 2 3 4 5 6'.split():
            print(' ' * (len(d1)+16),'Enter the speed ( 1 to 6 ) :', end=' ')
            speed = input()
        
    if move_lang == '1':
        toh_s()
        print('''
                                             LAS TORRES DE HANOI
     ╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
     ║                                                                                                     ║
     ║             ║                        ║                        ║                        ║            ║
     ║             ║                    ████████                     ║                        ║            ║
     ║             ║                   ██████████                    ║                        ║            ║
     ║             ║                  ████████████                   ║                        ║            ║
     ║             ║                 ██████████████                  ║                        ║            ║
     ║             ║                ████████████████                 ║                        ║            ║
     ║             ║               ██████████████████                ║                        ║            ║
     ║             ║              ████████████████████               ║                        ║            ║
     ║             ║             ██████████████████████              ║                        ║            ║
     ╚═════════════╚════════════════════════╚════════════════════════╚════════════════════════╚════════════╝
         ''')

        printFramedSentences(33,' Le gustaria ver las instrucciones? (si/no) ')
        if input().lower().startswith('s'):
            showInstructions_s()

        style1 = [convert_to_symbol_1,convert_to_symbol_2,convert_to_symbol_3,convert_to_symbol_4,convert_to_symbol_5][randint(0,4)]
        print()
        d1 = generate_disks(8)
        print(' ' * (len(d1)//1-8) + '   ' + myConcat([chr(randint(10241,10495)) for x in range(96)]))
        for x in range(len(lucho)):
            print(' ' * (len(d1)//1-8) , msg_cr[x] , chr(randint(10241,10495))+chr(randint(10241,10495))+myConcat(style1(lucho[x]))+chr(randint(10241,10495))+chr(randint(10241,10495)),msg_rs[x])
            time.sleep(.009)
        print(' ' * (len(d1)//1-8) + '   ' + myConcat([chr(randint(10241,10495)) for x in range(96)]))
        printFramedSentences(25,msg_m2.upper())
        if len(d1)==64:
            toh_msg = ' ' * (4+(len(d1)//4)) + 'LAS TORRES DE BRAHMA'
        elif len(d1)==8:
            toh_msg = ' ' * (4+(len(d1)//4)) + 'LAS TORRES DE HANOI'
        else:
            toh_msg = ' ' * (1+(len(d1)//4)) + f'LAS TORRES DE HANOI MÁS {len(d1)-8}'
        print()
        for x in range(len(d1)):
            print(' ' * 35,myConcat(d1[x]),x+1)
            time.sleep(.009)
        print()
        print(' ' * (26 + len(d1)),'{} Discos ='.format(len(d1)),2**len(d1)-1,'Movimientos')
        print()
        #snake_string_pythonic(toh_msg)
        toh_msg2 = ' ' * (4+(len(d1)//4)) + 'Solución para N discos'.upper()
        #snake_string_pythonic(toh_msg2)
        disks = ' '
        while disks not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29'.split():
            print(' ' * (len(d1)+16),'Cuantos Discos quieres resolver? (Del 1 al 29) :', end=' ')
            disks = input()
        tab = ['1','2','3','4']
        fr = ' '
        while fr not in tab:
            print(' ' * (len(d1)+16),'En que Clavija quieres comenzar? ( 1, 2, 3 '+chr(243)+' 4 ) :', end=' ')
            fr = input()
        tab.remove(fr)
        to = ' '
        while to not in tab:
            print(' ' * (len(d1)+16),f'A que Clavija vas a transferir los discos? ({tab[0]}, {tab[1]} ó {tab[2]}) :', end=' ')
            to = input()
        tab.remove(to)
        spare1 = tab[0]
        spare2 = tab[1]
        speed = ' '
        while speed not in '1 2 3 4 5 6'.split():
            print(' ' * (len(d1)+16),'Pon la velocidad ( del 1 al 6 ) :', end=' ')
            speed = input()

          
    print()
    counter = []
    PEGS = 4
    T1 = generate_disks(int(disks))    
    X = build_structure(PEGS, len(T1), int(to), int(spare1), int(spare2))
    ring_length = len(X[int(fr)-1][0])
    T(int(disks), int(fr), int(to), int(spare1), int(spare2))


    if move_lang == '0':
        print()
        print()
        cond=input('      Press "enter" to Play again! or type "Q" and Press "enter" to quit: ')
        print()
        if(cond.lower().startswith('q')):
            snake_string_pythonic('  thank*you*for*playing!'.upper())
            print()
            print('      G\vo\vo\vd\v \vB\vy\ve\v!\v')
            printFramedSentences(20,' The key to immortality is first living a life worth remembering. - Bruce Lee '.upper())
            break

    if move_lang == '1':
        print()
        print()
        cond=input('      Presione "intro" para Jugar nuevamente! ó teclee "S" y Presione "intro" para salir: ')
        print()
        if(cond.lower().startswith('s')):
            snake_string_pythonic('  gracias*por*jugar!'.upper())
            print()
            print('      H\va\vs\vt\va\v \vL\va\v \vV\vi\vs\vt\va\v!\v')
            printFramedSentences(20,' La clave de la inmortalidad es primero vivir una vida que valga la pena recordar. - Bruce Lee '.upper())
            break


