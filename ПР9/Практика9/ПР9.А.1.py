x = int(input("x="))
n = int(input("n="))

# объявление рекурсивной функции для вычисления факториала
def factorial(n):
  if n < 0:
    # генерируем исключение если n отрицательно
    raise ValueError("Факториал не определен для отрицательных чисел")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)


# объявление рекурсивной функции для вычисления x в степени n
def f(x, n):
  if n < 0:
    # генерируем исключение, если n отрицательно
    raise ValueError("Степень не определена для отрицательных чисел")
  elif n == 0:
    return 1
  else:
    return x * f(x, n - 1)

# объявление функции для вычисления выражения x^n / n!
def fact(x, n):
  if n < 0:
    raise ValueError("Выражение не определено для отрицательных n")
  else:
    return f(x, n) / factorial(n)

# вызываем функцию fact для вычисления результата
result = fact(x,n)
print(f"{x}^{n}/{n}!={result}")