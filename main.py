import chord_method
import inp
import simple_iteration
import simple_iteration_system
import solution


def main():
    Data = solution.get_initial_data()
    if Data['method'] == 1:
        chord_method.chord_method(Data['a'],Data['b'],Data['funct'],Data['accuracy'])
    elif Data['method'] == 2:
        simple_iteration.s_iteration(Data['a'],Data['b'],Data['funct'],Data['accuracy'])
    elif Data['method'] == 3:
        simple_iteration_system.simple_iteration(Data['func1'],Data['func2'],Data['accuracy'],Data["a1"],Data["a2"])


main()