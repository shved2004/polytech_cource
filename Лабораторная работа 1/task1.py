numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

filtered_numbers = [i for i in numbers if i]
for i, value in enumerate(numbers):
    if value is None:
        numbers[i] = sum(filtered_numbers)/(len(numbers))
print("Измененный список:", numbers)
