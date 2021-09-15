# -*- coding: utf-8 -*-
"""
Edmond Tongyou
CPSC 223P-01
Thu April 12, 2021
tongyouedmond@fullerton.edu
"""

attendanceList = []
examList = []
gradeList = []
dayList = []
studentList = []

# Opens the attendance.txt file and creates a list for the first line and the
# students in the class.
with open("attendance.txt", "r") as myAttendanceFile:
    dayList = myAttendanceFile.readlines(1)
    attendanceList = myAttendanceFile.readlines()


# Opens the exam.txt file and creates a list for the first line and an empty grades
# list for the students in the class.
with open("grades.txt", "r") as myGradesFile:
    examList = myGradesFile.readlines(1)


# Uses the attendance list to create a list of students.
for index in range(0, len(attendanceList)):
    studentList += attendanceList[index].split(",,,,,,,,,,,,,,,,\n")


# Removes extra indices created by split().
for index in range(0, (len(studentList)//2)):
    index += 1
    studentList.pop(index)


# Removes escape character at the end and removes "Student" from both lists.
# Additionally reformats the elements to not have spaces in front of them.
examList[0] = examList[0].strip()
strExamList = "".join(examList)
examList = strExamList.split(",")
examList.pop(0)
for index in range(0, len(examList)):
    examList[index] = examList[index].strip()

dayList[0] = dayList[0].strip()
strDayList = "".join(dayList)
dayList = strDayList.split(",")
dayList.pop(0)
for index in range(0, len(dayList)):
    dayList[index] = dayList[index].strip()


# Adds ":" to the end of each element in examList and dayList.
for index in range(0, len(examList)):
    examList[index] += ":"

for index in range(0, len(dayList)):
    dayList[index] += ":"


# Appends studentList and examList to create a Grade List.
# Also appends studentList and dayList to create an Attendance List.
for index in range(0, len(studentList)):
    gradeList.append(studentList[index])
    for index in range(0, len(examList)):
        gradeList.append(examList[index])

attendanceList.clear()
for index in range(0, len(studentList)):
    attendanceList.append(studentList[index])
    for index in range(0, len(dayList)):
        attendanceList.append(dayList[index])


# User selects a choice from one of the 6 options below
# if the user's input is invalid they will be prompted to
# enter a choice again.
# 1: Returns a list of all students in the class
# 2: Returns a list of all grades for every student in the class
# 3: Returns a list of attendence for a chosen student
# 4: Inputs a grade for each student for a chosen assignment
# 5: Inputs an attendance check for each student for a chosen date
# Q: Exits the loop and closes the program
# Note: The examList is only a list of the exams in the class, the
# gradeList is the list of grades which are returned in option 2 and 4
exit = False
while not exit: 
    print("What would you like to do?")
    print("1 - List all students")
    print("2 - List all grades")
    print("3 - List attendance")
    print("4 - Submit a grade")
    print("5 - Take attendance")
    print("Q - Quit")

    choice = input()
    print("")


    if choice == "1":
        for index in range(0, len(studentList)):
            print(studentList[index])
        print("")


    elif choice == "2":
        for index in range(0, len(gradeList)):
            print(gradeList[index])
            if "Final:" in gradeList[index]:
                print("")


    elif choice == "3":
        correctChoice = False
        totalStudents = 0

        print("For which Student?")

        for index in range(0, len(studentList)):
            print(str(index + 1) + " - " + studentList[index])
            totalStudents += 1

        while correctChoice == False:
            studentChoice = input()
            
            if studentChoice.isalpha() or int(studentChoice) <= 0 or int(studentChoice) > totalStudents:
                print("Invalid choice, please pick a Student Number.\n")
            
            else:
                correctChoice = True

        print("")
        for index in range(0, len(attendanceList)):
            if studentList[int(studentChoice) - 1] in attendanceList[index]:
                for x in range(0, len(dayList) + 1):
                    print(attendanceList[index + x])
                break
        print("")


# Writes to file by converting file contents to a list and mutating the specified element.
# Afterwards, converts list to string to write back into file.
    elif choice == "4":
        correctChoice = False
        totalExams = 0

        print("For which Assignment?")

        for index in range(0, len(examList)):
            print(str(index + 1) + " - " + examList[index])
            totalExams += 1
        
        while correctChoice == False:
            examChoice = input()

            if examChoice.isalpha() or int(examChoice) <= 0 or int(examChoice) > totalExams:
                print("Invalid choice, please pick an Exam Number\n")
            
            else:
                correctChoice = True

        print("")


        for student in range(0, len(studentList)):
            legalGrade = False
            while legalGrade == False:
                grade = input("Grade for " + studentList[student] + " for " + examList[int(examChoice) - 1] + " > ")
                if grade.isalpha() or int(grade) < 0 or int(grade) > 100:
                    print("Invalid grade, please enter a  number between 0 and 100\n")
                else:
                    legalGrade = True

            print("")


            for x in range(0, len(gradeList)):
                if studentList[student] in gradeList[x]:
                    gradeList[x + int(examChoice)] =  examList[int(examChoice) - 1] + " " + grade


                    with open("grades.txt", "r") as myGradesFile:
                        newContentList = myGradesFile.readlines()

                    with open("grades.txt", "w") as myGradesFile:
                        gradeUpdate = ""

                        for y in range(0, totalExams):
                            if y == int(examChoice):
                                gradeUpdate += grade
                            gradeUpdate += ","
                        gradeUpdate += "\n"
                        
                        newContentList[student + 1] = studentList[student] + gradeUpdate
                        newContentStr = "".join(newContentList)
                        myGradesFile.write(newContentStr)
                    break


        print("")


# Same process for file writing as option 4 but with different variables.
    elif choice == "5":
        correctChoice = False
        totalDays = 0

        print("For which Date?")
        for index in range(0, len(dayList)):
            print(str(index + 1) + " - " + dayList[index].strip(":"))
            totalDays += 1

        while correctChoice == False:
            dayChoice = input()

            if dayChoice.isalpha() or int(dayChoice) <= 0 or int(dayChoice) > totalDays:
                print("Invalid choice, please pick a Day Number\n")

            else:
                correctChoice = True

        print("")


        for student in range(0, len(studentList)):
            legalDay = False
            while legalDay == False:
                day = input("Student " + studentList[student] + " (p/a) > ")
                if day.isnumeric() or day.lower() not in "ap" or len(day) != 1:
                    print("Invalid choice, please enter either p or a\n")
                else:
                    legalDay = True

            print("")


            for x in range(0, len(attendanceList)):
                if studentList[student] in attendanceList[x]:
                    if day.lower() == "p":
                        attendanceList[x + int(dayChoice)] = dayList[int(dayChoice) - 1] + " " + "Present"


                        with open("attendance.txt", "r") as myAttendanceFile:
                            newContentList = myAttendanceFile.readlines()

                        with open("attendance.txt", "w") as myAttendanceFile:
                            dayUpdate = ""

                            for y in range(0, totalDays):
                                if y == int(dayChoice):
                                    dayUpdate += "Present"
                                dayUpdate += ","
                            dayUpdate += "\n"
                            
                            newContentList[student + 1] = studentList[student] + dayUpdate
                            newContentStr = "".join(newContentList)
                            myAttendanceFile.write(newContentStr)
                        break
                    else:
                        attendanceList[x + int(dayChoice)] = dayList[int(dayChoice) - 1] + " " + "Absent"


                        with open("attendance.txt", "r") as myAttendanceFile:
                            newContentList = myAttendanceFile.readlines()

                        with open("attendance.txt", "w") as myAttendanceFile:
                            dayUpdate = ""

                            for y in range(0, totalDays):
                                if y == int(dayChoice):
                                    dayUpdate += "Absent"
                                dayUpdate += ","
                            dayUpdate += "\n"
                            
                            newContentList[student + 1] = studentList[student] + dayUpdate
                            newContentStr = "".join(newContentList)
                            myAttendanceFile.write(newContentStr)
                        break


        print("")
    elif choice.upper() == "Q":
        exit = True


    else:
        print("Invalid option, please enter a number from 1-5 or Q\n")
        print("")