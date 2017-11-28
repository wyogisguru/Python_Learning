#-------------------------------------------------------------------------------
# Name:        Quadratic Formula...
# Purpose:     Learning...
#
# Author:      cbrink
#
# Created:     17/09/2015
#-------------------------------------------------------------------------------
import math
import time

def my_main():
    # Assign variables a, b, c from the quadratic function...
    a = raw_input('What is the coefficient of x^2 term, a?')
    b = raw_input('What is the coefficient of x term, b?')
    c = raw_input('What is the constant of the function, c?')

    a = float(a)
    b = float(b)
    c = float(c)

    # Execute quadratic formula to find the x-intercepts, zeros, or roots...
    x1 = -b/(2*a) + math.sqrt(b**2-4*a*c)/(2*a)
    x2 = -b/(2*a) - math.sqrt(b**2-4*a*c)/(2*a)

    # Print solution...
    print('The x-intercepts are %s and %s.' % (x1, x2))
    time.sleep(10)

if __name__ == '__main__':
    my_main()


