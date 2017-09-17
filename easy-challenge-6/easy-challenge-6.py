from decimal import *
import math

def chudnovsky(k):
    total = Decimal(0)
    for x in range(0, k + 1):
        total += (Decimal(-1)**x)*(Decimal(math.factorial(6*x)) \
                /((math.factorial(x)**3)*(math.factorial(3*x)))* (13591409+545140134*x)\
                /(640320**(3*x)))
    total = total * Decimal(10005).sqrt()/4270934400
    total = total**(-1)

    return total

def get_int(phrase):
    val = input(phrase)
    while not val.isdigit():
        print('Not a positive integer, try again.')
        val = input(phrase)
    return abs(int(val))

def main():
    iterations = get_int('What iterative degree would you like? ')
    decimals = get_int('What number of decimals? ')
    getcontext().prec = decimals
    print('Pi: {}'.format(chudnovsky(iterations)))

if __name__ == '__main__' : main()
