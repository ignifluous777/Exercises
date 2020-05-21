x = 1
y = 1

while True:
    x += 1
    y += 1
    if id(x) == id(y):
        pass
    else:
        print(x, y)
        break

x = 1
y = 1

while True:
    x -= 1
    y -= 1
    if id(x) == id(y):
        pass
    else:
        print(x, y)
        break

LOWER_BOUND = -5
UPPER_BOUND = 256
