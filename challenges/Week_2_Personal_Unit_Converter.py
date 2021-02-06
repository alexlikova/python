# define the function blocks
def one():
    print(f"Value in {sm} to convert: {value}")
    inch = value * 2.54
    return print(f"{value} {sm} = {inch} {inches}")


def two():
    print(f"Value in {percentage} to convert: {value}")
    if 0 <= value < 20:
        grade = "F"
    elif 20 <= value < 40:
        grade = "E"
    elif 50 <= value < 60:
        grade = "D"
    elif 60 <= value < 70:
        grade = "C"
    elif 70 <= value < 80:
        grade = "B"
    elif 80 <= value <= 100:
        grade = "A"

    return print(f"{value} % = {grade}")


def three():
    print(f"Value in {cups} to convert: {value}")
    ml_result = value * 237
    return print(f"{value} {cups} = {ml_result} {ml}")


def four():
    print(f"Value in {grams} to convert: {value}")
    ounces_result = value / 28.35
    return print(f"{value} {grams} = {ounces_result} {ounces}")


def five():
    print(f"Value in {fahrenheit} to convert: {value}")
    celsius_result = (value - 32) * 5 / 9
    return print(f"{value} {fahrenheit} = {celsius_result} {celsius}")


# map the inputs to the function blocks
def indirect_number_choice(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five}

    func = switcher.get(argument, lambda: 'Invalid number')
    return func()


name = input("Please, enter your name: ")

print(
    f"\nHello {name}, welcome to your personal unit converter.\n Please, choose which conversion you would like to perform: \n"
    f"1. Convert sm to inches\n"
    f"2. Convert Percentage to letter grade\n"
    f"3. Convert cups to ml\n"
    f"4. Convert grams to ounces\n"
    f"5. Convert Fahrenheit to Celsius\n")

choice = int(input(f" Choice: "))

value = float(input("Please, type the value number that you want to convert: "))

sm = "sm"
inches = "inches"
percentage = "percentage"
letter_grade = "letter grade"
cups = "cups"
ml = "ml"
grams = "grams"
ounces = "ounces"
fahrenheit = "Fahrenheit"
celsius = "Celsius"
grade = ""

indirect_number_choice(choice)
print(f"Goodbye, {name}.")
