# from myProject import *
def main():
    pass

class set_operation:
    def __init__(self):
       pass

    def set_dividing(self): # Делитель множества

        y = set(map(int, input("Введите список: ").split()))
        x = int(input("Введите делитель: "))
        for i in y:
            if i % x == 0:
                 print(i)

    def set_sorted(self): # Сортировка множества
        y = set(map(int, input("Введите список: ").split()))
        sorted_set = sorted(y)
        print(sorted_set)

workingSet = set_operation()

class tuple_operation:
    def __init__(self):
       pass

    def tuple_dividing(self): # Делитель списка
        tuple1 = tuple(map(int, input("Введите список: ").split()))
        x = int(input("Введите делитель: "))
        for i in range(len(tuple1)):
            if tuple1[i] % x == 0:
                print(tuple1[i],end=(","))

    def merging_tuple(self): # Совпадение чисел в кортежах и построение списка
        tuple1 = tuple(map(int, input("Введите список: ").split()))
        tuple2 = tuple(map(int, input("Введите второй список: ").split()))
        result = []
        for i in range(len(tuple1)):
            for g in range(len(tuple2)):
                if tuple1[i] == tuple2[g]:
                    result.append(tuple1[i])
        print(result)

    def tuple_sorted(self): # Сортировка кортежа
        (y) = tuple(map(int, input("Введите список: ").split()))
        sorted_tuple = tuple(sorted(y))
        print(sorted_tuple)

workingtuple = tuple_operation()

class listOperation:
    def __init__(self):
       pass

    def list_dividing(self): # Делитель списка

        list1 = list(map(int, input("Введите список: ").split()))
        x = int(input("Введите делитель: "))

        for i in range(len(list1)):
            if list1[i] % x == 0:

                print(list1[i],end=(","))

    def polin(self): # Список палиндром
        s = input("Введите список: ")
        l = len(s)
        for i in range(l//2):
            if s[i] != s [-1-i]:
                print("не палиндром")
            else:
                print("палиндром")

    def merging_lists(self): # Совпадение чисел в списках
        list1 = list(map(int, input("Введите список: ").split()))
        list2 = list(map(int, input("Введите второй список: ").split()))
        result = []
        for i in range(len(list1)):
            for g in range(len(list2)):
                if list1[i] == list2[g]:
                    result.append(list1[i])
        print(result)

    def list_sorted(self): # Сортировка списков

        a = list(map(int, input("Введите список: ").split()))

        f = []
        for i in a:
            f.append(i)
        f.sort(reverse=True)
        print(f)
        f.sort()
        print(f)

workinglist = listOperation()

class calculatorOperation:
    def __init__(self):
       pass

    def calculator(self): # Калькулятор
        numbers = int(input('введите ваше число: '))
        numbers1 = int(input('введите второе число: '))
        operation = input('введите арифметическую операцию: ')
        if operation == "+":
            print(numbers + numbers1)
        if operation == "*":
            print(numbers * numbers1)
        if operation == "-":
            if operation == numbers > numbers1:
                print(numbers - numbers1)
            else:
                print(numbers1 - numbers)
        if operation == "/":
            if operation == numbers > numbers1:
                print(numbers / numbers1)
            else:
                print(numbers1 / numbers)


    def currency_converter(self): # Конвертор валют
        rubls = int(input("введите сумму рубли: "))
        name = int(input("код валюты: "))
        dollar = rubls / 73
        evro = rubls / 84

        if name == 400:
            if round(dollar % 10) == 1:
                print(round(dollar), "доллар")
            elif round(dollar % 10) == 2 or round(dollar % 10) == 3 or round(dollar % 10) == 4:
                print(round(dollar), "доллара")
            else:
                print(round(dollar), "долларов")

        elif name == 401:
            print(round(evro), "Евро")
        else:
            print("Error")


    def time_calculator(self): # Калькулятор времени
        y = int(input("Введите количество секунд: "))
        years = y / 86400 / 30 / 12
        years1 = y % (86400 * 30 * 12)
        if int(years % 10) == 1:
            if int(years % 100) == 11:
                print(int(years), "лет")
            else:
                print(int(years), "год")
        elif int(years % 10) == 2 or int(years % 10) == 3 or int(years % 10) == 4:
            if int(years % 100) == 12 or int(years % 100) == 13 or int(years % 100) == 14:
                print(int(years), "лет")
            else:
                print(int(years), "года")
        else:
            print(int(years), "лет")
        month = years1 / 86400 / 30
        month1 = years1 % (86400 * 30)
        if int(month % 10) == 1:
            if int(month % 100) == 11:
                print(int(month), "месяцев")
            else:
                print(int(month), "месяц")
        elif int(month % 10) == 2 or int(month % 10) == 3 or int(month % 10) == 4:
            if int(month % 100) == 12 or int(month % 100) == 13 or int(month % 100) == 14:
                print(int(month), "месяцев")
            else:
                print(int(month), "месяца")
        else:
            print(int(month), "месяцев")
        week = month1 / 604800
        week1 = month1 % 604800
        if int(week % 10) == 1:
            if int(week % 100) == 11:
                print(int(week), "недель")
            else:
                print(int(week), "неделя")
        elif int(week % 10) == 2 or int(week % 10) == 3 or int(week % 10) == 4:
            if int(week % 100) == 12 or int(week % 100) == 13 or int(week % 100) == 14:
                print(int(week), "недель")
            else:
                print(int(week), "недели")
        else:
            print(int(week), "недель")
        days = week1 / 86400
        days1 = week1 % 86400
        if int(days % 10) == 1:
            if int(days % 100) == 11:
                print(int(days), "дней")
            else:
                print(int(days), "день")
        elif int(days % 10) == 2 or int(days % 10) == 3 or int(days % 10) == 4:
            if int(days % 100) == 12 or int(days % 100) == 13 or int(days % 100) == 14:
                print(int(days), "дней")
            else:
                print(int(days), "дня")
        else:
            print(int(days), "дней")
        hours = days1 / 3600
        hours1 = days1 % 3600
        if int(hours % 10) == 1:
            if int(hours % 100) == 11:
                print(int(hours), "часов")
            else:
                print(int(hours), "час")
        elif int(hours % 10) == 2 or int(hours % 10) == 3 or int(hours % 10) == 4:
            if int(hours % 100) == 12 or int(hours % 100) == 13 or int(hours % 100) == 14:
                print(int(hours), "часов")
            else:
                print(int(hours), "часа")
        else:
            print(int(hours), "часов")
        minutes = hours1 / 60
        minutes1 = hours1 % 60
        if int(minutes % 10) == 1:
            if int(minutes % 100) == 11:
                print(int(minutes), "минут")
            else:
                print(int(minutes), "минута")
        elif int(minutes % 10) == 2 or int(minutes % 10) == 3 or int(minutes % 10) == 4:
            if int(minutes % 100) == 12 or int(minutes % 100) == 13 or int(minutes % 100) == 14:
                print(int(minutes), "минут")
            else:
                print(int(minutes), "минуты")
        else:
            print(int(minutes), "минут")
        seconds = minutes1 / 60
        seconds1 = minutes1 % 60
        if int(minutes1 % 10) == 1:
            if int(minutes1 % 100) == 11:
                print(int(minutes1), "секунд")
            else:
                print(int(minutes1), "секунда")
        elif int(minutes1 % 10) == 2 or int(minutes1 % 10) == 3 or int(minutes1 % 10) == 4:
            if int(minutes1 % 100) == 12 or int(minutes1 % 100) == 13 or int(minutes1 % 100) == 14:
                print(int(minutes1), "секунд")
            else:
                print(int(minutes1), "секунды")
        else:
            print(int(minutes1), "секунд")

    def leap_year(self): # Калькулятор високосный год
        years = int(input("Введите год: "))

        if int(years % 100) == 0:
            print((years), (years % 100), "не високосный год")
        if int(years % 4) == 0 or int(years % 400) == 0:
            print((years), "високосный год")
        else:
            print((years), "не високосный год")

workingCalculator = calculatorOperation()

class mathematicsOperation:
    def __init__(self):
       pass

    def compares_numbers(self):  # Вычетание из большего числа
        numbers1 = int(input("введите первое число: "))
        numbers2 = int(input("введите второе число: "))
        numbers3 = int(input("введите третье число: "))
        if numbers1 >= numbers2 <= numbers3:
            print(numbers2)
        elif numbers2 >= numbers1 <= numbers3:
            print(numbers1)
        else:
            print(numbers3)
        if numbers1 <= numbers2 >= numbers3:
            print(numbers2)
        elif numbers2 <= numbers1 >= numbers3:
            print(numbers1)
        else:
            print(numbers3)


    def factorial(self): # Факториал
        y = int(input("Факториал числа: "))
        x = 1
        for i in range(1, y + 1):
            x = x * i
        print("factorial = ", x)

    def fibonacci(self): # Последовательность Фибоначи
        fibonacci = int(input("Введите число последовательности фибонначи: "))
        i = 1
        x = 1
        print(x, i, end=" ")
        z = 2
        while i < fibonacci:
            i, x = x, i + x
            print(x, end=" ")
            z += 1

    def titration(self): # Тетрация
        x = int(input("Тетрация числа: "))
        for i in range(1, 5):
            x = (x * x)
        print(x)

workingMathematics = mathematicsOperation()

class geometricOperation:
    def __init__(self):
       pass

    def triangle(self):
        y = int(input("Число строк: "))
        for i in range(y):
            for g in range(i + 1):
                g = i + 1
                print(g, end=" ")
            print()


    def pascal(self):
        n = int(input("Число строк: "))
        count = n
        for g in range(1, n + 1):
            c = 1
            for i1 in range(1, count):
                print(" ", end="")

            for i in range(1, g + 1):
                print(c, end=" ")
                c = int(c * (g - i) / i)
            print()
            count -= 1

workingGeometric = geometricOperation()







if __name__ == '__main__':
    main()
