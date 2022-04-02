import func


def inp():
    print("Lab 2 (14) Ryabikin Aleksey \n Github: @SamaraGorodok")
    print("\nChoose your type\n"+"choose your function")

    inp_type = int

    print("Choose: \n 1: single \n 2: system")
    while(inp_type!=1 and inp_type!=2):
        try:
            inp_type = int(input("\n Type here: "))
        except ValueError:
            print("Type a number")
        else:
            break


    # одиночное уравнение
    if (inp_type == 1):
        func_num=int
        method_num=int

        print("Choose: \n")
        print("\n1:2.3x^3 + 5.x^2 - 7.41x - 10.6" +
              "\n2:x^2 + 50 +2.24x" +
              "\n3:4,3cos(x) + cos(x) - 5")
        while (func_num != 1 and func_num != 2 and func_num !=3 ):
            try:
                func_num = int(input("\n Type here: "))
            except ValueError:
                print("Type a number")
            else:
                break

        print("Choose your method: \n")
        print("\n1:chords method" +
              "\n2:simple iteration")
        while (method_num != 1 and method_num !=2):
            try:
                method_num = int(input("\n Type here: "))
            except ValueError:
                print("Type a number")
            else:
                break

        return func_num,method_num,None



    # система уравнений
    if (inp_type == 2):
        method_num = 3
        func_num =int
        print("Choose: \n")
        print("1:x**2 + y**2 - 4", "\n2: x**3 + y - 1","\n 3:x**2 - y - 3")

        while (func_num != 1 and func_num != 2 and func_num != 3):
            try:
                func_num1 = int(input("\n Type here: "))
                try:
                    func_num2 = int(input("\n Second function: "))
                except ValueError:
                    print("Type a number")
                else:
                    break
            except ValueError:
                print("Type a number")
            else:
                break

        return func_num1,method_num,func_num2,

