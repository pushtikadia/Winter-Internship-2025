numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_numbers_count = 0
for num in numbers:
    if num > 0:
        positive_numbers_count += 1
        print("Count of positive numbers:", positive_numbers_count)