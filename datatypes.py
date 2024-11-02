# Integer

# test
int_a = 10
int_b = 3
int_sum = int_a + int_b
int_product = int_a * int_b
print(f"Integer Operations: Sum = {int_sum}, Product = {int_product}")

# Float
float_a = 5.7
float_b = 2.3
float_sum = float_a + float_b
float_div = float_a / float_b
print(f"Float Operations: Sum = {float_sum}, Division = {float_div}")

# String
string_a = "Hello"
string_b = "World"
concatenated_string = string_a + " " + string_b
string_length = len(concatenated_string)
print(f"String Operations: Concatenated = '{concatenated_string}', Length = {string_length}")

# List
list_a = [1, 2, 3, 4]
list_a.append(5)
list_sum = sum(list_a)
print(f"List Operations: Appended List = {list_a}, Sum = {list_sum}")

# Tuple
tuple_a = (10, 20, 30)
tuple_sum = sum(tuple_a)
print(f"Tuple Operations: Tuple = {tuple_a}, Sum = {tuple_sum}")

# Set
set_a = {1, 2, 3, 4}
set_a.add(5)
set_b = {3, 4, 5, 6}
set_union = set_a.union(set_b)
print(f"Set Operations: Set A = {set_a}, Set B = {set_b}, Union = {set_union}")

# Dictionary
dict_a = {"name": "Alice", "age": 25}
dict_a["city"] = "New York"
age = dict_a.get("age")
print(f"Dictionary Operations: Updated Dictionary = {dict_a}, Age = {age}")

# Boolean
is_greater = int_a > int_b
is_equal = float_a == float_b
print(f"Boolean Operations: is_greater = {is_greater}, is_equal = {is_equal}")
