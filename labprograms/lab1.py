name = input("Enter the student name: ")
usn = input("Enter the student USN: ")
phy = int(input("Enter the marks obtained in Physics: "))
che = int(input("Enter the marks obtained in Chemistry: "))
mat = int(input("Enter the marks obtained in Mathematics: "))
max_marks = 300
print(30 * "*")

print("Name of the Student:", name)
print("Student USN:", usn)
print(30 * "*")

total = phy + che + mat
print("The total marks scored by the student in Physics", phy, "Chemistry", che, "Mathematics", mat, "is", total)
print(30 * "*")

percent = (total/max_marks) * 100
print("Percentage of the Student:", round(percent))

# (b) Develop a program to reas the name and year of birth of a person. Display whether the person is a senior citizen or not.
import datetime
name = input("Enter the name of the person: ")
birth_year = int(input("Enter the year of birth of the person: "))
today = datetime.date.today()
year = today.year
age = year - birth_year
if age >= 60:
print(name + "is a senior citizen")
else:
print(name + "is not a senior citizen")
