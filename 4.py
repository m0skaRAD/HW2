def nsd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Введіть перще число - "))
b = int(input("Введіть перще число - "))
print("Найбільший спільний дільник чисел" ,a, "і" ,b, "є:", nsd(a, b))