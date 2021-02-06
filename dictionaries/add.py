# EX  1
thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"
print(thisdict)
# Output {'brand': 'Food', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# EX  2
thisdict = {"brand": "Food", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})
print(
    thisdict
)  # Output {'brand': 'Food', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
