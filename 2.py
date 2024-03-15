def a(number):
    if number <= 1:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

number = int(input("Введіть число - "))
if a(number):
    print(number, "є простим числом")
else:
    print(number, "не є простим числом")