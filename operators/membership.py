# Ex1
string = " Hello world "
print("H" in string)
# Output : True
print("hELLO" not in string)
# Output : True

# Ex2
dictObject = {"name": "Me &  Mate", "age": "21"}
print("name" in dictObject)
# Output : True
print("Me & Mate" in dictObject)
# Output : False

# Ex3
number_list = [1, 2, 3]
print(1 in number_list)
# Output :True
print(5 in number_list)
# Output :False

# Ex 5
name_list = ["Me", "Mate"]
print("Me" in name_list)
# Output :True
print("You" in name_list)
# Output :False
