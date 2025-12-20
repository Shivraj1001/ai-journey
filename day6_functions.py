# Day 6: Functions

def calculate_average(marks_dict):
    total = 0
    for marks in marks_dict.values():
        total += marks
    return total/len(marks_dict)

sub_marks = {
    "Physics": 47,
    "Maths": 95,
    "Chemistry": 99
}

#Calculate avg of marks
avg = calculate_average(sub_marks)
print("Avereage marks:", avg )

#Calculate the maximum marks
def maxi(sub_marks):
    return max(sub_marks.values())
print("Maximum marks:", maxi(sub_marks))

#Calculate to check wether pass or fail
def evaluation(avg):
    if avg > 90:
        return "Pass"
    else:
        return "Fail"
print("Evaluation:", evaluation(avg))

#Grade based on average
def grade(avg):
    if avg > 90:
        return "A"
    elif avg > 80:
        return "B"
    else:
        return "C"
print("Grade:", grade(avg))