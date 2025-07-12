# Prompt the user to input their current age
# input() reads a string, so we convert it to an integer using int()
current_age = int(input("How old are you? "))

# Calculate how old the user will be in 2050
# Assuming current year is 2023, 2050 - 2023 = 27 years
future_age = current_age + 27

# Print the user's age in 2050
print(f"In 2050, you will be {future_age} years old.")