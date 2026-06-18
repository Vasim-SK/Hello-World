age = int(input())
with_parent = input() == "true"

message = "None"

if age >= 18:
    message = "You can watch any movie"
else:
    if age >= 18 and with_parent:
        message = "Yoy can watch PG-13 movies"
    else:
        message = "You can watch only G-rated movies"

print(message)