import pandas as pd

def create_plan():
    print("===== AI STUDY PLANNER =====")

    subjects = []
    hours = []

    total_subjects = int(input("How many subjects? "))

    for i in range(total_subjects):
        subject = input("Enter subject name: ")
        hour = int(input(f"How many hours for {subject}? "))

        subjects.append(subject)
        hours.append(hour)

    data = {
        "Subject": subjects,
        "Hours": hours
    }

    df = pd.DataFrame(data)

    df.to_csv("data/study_data.csv", index=False)

    print("\nStudy Plan Saved Successfully!")

if __name__ == "__main__":
    create_plan()