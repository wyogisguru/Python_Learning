#-------------------------------------------------------------------------------
# Name:        List Comprehensions
# Purpose:     Learning list comprehensions
#
# Author:      cbrink
#
# Created:     17/09/2015
#-------------------------------------------------------------------------------
def main1():
    nums = range(10)
    evens = []
    for x in nums:
        if (x%2 == 0):
            evens.append(x)
    print(evens)

def main2():
    nums = range(10)
    evens = [x for x in nums if x%2 == 0]
    print(evens)
# ------------------------------------------------------------------------------
def main3():
    cursor = range(10)
    idList1 = [rowVal for row in cursor (rowVal = row)]
    print(idList1)
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main3()
