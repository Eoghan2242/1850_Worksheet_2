user_grade = input("Enter a numerical grade between 0-100: ")


try:
    number_grade = float(user_grade)   
    
    if number_grade < 0 or number_grade > 100:
        print("Error: Grades must be between 0 and 100")
        exit()
    
    
    if number_grade >= 80:
        letter_grade = "A"
    elif number_grade >= 60:
        letter_grade = "B"
    elif number_grade >= 50:
        letter_grade = "C"
    elif number_grade >= 40:
        letter_grade = "D"
    else:  
        letter_grade = "F"

    print("Your grade is: " + letter_grade)

except ValueError:
    print("Error: Please enter a number")
    exit()
    
   

