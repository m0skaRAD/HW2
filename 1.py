def n(numbers):
    t = sum(numbers)
    c = len(numbers)
    return t / c if c != 0 else 0

list = [1, 2, 3, 4, 5]
print("Середнє значення списку чисел:", n(list))