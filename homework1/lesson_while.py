# Задание
# Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
# Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
# Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соответствующий ответ. Например:
# Пользователь: Что делаешь?
# Программа: Программирую

def ask_user():
    user_input = input("Как дела? ")
    return user_input

while True:
    user_say = ask_user()
    if user_say == "Хорошо":
        break
    else:
        ask_user()

# пока код плохо работает. Мне почему то надо два раза писать "Хорошо", чтобы программа остановилась.