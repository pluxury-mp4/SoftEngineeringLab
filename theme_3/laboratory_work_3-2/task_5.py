# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
# Напишите программу, которая определяет номер купе,
# в котором находится место с заданным номером
# (нумерация мест сквозная, начинается с 1).

seat = int(input("Введите номер места: "))
compartment = (seat - 1) // 4 + 1
print(compartment)
