try:
    x = int(input('podaj x'))
    y = int(input('podaj y'))
    print('dzielenie ', x/y)
    raise Exception('spam', 'eggs')
except ZeroDivisionError :
    print('dzielenie przez zero')
except ValueError :
    print('zła wartosc')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    # x, y = inst.args     # unpack args
    # print('x =', x)
    # print('y =', y)