from datetime import date
import calendar

# 1. gets today's date and stores it in a variable 'date'
date = date.today()

"""
2. uses today's date to get the name on the day of the week written in a short
form with the first letter capitalized eg. 'Fri' if today were Friday and assigns
it a variable 'day'
"""

day = calendar.day_name[date.weekday()].capitalize()

"""
3. uses if statements to determine the today's fare following these bus fare
schedule:
○ Monday - Friday --> 100
○ Saturday --> 60
○ Sunday --> 80
"""
fare = 0
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    fare = 100
elif day == "Saturday":
    fare = 60
elif day == "Sunday":
    fare = 80
else:
    print("Error, please try again!")

"""
4. Prints the results in this exact format
Date: 2021-01-05
Day: Tue
Fare: 100
"""

day = day[0:3]
print(f"Date: {date}\n"
      f"Day: {day}\n"
      f"Fare: {fare}")
