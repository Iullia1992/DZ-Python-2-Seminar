# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите число '))

# f = 1
# for i in range(N):
#    i = i + 1
#    f = i * f
    
#    print(f, end=" ")



# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример: Для n = 5: сумма = 11,55

# n = int(input('Введите количество чисел в списке '))

# def numbers(n):
#    summ = 0
#    for i in range(n):
#        a = int(input(f'Введи число {i + 1} '))
#       a = (1+1/a)**a
#        summ = a + summ
#        i += 1
#    return summ

#print('Сумма чисел равна',round((numbers(n)), 2))



# Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
# from random import Random, randint

# N = int(input('Введите число '))
# numbers = []
# for i in range(N):
#    numbers.append(randint(-N,N+1))
# print(numbers)

# def smes(numbers):
#    list = numbers[:]
#    numbers_length = len(list)
#    for i in range(numbers_length):
#        index = randint(0, numbers_length - 1)
#        temp = list[i]
#        list[i] = list[index]
#        list[index] = temp
#    return list
# print(smes(numbers))