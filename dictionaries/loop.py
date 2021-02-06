thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}

# EX  1
for key in thisdict:
    print(key)
# Output :
# brand
# model
# year

thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}

# EX  2
for key in thisdict:
    print(thisdict[key])
# Output :
# Food
# Mustang
# 1964

thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}

# EX  3
for key in thisdict.keys():
    print(key)
# Output :
# brand
# model
# year

thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}

# EX  4
for value in thisdict.values():
    print(value)
# Output :
# Food
# Mustang
# 1964

thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}

# EX  5
for key, value in thisdict.items():
    print(key, value)
# Output :
# brand Food
# model Mustang
# year 1964
