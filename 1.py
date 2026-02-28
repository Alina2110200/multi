nums_input = input("Введіть числа через пробіл: ")

nums_list = nums_input.split()

numbers = []

for num in nums_list:
    numbers.append(int(num))

unique_nums = set(numbers)

print("Унікальні елементи:", unique_nums)