# def countdown(n):
#     if n <= 0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n-1)


# countdown(5)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
        print(value)