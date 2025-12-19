age = int(input("Enter your age: "))

if age >= 60:
    print("You are eligible to vote and retirement age")
elif age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

print("Numbers from 1 to 5:")
for i in range(1,6):
    print(i)