from colorama import Fore, Style, Back
import sys
from fractions import Fraction

subscript = str.maketrans("0123456789n-", "₀₁₂₃₄₅₆₇₈₉ₙ₋")
superscript = str.maketrans("0123456789-n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻ⁿ")

al = '\u03B1'
be = '\u03B2'

bracket_open = str(Fore.RED + '(' + Style.RESET_ALL)
bracket_close = str(Fore.RED + ')' + Style.RESET_ALL)
add_symbol = Fore.RED + ' + ' + Style.RESET_ALL
equal_symbol = Fore.RED + ' = ' + Style.RESET_ALL
multiply_symbol = Fore.RED + 'x' + Style.RESET_ALL
divide_symbol = Fore.RED + '/' + Style.RESET_ALL
minus_symbol = Fore.RED + ' - ' + Style.RESET_ALL
cyan = Fore.CYAN
red = Fore.RED 
green = Fore.GREEN
reset = Style.RESET_ALL
white = Back.WHITE + Fore.BLACK
yelllow = Back.YELLOW + Fore.BLACK
magenta = Fore.MAGENTA
yel = Fore.YELLOW

statement = cyan + "By Newton's Theorem, aSₙ + bSₙ₋₁ + c = 0" + reset
lst = []
S_print = green + 'S' + reset

def f_input():
    a, b, c = input(cyan + 'Please enter the values of a, b and c ' + reset).split()     
    n = input(cyan + 'Value of power (n)? ' + reset)
    lst.extend([a, b, c, n])     
    try:
        return int(a), int(b), int(c), int(n)
    except ValueError:
        print(magenta + '\n All values must be an integer \n Please try again \n' + reset)
        sys.exit()
#---------------------------------------------------------------------------------------------

def cases(n):
    if n < 0:
        negative(n, a, b, c)
        sys.exit()
    if n == 0:
        sups = '0'.translate(superscript)
        print('\n' + al + sups + add_symbol + be + sups)
        print('1' + add_symbol + '1' + green + ' (a' + sups + '=1)')
        print(yelllow + ' 2 ' + reset + '\n')
    else:
        print('\n' + green + 'Sₙ = ' + al + 'ⁿ' + ' + ' + be + 'ⁿ' + reset)
        poop = main(n, a, b, c)

#-------------------------------------------------------------------------------------------------------------------------------
def negative(n, a, b, c):
    sups = str(n).translate(superscript)
    print('\n' + al + sups + add_symbol + be + sups )
    sups = str(n*-1).translate(superscript)
    frac1, frac2,  meh = '1' + divide_symbol + al + sups, '1' + divide_symbol + be + sups, 'a' + 'n'.translate(superscript),
    sups2, frac3 = '-n'.translate(superscript), '1/' + meh
    n = n*-1
    print(frac1 + ' + ' + frac2 + green + ' (a' + sups2 + ' = ' + frac3 + ')' + reset)
    print(bracket_open + al + sups + add_symbol + be + sups + bracket_close + divide_symbol + al + sups + be + sups)
    subs = str(n).translate(subscript)
    print(green + 'S' +  subs + divide_symbol + bracket_open + al + be + bracket_close + sups + reset + '  (S' + subs + ' = ' + al + sups + "+" + be + sups + ')')
   
    print('\n' + al + be + equal_symbol + 'c' + divide_symbol + 'a' + equal_symbol +  str(Fraction(c/a)))
    print(yel + bracket_open + al + be + bracket_close + sups + equal_symbol + str(Fraction((c/a)**n)) + reset)
    prod = (c/a)**n
    print(yelllow + ' ' + str(Fraction(prod)) + ' ' + reset)

    print('\n' + white + ' Finding S' + subs + ' = ' + al + sups + "+" + be + sups +  reset)
    summ = main(n, a, b, c)
    print(green + 'S' +  subs + divide_symbol + bracket_open + al + be + bracket_close + sups + reset + '  (S' + subs + ' = ' + al + sups + "+" + be + sups + ')')
    print(str(summ) + divide_symbol + str(prod))
    print(yelllow + ' ' + str(Fraction(summ/prod)) + ' ' + reset)

#----------------------------------------------------------------------------------------------------------

def main(n, a, b, c):
    print('\n' + al + add_symbol + be + equal_symbol + '-b/a' + equal_symbol + green + str(Fraction(-b/a)) + reset)

    if n == 1:
        print(yelllow + ' ' + -b/a + ' ' + reset)
        return -b/a

    sups = '2'.translate(superscript)
    print('\n' + al + sups + add_symbol + be + sups + equal_symbol + bracket_open + al + add_symbol + be + bracket_close + sups + add_symbol + '-2' + al + be)
    print(al + sups + add_symbol + be + sups + equal_symbol + bracket_open + '-b' + divide_symbol + 'a' + bracket_close + sups + add_symbol + '-2' + bracket_open + 'c' + divide_symbol + 'a' + bracket_close)
    print(al + sups + add_symbol + be + sups + equal_symbol + bracket_open + str(Fraction(-b/a)) + bracket_close + sups + minus_symbol+ '2' + bracket_open + str(Fraction(c/a)) + bracket_close)
    print(al + sups + add_symbol + be + sups + equal_symbol + str(Fraction((-b/a)**2)) + ' - ' + str(Fraction(2*(c/a))))
    print(al + sups + add_symbol + be + sups + equal_symbol + green + str(Fraction((-b/a)**2 - 2*(c/a))) + reset)
    s_2 = -b/a
    s_1 = (-b/a)**2 - 2*(c/a)

    if n == 2:
        print(yelllow + ' ' + Fraction(str(s_2)) + ' ' + reset + '\n')
        return s_2

    powr = 3

    while powr != n+1:
        subs = str(powr).translate(subscript)
        print('\n' + statement)
        print(yel + 'n=' + str(powr) + ': '+ reset + str(a) + S_print + subs + add_symbol + str(b) + multiply_symbol + str(Fraction(s_1)) + add_symbol + str(c) + multiply_symbol + str(Fraction(s_2)) + equal_symbol + '0')
        print(str(a) + S_print + subs + add_symbol + str(Fraction(b*s_1)) + add_symbol + str(Fraction(c*s_2)) + equal_symbol + '0')
        S = b*s_1 + c*s_2
        print(str(a) + S_print + subs + add_symbol + str(Fraction(str(S))) + equal_symbol + '0')
        S = S*-1
        print(str(a) + S_print + subs + equal_symbol + str(Fraction(S)))
        S = S/a
        print(green + 'S = ' + str(Fraction(S)) + reset)
        s_2, s_1 = s_1, S
        powr += 1

    print(yelllow + ' ' + str(Fraction(s_1)) + ' ' + reset)
    print(reset + '\n')
    return Fraction(s_1)
        


#body
sups = 'n'.translate(superscript)
sups2 = '2'.translate(superscript)
print('\n' + green + 'This program finds the value for ' + 
    al + sups + '+' + be + sups + ', for any integer n and ' + al + ' and ' + be + 
    ' being the zeroes of the equation ax' + sups2 + ' + bx + c.')

a, b, c, n = f_input()
cases(n)
