# Helper function to print number from 1 to 999.
# number: number from 1 to 999

from snake_string import snake_string_pythonic
import random


#snake_string_pythonic('    numeros en palabras'.upper())



def imprimir_3_digitos(number):
    #basic_lookup[0] is empty. We want basic_lookup[1] to map to 'One' and so on.
    basic_lookup = [ '', 'Un', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis',
                    'Siete', 'Ocho', 'Nueve', 'Diez', 'Once', 'Doce',
                    'Trece', 'Catorce', 'Quince', 'Dieciseis',
                    'Diecisiete', 'Dieciocho', 'Diecinueve'] 
    #tens_lookup[0] and tens_lookup[1] are empty.
    #We want tens_lookup[2] to map to 'Twenty' and so on.
    tens_lookup = [ '', '', 'Veinte', 'Treinta', 'Cuarenta', 'Cincuenta', 'Sesenta',
                    'Setenta', 'Ochenta', 'Noventa' ]

    hundreds_lookup = [ '', 'Ciento', 'Doscientos', 'Trescientos', 'Cuatrocientos',
                        'Quinientos', 'Seiscientos', 'Setecientos', 'Ochocientos',
                        'Novecientos', ]

    #Suppose number is 987, then hundreds_digit is 9
    hundreds_digit = number // 100
                    
    if (hundreds_digit > 0):
        if (number == 100):
            print('Cien ', end='')
        else:
            print(hundreds_lookup[hundreds_digit] + ' ', end='')


    #Suppose number is 987, then remainder will be 87
    remainder = number % 100
    if (remainder > 0):

        if (remainder <= 19):
            print(basic_lookup[remainder] + ' ', end='')
        elif remainder==21:
            print('Veintiún' + ' ', end='')
        elif remainder==22:
            print('Veintidos' + ' ', end='')
        elif remainder==23:
            print('Veintitres' + ' ', end='')
        elif remainder==24:
            print('Veinticuatro' + ' ', end='')
        elif remainder==25:
            print('Veinticinco' + ' ', end='')
        elif remainder==26:
            print('Veintiseis' + ' ', end='')
        elif remainder==27:
            print('Veintisiete' + ' ', end='')
        elif remainder==28:
            print('Veintiocho' + ' ', end='')
        elif remainder==29:
            print('Veintinueve' + ' ', end='')         
        else:
            tens_digit = remainder // 10
            unit_digit = remainder % 10
            print(tens_lookup[tens_digit] + ' ', end='')
            if (unit_digit == 0):
                print(basic_lookup[unit_digit] + ' ', end='')
            else:
                print('y',basic_lookup[unit_digit] + ' ', end='')



# Main function to print the number in words.
# number: any number from 0 to 999999999.


def imprimir_numeros_en_palabras(number,singular,plural):
    remainder = number % 1000000000
    # If number is 0, handle it there and return.
    if (number == 0):
        print(f'Cero {plural}')
        return

    # Suppose number is 123456789, then millions =123, remainder = 456789.
    millions = number // 1000000
    remainder = remainder - (millions * 1000000)

    # Suppose remainder = 456789, then thousands = 456, remainder = 789

    thousands = remainder // 1000
    remainder = remainder - (thousands * 1000)

    if (millions > 0):
        imprimir_3_digitos(millions)
        if (number >= 2000000):
            print('Millones ', end='')
        if (number == 1000000 or number <= 1999999):
            print('Millón ', end='')

    if (thousands > 0):
        imprimir_3_digitos(thousands)
        print('Mil ', end='')

    if (remainder == 0):
        print()

    if (remainder > 0):
        imprimir_3_digitos(remainder)
        if (number == 1):
            print(f'{singular}')
        else:
            print(f'{plural}')
            

       


##for i in range(1,51):
##    x = randint(0,[(999999999),(99999999),(9999999),(999999)][randint(0,3)])
##    counter2 = i
##    if i < 10:
##        extraSpace = ' ' 
##    else:
##        extraSpace = ''
##    if len(str(counter2))>=2 and str(counter2).endswith('11') or len(str(counter2))>=2 and str(counter2).endswith('12') or len(str(counter2))>=2 and str(counter2).endswith('17'):
##        print(f'   ({extraSpace} {counter2}mo )',x, end=' ')
##        imprimir_numeros_en_palabras(x,random.choice(['Movimiento','Sol','Dolar','Credito']),random.choice(['Movimientos','Soles','Dolares','Creditos']))
##    elif str(counter2).endswith('1') or str(counter2).endswith('3'):
##        print(f'   ({extraSpace} {counter2}ro )',x, end=' ')
##        imprimir_numeros_en_palabras(x,random.choice(['Movimiento','Sol','Dolar','Credito']),random.choice(['Movimientos','Soles','Dolares','Creditos']))
##    elif str(counter2).endswith('2'):
##        print(f'   ({extraSpace} {counter2}do )',x, end=' ')
##        imprimir_numeros_en_palabras(x,random.choice(['Movimiento','Sol','Dolar','Credito']),random.choice(['Movimientos','Soles','Dolares','Creditos']))
##    elif str(counter2).endswith('4') or str(counter2).endswith('5') or str(counter2).endswith('6'):
##        print(f'   ({extraSpace} {counter2}to )',x, end=' ')
##        imprimir_numeros_en_palabras(x,random.choice(['Movimiento','Sol','Dolar','Credito']),random.choice(['Movimientos','Soles','Dolares','Creditos']))
##    elif str(counter2).endswith('7'):
##        print(f'   ({extraSpace} {counter2}mo )',x, end=' ')
##        imprimir_numeros_en_palabras(x,random.choice(['Movimiento','Sol','Dolar','Credito']),random.choice(['Movimientos','Soles','Dolares','Creditos']))
##    elif str(counter2).endswith('8'):
##        print(f'   ({extraSpace} {counter2}vo )',x, end=' ')
##        imprimir_numeros_en_palabras(x,random.choice(['Movimiento','Sol','Dolar','Credito']),random.choice(['Movimientos','Soles','Dolares','Creditos']))
##    elif str(counter2).endswith('9'):
##        print(f'   ({extraSpace} {counter2}no )',x, end=' ')
##        imprimir_numeros_en_palabras(x,random.choice(['Movimiento','Sol','Dolar','Credito']),random.choice(['Movimientos','Soles','Dolares','Creditos']))
##    else:
##        print(f'   ( {counter2}mo )',x, end=' ')
##        imprimir_numeros_en_palabras(x,random.choice(['Movimiento','Sol','Dolar','Credito']),random.choice(['Movimientos','Soles','Dolares','Creditos']))
##    
##
##
##
##
##
##



from spreadsheet_encoding import *


##for i in range(1,41):
##    if i < 10:
##        extraSpace = ' ' 
##    else:
##        extraSpace = ''
##    x = randint(1,[(999999999),(99999999),(9999999),(999999),(99999),(9999),(999),(99)][randint(0,7)])
##    print(f'( {extraSpace}{i} )',int_to_ss_col_id(x),x, end=' ')
##    imprimir_numeros_en_palabras(x,'','')
##
##
