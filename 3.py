def count_vowels(string):
    abc = "euioaEUIOA"
    count = 0
    for i in string:
        if i in abc:
            count += 1
    return count


q = (input("Введіть строку - "))
print("Кількість голосних букв у рядку:", count_vowels(q))