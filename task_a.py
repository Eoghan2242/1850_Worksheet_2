day = input("Please enter the day of the week: ")

d_low = day.lower()

if d_low == "monday":
    print("Monday is day 1")
elif d_low == "tuesday":
    print("Tuesday is day 2")
elif d_low == "wednseday":
    print("Wednesday is day 3")
elif d_low == "thursday":
    print("Thursday is day 4")
elif d_low == "friday":
    print("Friday is day 5")
elif d_low == "saturday":
    print("Saturday is day 6")
elif d_low == "sunday":
    print("Sunday is day 7") 
else:
    print("Please enter a valid day")   
    exit()
