# Day 2: 30 Days of python programming
first_name = "Bilkisu"
last_name =" Bashir"
full_name = first_name + last_name
print(full_name)
country  = "Nigeria"
city = "Kano"
age = 34
year = 1990
is_married = "yes married"
is_true = "yes"
is_light_on = "yes it is on"
apple,orange,mango,banana = 2,3,1,2

# To check the type of each variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(apple))
print(type(orange))
print(type(mango))
print(type(banana))

# to see the length of first_name
print(len(first_name))

# Compare the length of your first name and your last name

# Define first and last names
first_name = "Bilkisu"
last_name = "Bashir"

# Compare their lengths
if len(first_name) > len(last_name):
    print("The first name is longer.")
elif len(first_name) < len(last_name):
    print("The last name is longer.")
else:
    print("Both names are of equal length.")




num_one = 5
num_two = 4
# Addition
total = num_one + num_two
print(total)

#Subtraction
diff = num_one - num_two
print(diff)

# multiplication
product = num_one * num_two
print(product)

# Division
division = num_one / num_two
print(division)

# modulus
remainder = num_two % num_one
print(remainder)

# floor_division
floor_division = num_one // num_two
print(floor_division)



# Calculating area of a circle
# Given radius
import math
radius = 30
area_of_circle = math.pi * radius**2
print("The area of the circle is:", area_of_circle)


# Calculate the circumference of the circle
circum_of_circle = 2 * math.pi * radius
print("The circumference of the circle is:", circum_of_circle)

6
# Take radius as user input and calculate the area
radius = float(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius**2

# Print the result for user input
print("The area of the circle with radius", radius, "is:", area_of_circle)



# input data from the user

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

# Print the values to confirm
#print("\nUser Details:")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)
