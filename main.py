from planner import create_plan
from analysis import analyze_data

while True:

    print("\n===== SMART AI STUDY PLANNER =====")
    print("1. Create Study Plan")
    print("2. Analyze Study Data")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_plan()

    elif choice == "2":
        analyze_data()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")