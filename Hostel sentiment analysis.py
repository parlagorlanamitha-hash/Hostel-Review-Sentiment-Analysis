
"""
HOSTEL LIFE SENTIMENT ANALYSIS
TF-IDF + Logistic Regression + SVM
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score, precision_score,
    recall_score, f1_score
)

# ---------- 1. Load Dataset ----------

FILE_PATH = r"C:\Users\P.Namitha\Downloads\hostel_life_sentiment_dataset.xlsx"

df = pd.read_excel(FILE_PATH)
df.columns = df.columns.str.strip()

target_col = "Overall hostel experience?"
suggestion_col = (
    "Do you have any suggestions or improvements "
    "you would like to see in your hostel?"
)

df[target_col] = pd.to_numeric(df[target_col], errors="coerce")
df = df.dropna(subset=[target_col]).copy()

# ---------- 2. Create Sentiment Labels ----------

def get_sentiment(rating):
    if rating <= 2:
        return "Negative"
    elif rating == 3:
        return "Neutral"
    return "Positive"

df["Sentiment"] = df[target_col].apply(get_sentiment)

# ---------- 3. Prepare NLP Text ----------

excluded_cols = [
    "Timestamp",
    "Email Address",
    "Gender",
    target_col,
    "Sentiment"
]

feature_cols = [
    col for col in df.columns
    if col not in excluded_cols
]

df[feature_cols] = df[feature_cols].fillna("")

df["Combined_Text"] = df[feature_cols].astype(str).agg(
    " ".join, axis=1
).str.strip()

df = df[df["Combined_Text"].str.len() > 0].copy()

X = df["Combined_Text"]
y = df["Sentiment"]

print("=" * 60)
print("HOSTEL LIFE SENTIMENT ANALYSIS")
print("=" * 60)
print("Dataset loaded successfully!")
print("Total records:", len(df))
print("Technique: NLP - TF-IDF")
print("Algorithms: Logistic Regression and SVM")

# ---------- 4. Split Dataset ----------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ---------- 5. Create Models ----------

models = {
    "Logistic Regression": Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
            min_df=1
        )),
        ("classifier", LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            random_state=42
        ))
    ]),

    "SVM": Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
            min_df=1
        )),
        ("classifier", LinearSVC(
            class_weight="balanced",
            random_state=42
        ))
    ])
}

# ---------- 6. Train and Compare Models ----------

trained_models = {}
results = []

print("\nComparing Machine Learning Models...")
print("Evaluation Metrics: Accuracy, Precision, Recall and F1-Score")
print("-" * 60)

for name, model in models.items():

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    trained_models[name] = model

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test, predictions,
        average="macro", zero_division=0
    )
    recall = recall_score(
        y_test, predictions,
        average="macro", zero_division=0
    )
    f1 = f1_score(
        y_test, predictions,
        average="macro", zero_division=0
    )

    results.append({
        "Algorithm": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1
    })

    print(f"{name} -> Accuracy: {accuracy:.4f}, "
          f"Precision: {precision:.4f}, "
          f"Recall: {recall:.4f}, F1-Score: {f1:.4f}")

comparison = pd.DataFrame(results)

# ---------- 7. Model Comparison Result ----------

print("\n" + "=" * 60)
print("MODEL COMPARISON RESULT")
print("=" * 60)

best = comparison.sort_values(
    by=["F1-Score", "Accuracy"],
    ascending=False
).iloc[0]

print("Best Model Selected:", best["Algorithm"])
print(f"Best Test F1-Score: {best['F1-Score']:.4f}")
print(f"Test Accuracy: {best['Accuracy']:.4f}")

print("\nSelected models trained on the training dataset.")
print("Sentiment analysis system is ready.")

# ---------- 8. Selection Menu ----------

aspects = [
    "Cleanliness and Maintenance",
    "Safety and Security",
    "Hostel Fees",
    "Quality of Food",
    "Roommate Issues",
    "Noise Disruptions",
    "Internet Speed",
    "Hostel Staff",
    "Social and Recreational Activities",
    "Hostel Rules",
    "Social Atmosphere",
    "Overall Hostel Experience"
]

while True:

    print("\n" + "=" * 60)
    print("HOSTEL LIFE SENTIMENT ANALYSIS MENU")
    print("=" * 60)

    print("\n1. Analyze Hostel Feedback")
    print("2. Compare Algorithms")
    print("3. View Sentiment Distribution")
    print("4. Exit")

    choice = input("\nSelect number: ").strip()

    if choice == "1":

        print("\nAvailable Hostel Aspects:")
        for i, aspect in enumerate(aspects, 1):
            print(f"{i}. {aspect}")

        while True:
            pick = input(
                "\nWhich hostel aspect do you want to analyze? "
            ).strip()

            if pick.isdigit() and 1 <= int(pick) <= len(aspects):
                aspect = aspects[int(pick) - 1]
                break

            print("Invalid selection. Please try again.")

        print("\nSelect Algorithm:")
        print("1. Logistic Regression")
        print("2. SVM")
        print("3. Both Algorithms")

        alg_choice = input("Select number: ").strip()

        if alg_choice == "1":
            selected = ["Logistic Regression"]
        elif alg_choice == "2":
            selected = ["SVM"]
        elif alg_choice == "3":
            selected = list(trained_models.keys())
        else:
            print("Invalid algorithm selection.")
            continue

        feedback = input(
            f"\nEnter your feedback about {aspect}: "
        ).strip()

        if not feedback:
            print("Please enter feedback.")
            continue

        # Include the selected aspect as context
        text_input = aspect + ". " + feedback

        print("\n" + "-" * 60)
        print("HOSTEL SENTIMENT PREDICTION")
        print("-" * 60)
        print("Selected Aspect:", aspect)
        print("Your Feedback:", feedback)

        for name in selected:
            prediction = trained_models[name].predict(
                [text_input]
            )[0]

            print(f"{name} Prediction: {prediction}")

    elif choice == "2":

        print("\n===== ALGORITHM COMPARISON =====")
        print(comparison.to_string(
            index=False,
            formatters={
                "Accuracy": "{:.4f}".format,
                "Precision": "{:.4f}".format,
                "Recall": "{:.4f}".format,
                "F1-Score": "{:.4f}".format
            }
        ))

        print("\nBest Model:", best["Algorithm"])

    elif choice == "3":

        print("\n===== SENTIMENT DISTRIBUTION =====")
        print(df["Sentiment"].value_counts().to_string())

    elif choice == "4":

        print("\nThank you for using Hostel Life Sentiment Analysis!")
        break

    else:
        print("Invalid choice. Select a number from 1 to 4.")
