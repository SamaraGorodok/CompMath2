import graphic
import inp
import func


def get_initial_data():
    DATA = {}
    fn, method, fn2 = inp.inp()
    if (method==1 or method == 2 ):
        x,funct = func.get_function(fn)
        graphic.graphic(x, funct(x))
        DATA['funct'] = funct
    if (method==3):
        x, func1 = func.get_system(fn)
        x, func2 = func.get_system(fn2)
        DATA['func1'] = func1
        DATA['func2'] = func2

    try:
        answ = None
        DATA['method'] = method
        DATA['x'] = x



        if (method==1) or (method==2):
            a,b = single_sol_borders(x,funct)
            DATA['a'] = a
            DATA['b'] = b

        if (method==3):
            x_in = sys_sol_borders(x,func1)
            DATA['a1'] = x_in
            y_in = sys_sol_borders(x, func2)
            DATA['a2'] = y_in
        DATA['accuracy']=accuracy_solver()
    except ValueError:
        pass
    return DATA

def single_sol_borders(x,funct):
    while True:
        try:
            print("\n Choose your borders")
            a, b = map(float, input("\n Type here: ").split())
            if (a == b):
                print("left border and right boder can't be same")
                raise ArithmeticError
            if (funct(a) * funct(b) > 0):
                print("ERROR")
                raise ArithmeticError
            if (a > b):
                print("left border is bigger than right")
                raise ArithmeticError
        except ValueError:
            print("Type a number")
        except ArithmeticError:
            print("error! Try again")
        else:
            break
    return a,b




def sys_sol_borders(x, funct):
    while True:
        try:
            print("\n Choose initial approximation")
            a = float( input("\n Type here: "))
            return a
            break
        except ValueError:
            print("Type a number")
        else:
            break

def accuracy_solver():
    while True:
        try:
            print("\n Choose accuracy")

            accuracy = float(input("\n Type here: "))
            if accuracy>0:
                raise ValueError
        except ValueError:
            print("Type a number, number must be >0")
        else:
            return accuracy
            break
        return accuracy

