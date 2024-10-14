from enum import member

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

new_number_4 = sum(numbers[0:4] + numbers[5:]) / len(numbers)
numbers[4] = new_number_4

print(f"Измененный список: {numbers}")
