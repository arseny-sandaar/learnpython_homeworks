# Задание
# Перепишите функцию ask_user() из задания про while, 
# чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
# и завершала работу при помощи оператора break

def ask_user():
    user_input = input("Как дела? ")
    return user_input

try:
    while True:
        if ask_user() == "Хорошо":
            break
except KeyboardInterrupt:
    print("Пока!")