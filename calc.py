# basic calculator code in python 
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# the code below will add the two numbers
result_sum = first_number + second_number
print("Sum:", result_sum)

# the code below will subtract the two numbers
result_subtraction = first_number - second_number
print("Subtraction:", result_subtraction) 
# the code below will multiply the two numbers
result_multiplication = first_number * second_number
print("Multiplication:", result_multiplication)

# the code below will divide the two numbers
result_division = first_number / second_number
print("Division:", result_division)

# the code below will raise first_number to the power of second_number
print("Power:", first_number ** second_number)

# the code below will perform floor division
print("Floor Division:", first_number // second_number)

# the code below will find the modulus
print("Modulus:", first_number % second_number)

# the code below will perform bitwise AND (only works with integers)
print("Bitwise AND:", int(first_number) & int(second_number))