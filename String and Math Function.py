import math

word = input("Enter a word: ").strip()
value = float(input("Enter a decimal number: "))

ceil_value = math.ceil(value)
floor_value = math.floor(value)

print(f"You entered '{word.capitalize()}'")
print(f"Ceiling value: {ceil_value}")
print(f"Floor value: {floor_value}")
