# Задание
# Перепишите функцию discounted(price, discount, max_discount=20)из урока про функции так,
# чтобы она перехватывала исключения, когда переданы некорректные аргументы (например, строки вместо чисел).

def discounted(price, discount, max_discount = 20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Максимальная скидка не может быть больше 99%')
    if discount >= max_discount:
        price_with_discount = price
    else: 
        price_with_discount = price - price * discount / 100
    return price_with_discount

price = input('Enter the price: ')
discount = input('Enter the discount: ')
max_discount = input('Enter max. discount: ')

try:
    print(discounted(price,discount,max_discount))
except ValueError:
    print("You should have typed NUMBERS everywhere!")