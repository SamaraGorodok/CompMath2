import derivative


def chord_method(a,b,f,accuracy):
    itr = 0
    max = 1000
    if ((f(a) * derivative.der(f)(a))<0):
        x=a
        fix = b
    if (f(b) * derivative.der(f)(a)<0):
        x=b
        fix = a
    else:
        x = a - (b-a) / ((f(b)-f(a))*f(a))
        fix = None
    x_init = x + 2 * accuracy
    while ((abs(x-x_init) > accuracy) and (itr<max)):
        if fix != None:
            x_init =x
            x = (fix -x)/ (f(fix)-f(x))*f(x)
        if (itr>1000):
            print("расходится")
            break
        if fix == None:
            if f(a)*f(x)<0:
                b=x
            else:
                a=x
            x_init = x
            x = a - (b-a)/(f(b)-f(a))*f(a)
        itr+=1
    print("root is: ")
    print(x)
    print("f(x) in root: ")
    print(f(x))
    print("on iteration: ")
    print(itr)
