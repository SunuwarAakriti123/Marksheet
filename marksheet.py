def display_gpa():
    grade = input("Enter your grade (eg: A+, B, E): ").strip().lower()

    if grade == "a+":
        print("Your GPA value is 4.0! Outstanding Performance!")
    elif grade == "a":
        print("Your GPA value is 3.6! Excellent!")
    elif grade == "b+":
        print("Your GPA value is 3.2! Very Good!")
    elif grade == "b":
        print("Your GPA value is 2.8!")
    elif grade == "c+":
        print("Your GPA value is 2.6!")
    elif grade == "c":
        print("Your GPA value is 2.4!")
    elif grade == "d+":
        print("Your GPA value is 2.0!")
    elif grade == "d":
        print("Your GPA value is 1.6!")
    elif grade == "e":
        print("Your GPA value is 1.0! Fail! Better Luck Next Time!")
    else:
        print("Invalid Grade Entered!")

display_gpa()