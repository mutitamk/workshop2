# EX  1
thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
# Output {'brand': 'Food', 'year': 1964}

# EX  2
thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)
# Output {'brand': 'Food', 'model': 'Mustang'}

# EX  3
thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)
# Output {'brand': 'Food', 'year': 1964}

# EX  4
thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
# Output {}