#module1.py

print("-------- running {0} ". format(__name__))

def prinThis(header, d):
    print('\n\n-----------------------')
    print('********** {0} **********'.format(header))
    for key, value in d.items():
        if key=='__builtins__':
            print("*** ", key)
            for v in value:
                print("      --- ", v)
        else:
            print(key,' --- ', value, ' --- ', type(value))
    print('---------------------------')

prinThis('module1.globals', globals())

print('---------------- end of {0} -------------------'.format(__name__))
 