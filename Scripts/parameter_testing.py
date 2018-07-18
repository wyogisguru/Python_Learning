def func_test(x=None, y=None):
    if x:
        text1 = 'x is holding a value.'
        text2 = "'This is some text. {0}'".format(text1)
        print(text2)
    else:
        print('x is {0}'.format(x))


func_test(y=1)

