table = [
    ("marley", "5"),
    ("bob", "99"),
    ("another name", "3")
]

total = sum(int(v) for name,v in table)

print(total)
