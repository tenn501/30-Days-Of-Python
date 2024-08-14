"""Day 2: 30 Days of Python programming"""
first_name = "Tom"
last_name = "Smith"
full_name = "Tom Smith"
country = "UK"
city = "London"
age = 10
school, language, score = "Oxford", "English", 100
print(type(first_name))
print(len(city))
print(len(city) > len(country))
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30
radius = input()
print(radius)
area_of_circle = 3.14 * int(radius) ** 2
user = {"first_name": input("First name: "), "last_name": input("Last name: "), "age": int(input("Age: "))}
print(user)