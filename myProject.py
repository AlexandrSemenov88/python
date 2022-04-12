from functions import *

def main():
    menu()
def function_calculator():
    function = int(input("Выберите калькулятор: "))
    while function > 0:
        if function == 1:
            workingCalculator.calculator()

        elif function == 2:
            workingCalculator.currency_converter()
        elif function == 3:
            workingCalculator.time_calculator()
        elif function == 4:
            workingCalculator.leap_year()
        function_exit = int(input("Главное меню 2, для продолжения нажмите 1, для выхода в меню нажмите 0: "))
        if function_exit == 0:
            function_calculator()
        elif function_exit == 2:
            menu()

def mathematical_function():
    function2 = int(input("Выберите математиескую функцию: "))
    while function2 > 0:
        if function2 == 1:
            workingMathematics.fibonacci()
        elif function2 == 2:
            workingMathematics.compares_numbers()
        elif function2 == 3:
            workingMathematics.factorial()
        elif function2 == 4:
            workingMathematics.titration()
        function_exit2 = int(input("Главное меню 2, для продолжения нажмите 1, для выхода в меню нажмите 0: "))
        if function_exit2 == 0:
            mathematical_function()
        elif function_exit2 == 2:
            menu()

def geometric_function():
    function3 = int(input("Выберите геометрическую функцию: "))
    while function3 > 0:
        if function3 == 1:
            workingGeometric.triangle()
        elif function3 == 2:
            workingGeometric.pascal()
        function_exit3 = int(input("Главное меню 2, для продолжения нажмите 1, для выхода в меню нажмите 0: "))
        if function_exit3 == 0:
            geometric_function()
        elif function_exit3 == 2:
            menu()

def set_tuple_dict_list_function():
    function4 = int(input("Выберите функцию списки, кортежи, словари, множества: "))
    while function4 > 0:
        if function4 == 1:
            workinglist.list_sorted()    # Сортировка списков
        elif function4 == 2:
            workinglist.merging_lists()   # Совпадение чисел в списках
        elif function4 == 3:
            workinglist.polin()              # Список палиндром
        elif function4 == 4:
            workinglist.list_dividing()       # Делитель списка
        elif function4 == 5:
            workingtuple.tuple_sorted()         # Сортировка кортежа
        elif function4 == 6:
            workingtuple.merging_tuple()         # Совпадение чисел в кортежах и построение списка
        elif function4 == 7:
            workingtuple.tuple_dividing()         # Делитель кортежа
        elif function4 == 8:
            workingSet.set_sorted()           # Сортировка множества
        elif function4 == 9:
            workingSet.set_dividing()     # Делитель множества
        function_exit4 = int(input("Главное меню 2, для продолжения нажмите 1, для выхода в меню нажмите 0: "))
        if function_exit4 == 0:
            set_tuple_dict_list_function()
        elif function_exit4 == 2:
            menu()

def menu():
    while True:
        try:
            function_big = int(input("Калькулятор - 1 \n"
                                     "Математические функции - 2 \n"
                                     "Геометрические функции - 3 \n"
                                     "Функции словари, кортежи,списки,множества - 4 \n"
                                     "Выберите функцию: \n"))
            while function_big > 0:
                if function_big == 1:
                    function = int(input("Калькулятор - 1 \n"
                                         "Конвертор валют - 2 \n"
                                         "Калькулятор времени - 3 \n"
                                         "Калькулятор високосный год - 4 \n: "))
                    while function > 0:
                        if function == 1:
                            workingCalculator.calculator()
                        elif function == 2:
                            workingCalculator.currency_converter()
                        elif function == 3:
                            workingCalculator.time_calculator()
                        elif function == 4:
                            workingCalculator.leap_year()
                        function_exit = int(
                            input("Главное меню 2, для продолжения нажмите 1, для выхода в меню нажмите 0: "))
                        if function_exit == 0:
                            function_calculator()
                        elif function_exit == 2:
                            menu()
                elif function_big == 2:
                    function2 = int(input("Последовательность Фибоначи - 1 \n"
                                          "Вычетание из большего числа - 2 \n"
                                          "Факториал - 3 \n"
                                          "Тетрация - 4 \n: "))
                    while function2 > 0:
                        if function2 == 1:
                            workingMathematics.fibonacci()
                        elif function2 == 2:
                            workingMathematics.compares_numbers()
                        elif function2 == 3:
                            workingMathematics.factorial()
                        elif function2 == 4:
                            workingMathematics.titration()
                        function_exit2 = int(
                            input("Главное меню 2, для продолжения нажмите 1, для выхода в меню нажмите 0: "))
                        if function_exit2 == 0:
                            mathematical_function()
                        elif function_exit2 == 2:
                            menu()
                elif function_big == 3:
                    function3 = int(input("Треугольник - 1 \n"
                                          "Треугольник Паскаля - 2 \n: "))
                    while function3 > 0:
                        if function3 == 1:
                            workingGeometric.triangle()
                        elif function3 == 2:
                            workingGeometric.pascal()
                        function_exit3 = int(
                            input("Главное меню 2, для продолжения нажмите 1, для выхода в меню нажмите 0: "))
                        if function_exit3 == 0:
                            geometric_function()
                        elif function_exit3 == 2:
                            menu()
                elif function_big == 4:
                    function4 = int(input("Сортировка списков - 1 \n"
                                          "Совпадение чисел в списках - 2 \n "
                                          "Список палиндром - 3 \n"
                                          "Делитель списка - 4 \n"
                                          "Сортировка кортежа - 5 \n"
                                          "Совпадение чисел в кортежах и построение списка - 6 \n"
                                          "Делитель кортежа - 7 \n"
                                          "Сортировка множества - 8 \n"
                                          "Делитель множества - 9 \n: "))
                    while function4 > 0:
                        if function4 == 1:
                            workinglist.list_sorted()  # Сортировка списков
                        elif function4 == 2:
                            workinglist.merging_lists()  # Совпадение чисел в списках
                        elif function4 == 3:
                            workinglist.polin()  # Список палиндром
                        elif function4 == 4:
                            workinglist.list_dividing()  # Делитель списка
                        elif function4 == 5:
                            workingtuple.tuple_sorted()  # Сортировка кортежа
                        elif function4 == 6:
                            workingtuple.merging_tuple()  # Совпадение чисел в кортежах и построение списка
                        elif function4 == 7:
                            workingtuple.tuple_dividing()  # Делитель кортежа
                        elif function4 == 8:
                            workingSet.set_sorted()  # Сортировка множества
                        elif function4 == 9:
                            workingSet.set_dividing()  # Делитель множества
                        function_exit4 = int(
                            input("Главное меню 2, для продолжения нажмите 1, для выхода в меню нажмите 0: "))
                        if function_exit4 == 0:
                            set_tuple_dict_list_function()
                        elif function_exit4 == 1:
                            function_big
                        elif function_exit4 == 2:
                            menu()

                function_big_exit = int(input("Для продолжения нажмите 1, для выхода в меню нажмите 0: "))

                if function_big_exit == 0:
                    menu()

        except ValueError:
            print("Input correct value\n")

main()

