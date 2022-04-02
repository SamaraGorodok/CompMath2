import derivative
from derivative import der
from dill.source import getsource


def s_iteration(a, b, f, accuracy):
    iter = 0
    # print(a)
    # print(b)
    # print(getsource(f))
    print("derivatives:")
    # print("a")
    des_a = der(f)(a)
    des_b = der(f)(b)
    # print(des_a)
    # print("b")
    # print(des_b)


    # max = -1/ max(des_a,des_b)
    if (der(f)(a) > der(f)(b)):
        max = (-1) / des_a
    else:
        max = -1 / des_b

    fi = lambda x: x + max * f(x)

    fi_der = derivative.der(fi)

    fi_a = fi_der(a)
    fi_b = fi_der(b)
    print(fi_a)
    print(fi_b)

    if (abs(fi_a) > 1 or abs(fi_b) > 1):
        print("doesent attach requierments")
        root = None


    previous = a
    x = b

    while (abs(x-previous) > accuracy) or (abs(f(x)) > accuracy):
        print(x, previous, f(x))
        x = fi(previous)
        previous = x

        if (iter > 100):
            print("function diverges")
            exit()

        iter += 1
    # root = x
    print("iterations")
    print(iter)
    print("x= ")
    print(x)
    print("\n y= ")
    print(f(x))
    # print("root= " + root)

