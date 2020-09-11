# Цикл
# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.

list_of_numbers = range(10)

for number in list_of_numbers:
    print(number+1)

# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.

input_string = input("Enter a string: ")

for letter in input_string:
    print(letter)

#     Оценки
# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

print("Задание про оценки")

# Sample for testing
# list_of_scores = [{'school_class': '1a', 'scores': [5,5,5,5,5]},
#                     {'school_class': '2a', 'scores': [5,5,5,5,5]},
#                     {'school_class': '3a', 'scores': [5,5,5,5,5]},
#                     {'school_class': '4a', 'scores': [5,5,5,5,5]}]

list_of_scores = [{'school_class': '1a', 'scores': [3,4,4,5,2]},
                    {'school_class': '2a', 'scores': [4,5,4,5,5]},
                    {'school_class': '3a', 'scores': [3,3,4,3,3]},
                    {'school_class': '4a', 'scores': [3,3,4,4,4]}]

sum_of_scores = 0

for school_class in list_of_scores: 
    average_of_class = sum(school_class['scores'])/len(school_class['scores'])
    school_class_name = school_class['school_class']
    print(f'Средний балл класса {school_class_name}: {average_of_class}')
    sum_of_scores += average_of_class 
    #sum_of_scores += sum(school_class['scores'])/len(school_class['scores'])

print(f'Средний балл по всей школе {sum_of_scores/len(list_of_scores)}.')