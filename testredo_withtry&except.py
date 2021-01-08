def main():
    x = 0
    student_marks = []
    student_names = []
    print(name_message())
    total_grades = int(input("How many grades would you like to enter?: "))
    while x < total_grades:
        student_marks.append(take_interger())
        student_names.append(take_name())
        x += 1
    print(f"The class average is % {average(student_marks)}")
    name_list(student_names, student_marks)
    print(failing_grades(student_marks))    


def take_name():
    while True:
        name = input("What's their name?: ")
        if 2 <= len(name) <= 15:
            return name
        else:
            print("Invalid input please try again")


def name_message():
    name = " "
    while True:
        try
    name = input("What's your name?: ")
    return (f"Hello {name}. Welcome to the Markbook Program.")


def take_interger():
    number = 0
    while True:
        try:
            number = int(input("Input an interger: "))
        except ValueError:
            print("Invalid input please try again.")
        if number >= 0:
            return number
        elif number < 0:
            print("Invalid input please try again")


def name_list(student_names, student_marks):
    for name, mark in zip(student_names, student_marks):
        print(name, mark)


def failing_grades(student_marks):
    fails = 0
    for mark in student_marks:
        if mark <= 50:
            fails += 1
    return (f"{fails} student(s) are failing")

def average(student_marks):
    y = 0
    for i in student_marks:
        y += i
    return round(y / len(student_marks),2)

main()
