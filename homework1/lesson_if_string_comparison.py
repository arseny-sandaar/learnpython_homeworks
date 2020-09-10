# Практика: Сравнение строк
# Написать функцию, которая принимает на вход две строки
# Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
# Если строки одинаковые, вернуть 1
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

def get_two_strings(string1,string2):
    
    if bool(not string1) and bool(not string2):
        return 0
    else:
        if string1 == string2:
            return 1
        elif len(string1) > len(string2) and string2 == "learn":
            return '2 and 3'
        elif len(string1) > len(string2):
            return 2
        elif string2 == "learn":
            return 3
        else:
            return "There's nothing to say about your strings"


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print(get_two_strings(string1,string2))
