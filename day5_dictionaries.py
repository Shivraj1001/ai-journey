# Day 5: Dictionaries

student = {
    "name": "Shivraj",
    "age": 18,
    "course": "AIDS"
}

print(student["name"])
print(student["age"])

student["college"] = "Pune University"
student["age"] = 19

for key, value in student.items():
    print(key, ":", value)

sub_marks = {
    "Physics": 47,
    "Maths": 95,
    "Chemistry": 99
}

print(sub_marks)

total = 0
for marks in sub_marks.values():
    total += marks

count = len(sub_marks)

avg = total/count
print("Average", avg)
