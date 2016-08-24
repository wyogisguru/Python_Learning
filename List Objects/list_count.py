#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cbrink
#
# Created:     02/08/2016
# Copyright:   (c) cbrink 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def num_check():
    listMHs = ['092MH001', '092MH002', '092MH002', '092MH002']
    mhsChecked = []

    for mh in listMHs:
        if mhsChecked.count(mh) == 0:
            mhsChecked.append(mh)
            if listMHs.count(mh) == 1:
                print(str(mh) + ' found ' + str(listMHs.count(mh)) + ' occurence.')
            elif listMHs.count(mh) >= 3:
                print(str(mh) + ' found ' + str(listMHs.count(mh)) + ' occurences.')
        elif mhsChecked.count(mh) == 1:
            pass
# ------------------------------------------------------------------------------
num_check()





