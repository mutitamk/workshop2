int1 = 5
int2 = 5

string1 = "Hello"
string2 = "Hello"

float1 = 0.1
float2 = 0.1

print(int1 is int2)
print(string1 is string2)
print(float1 is float2)

# True
# True
# True

dict1 = {"name": "mutita", "age": "26"}
dict2 = {"name": "mutita", "age": "26"}
dict3 = dict1

print(dict1 is dict3)
print(dict1 is dict2)
print(dict1 == dict2)

# True
# False
# True

# Tuple, Set, List
