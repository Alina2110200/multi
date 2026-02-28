set1 = set(input("Введіть 10 чисел для першої множини: ").split())
set2 = set(input("Введіть 10 чисел для другої множини: ").split())

print("Перша множина:", set1)
print("Друга множина:", set2)

print("Спільні елементи:", set1 & set2)
print("Різниця: ", set1 - set2)
print("Об'єднання:", set1 | set2)