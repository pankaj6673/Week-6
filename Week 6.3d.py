grade = int(input("Enter your mark:"))
letterGrade = "F"

if grade >= 90 :
	letterGrade = "A"
elif grade >= 80 :
	letterGrade = "B"
elif grade >= 70 :
	letterGrade = "C"
elif grade >= 60 :
	letterGrade = "D"
print(letterGrade)
