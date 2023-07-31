# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonachi(n: int):
    fib_1, fib_2 = 0, 1
    for x in range(n):
        yield fib_2
        fib_1, fib_2 = fib_2, fib_1 + fib_2


for x in fibonachi(7):
    print(x)