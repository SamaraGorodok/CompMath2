import derivative


def simple_iteration(func1, func2, a, a1, a2, maxitr=100):
    # def g(g_x):
    #     return g_x + (-1 / derivative.der(f(g_x))) * f(g_x)
    # x = g(x0)
    iter = 0
    prev1,prev2 = a1,a2
    while iter<maxitr:
        curr1,curr2 = func1(prev1,prev2), func2(prev1,prev2)
        if abs(curr1 - curr2)< a or abs(curr2-prev2)< a or iter>maxitr:
            break
        if curr1 > 10000:
            print("RASHODISYA")
            return
        iter+=1
        prev1,prev2 = curr1,curr2
        print(curr1,curr2)

    # while (abs(x - x0) > a) and (iter < maxitr):
    #     if derivative.der(g(x)) >=1:
    #         return None
    #     x0,x = x, g(x)
    #     iter+=1
    print("x")
    print(curr1)
    print("y")
    print(curr2)
    print("f(x)")
    print(func1(curr1,curr2))
    print("iter")
    print(iter)