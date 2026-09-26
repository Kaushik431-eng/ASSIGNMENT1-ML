# question 1

my_integer = 50
my_float = 10.10
my_complex = 3 + 4j
my_string = "This is my first assignment in machine learning"
my_boolean = True

print("Integer:", my_integer, "| Type:", type(my_integer))
print("Float:", my_float, "| Type:", type(my_float))
print("Complex:", my_complex, "| Type:", type(my_complex))
print("String:", my_string, "| Type:", type(my_string))
print("Boolean:", my_boolean, "| Type:", type(my_boolean))

# question 2

my_string = "this is my first python llm programe"

print("length:", len(my_string))

print("uppercase:", my_string.upper())

modified_string = my_string.replace("llm", "ml")
print("modified string:", modified_string)

# question 3

import math

n1 = 20
n2 = 30

print("sum:", n1 + n2)
print("difference:", n1 - n2)
print("product:", n1 * n2)
print("division:", n1 / n2)

print("square of n2:", n2**2)
print("cube of:", n2**3)
print("square root of n2", math.sqrt(n2))

print("remainder of n1 and n2 :", n1 / n2)


# question 4


my_list = [10, 20, "kaushik", 12.12]

print("first element:", my_list[1])
print("last element:", my_list[-1])
print("second to three element:", my_list[1:2])


# question 5
my_list = ["kaushik", "zain", "aashish", "mahipat", "mansi"]
print("my list :", my_list)

my_list.append("prince")
print("after append:", my_list)

my_list.remove("mansi")
print("after remove:", my_list)

print("is 'kaushik' my list :", "kaushik" in my_list)
print("is 'mansi' my list ", "mansi" in my_list)

# Sorting a numerical list since mixed types cannot be sorted directly

num_list = [
    20,
    23,
    56,
    78,
]

num_list.sort()
print("sorted numerical list:", num_list)

my_list.reverse()
print("reverse my list:", my_list)


# question 6

my_dict = {"name": "kaushik chavda", "course": "MCA", "semester": 1}

print("value of 'name':", my_dict["name"])

my_dict["university"] = "GLS"
print("after adding", my_dict)

del my_dict["semester"]
print("after removing:", my_dict)

print("is 'name'a key", "name" in my_dict)

# question 7

int_to_str = str(500)
print("Integer to String:", int_to_str, type(int_to_str))
str_to_int = int("500")
print("String to Integer:", str_to_int, type(str_to_int))
float_to_int = int(9.81)
print("Float to Integer:", float_to_int, type(float_to_int))
str_to_list = list("KAUSHIK")
print("String to List:", str_to_list, type(str_to_list))


# question 8

is_raining = False
is_sunny = True

is_good_day = not is_raining and is_sunny
print("it is a good day ?", is_good_day)


# question 9
num = 51
print("input:", num)

if num / 100 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

    # question 10
num = -10.10

print("input:", num)
if num > 0:
    print("positive")
elif num < 0:
    print("nagative")
else:
    print("zero")


# question 11
for i in range(10, 22):
    print(i, end=" ")


# question 12
total_sum = sum(range(10, 100))
print("sum of the number from 10 to 100:", total_sum)


# question 13
n = 10
print(f"Table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# question 14

for i in range(1, 4):
    print(f"Table of {i}:")
for j in range(1, 6):
    print(f"{i} x {j} = {i * j}")
print("-" * 15)
