# operasi Logika
# or and xor not

x = True
z = not x
print("nilai dari z =", z)

print("**** and *****")
x = True
y = True
z = x and y
print(x, 'and', y, '=', z)

x = True
y = False
z = x and y
print(x, 'and', y, '=', z)

x = False
y = True
z = x and y
print(x, 'and', y, '=', z)

x = False
y = False
z = x and y
print(x, 'and', y, '=', z)

print("**** xor *****")
x = True
y = True
z = x != y
print(x, 'xor', y, '=', z)
x = True
y = False
z = x != y
print(x, 'xor', y, '=', z)
x = False
y = True
z = x != y
print(x, 'xor', y, '=', z)
x = False
y = False
z = x != y
print(x, 'xor', y, '=', z)