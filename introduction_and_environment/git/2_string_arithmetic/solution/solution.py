# Code your solution here
STR_ARITHMETIC = 0
s = "string"
n = 2

try:
    print(s + s)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s - s)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s * s)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s / s)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s ** s)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s // s)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s % s)
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    print(s + n)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s - n)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s * n)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s / n)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s ** n)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s // n)
    STR_ARITHMETIC += 1
except TypeError:
    pass
try:
    print(s % n)
    STR_ARITHMETIC += 1
except TypeError:
    pass
print(STR_ARITHMETIC)
