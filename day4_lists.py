fruits = ["apple", "banana", "cherry"]

print(fruits)
print(fruits[0])
print(fruits[-1])

fruits.append("orange")

print("Updated list:")
for fruit in fruits:
    print(fruit)

x = [1, 2, 3, 4, 5, 6]
total = 0
for i in range(len(x)):
    total += x[i]
print(total)

print(x[1:5:1])