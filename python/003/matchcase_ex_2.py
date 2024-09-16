x = 5.6567567567567567567567567

match x: 
    case bool():
        print('bool')
    case str():
        print('string')
    case float():
        print('float')
    case int():
        print('int')
    case _:
        print('non primitive')