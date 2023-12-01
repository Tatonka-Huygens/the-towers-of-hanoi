# Helper function to print number from 1 to 999.
# number: number from 1 to 999

from snake_string import snake_string_pythonic
from random import *


#snake_string_pythonic('    NUMBERS TO WORDS')



def print_3_digits(number):
    #basic_lookup[0] is empty. We want basic_lookup[1] to map to 'One' and so on.
    basic_lookup = [ '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
                    'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
                    'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                    'Seventeen', 'Eighteen', 'Nineteen' ]
    #tens_lookup[0] and tens_lookup[1] are empty.
    #We want tens_lookup[2] to map to 'Twenty' and so on.
    tens_lookup = [ '', '', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty',
                    'Seventy', 'Eighty', 'Ninety' ]

    #Suppose number is 987, then hundreds_digits is 9
    hundreds_digit = number // 100
    if (hundreds_digit > 0):
        print(basic_lookup[hundreds_digit] + ' Hundred ', end='')
    #Suppose number is 987, then remainder will be 87
    remainder = number % 100
    if (remainder > 0):
        if (remainder <= 19):
            print(basic_lookup[remainder] + ' ', end='')
        else:
            tens_digit = remainder // 10
            unit_digit = remainder % 10
            print(tens_lookup[tens_digit] + ' ', end='')
            print(basic_lookup[unit_digit] + ' ', end='')



# Main function to print te number in words.
# number: any number from 0 to 999999999.


def print_num_in_words(number,singular,plural):
    remainder = number % 1000000000
    # If number is 0, handle it there and return.
    if (number == 0):
        print(f'Zero {plural}')
        return


    # Suppose number is 123456789, then millions = 123, remainder = 456789.
    millions = number // 1000000
    remainder = remainder - (millions * 1000000)

    # Suppose remainder = 456789, then thousands = 456, remainder = 789.
    thousands = remainder // 1000
    remainder = remainder - (thousands * 1000)

    if (millions > 0):
        print_3_digits(millions)
        print('Million ', end='')

    if (thousands > 0):
        print_3_digits(thousands)
        print('Thousand ', end='')

    if (remainder == 0):
        print()
    
    if (remainder > 0):
        print_3_digits(remainder)
        if (number == 1):
            print(f'{singular}')
        else:
            print(f'{plural}')

       
        




from spreadsheet_encoding import *

##for x in range(999999999):
##    print_num_in_words(x+1)


##for i in range(1,41):
##    if i < 10:
##        extraSpace = ' ' 
##    else:
##        extraSpace = ''
##    x = randint(1,[(999999999),(99999999),(9999999),(999999),(99999),(9999),(999),(99)][randint(0,7)])
##    print(f'( {extraSpace}{i} )',int_to_ss_col_id(x),x, end=' ')
##    print_num_in_words(x,'','')
##
##






    


    

    
                    
