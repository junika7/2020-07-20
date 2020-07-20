def func(num1: int):
    factorial = 1
    for i in range(1, num1+1):
        factorial *= i
    print(factorial)

func(5)
