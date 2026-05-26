import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():

    df = pd.read_csv("data/study_data.csv")

    print("\n===== STUDY ANALYSIS =====")
    print(df)

    weak_subject = df.loc[df['Hours'].idxmin()]

    print(f"\nWeak Subject: {weak_subject['Subject']}")
    print(f"Study Hours: {weak_subject['Hours']}")

    plt.figure(figsize=(8,5))
    plt.bar(df['Subject'], df['Hours'])

    plt.title("Daily Study Hours")
    plt.xlabel("Subjects")
    plt.ylabel("Hours")

    plt.savefig("graphs/study_graph.png")

    plt.show()

if __name__ == "__main__":
    analyze_data()