# Задача 8. Перестановка цифр
# Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
# Формат входных данных. На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.
# Формат выходных данных. Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке: abc, acb, bac, bca, cab, cba.

num = input("Введите трёхзначное число, в котором все цифры различны: ")

a, b, c = num[0], num[1], num[2]

print(num)
print(a + c + b)
print(b + a + c)
print(b + c + a)
print(c + a + b)
print(c + b + a)
