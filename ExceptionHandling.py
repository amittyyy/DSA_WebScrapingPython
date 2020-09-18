def divby(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error:- You tried to divide by zero.")


print(divby(2))
print(divby(10))
print(divby(0))
print(divby(10))