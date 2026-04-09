import numpy as np
import random
import matplotlib.pyplot as plt

def show_grades(grades):
    for i, grade in enumerate(grades, start=1):
        print(f"Student {i}: {grade}")

def show_stats(grades):
    if not grades:
        print("There no grades yet!")
        return
    grades_array = np.array(grades)
    print(f"Average: {np.mean(grades_array)}")
    print(f"Highest: {np.max(grades_array)}")
    print(f"Lowest: {np.min(grades_array)}")
    print(f"Number of student passed: {np.sum(grades_array >= 10)}")

def plot_bar_chart(students, grades):
    plt.bar(students, grades)
    plt.title("Grades Bar Chart")
    plt.xlabel("Student Number")
    plt.ylabel("Grades")
    plt.show()

def plot_histogram(grades):
    plt.hist(grades, bins=range(0, 21))
    plt.title("Grades Histogram")
    plt.show()
menu = "1. View grades\n2. Show stats (average, highest, lowest, passed count)\n3. Plot a bar chart\n4. Plot a histogram\n5. Exit"
grades = [random.randint(0, 20) for i in range(10)]
students = [i for i in range(1, 11)]

while True:
    print(menu)
    choice = input("Choose an option from the menu: ")
    if not choice.isdigit() or not(1 <= int(choice) <= 5):
        print("Enter a number between 1 and 5: \n\n")
        continue
    else:
        user_choice = int(choice)

        if user_choice == 1:
            show_grades(grades)
        elif user_choice == 2:
            show_stats(grades)
        elif user_choice == 3:
            plot_bar_chart(students, grades)
        elif user_choice == 4:
            plot_histogram(grades)
        elif user_choice == 5:
            print("Good Bye!")
            break
