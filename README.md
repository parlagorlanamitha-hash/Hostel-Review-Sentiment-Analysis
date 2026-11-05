.
# Hostel Life Sentiment Analysis

## 1. Project Overview

Hostel Life Sentiment Analysis is a Machine Learning and Natural Language Processing (NLP) project that analyzes students' feedback about their hostel experiences. It focuses on aspects such as cleanliness, food quality, safety, hostel fees, internet facilities, and other hostel-related issues.

The system uses TF-IDF for text feature extraction and compares Logistic Regression and Support Vector Machine (SVM) algorithms to classify student opinions into three categories: Positive, Negative, and Neutral.

## 2. Objectives

- To analyze student feedback about hostel facilities and experiences.
- To apply Natural Language Processing techniques using TF-IDF.
- To classify student opinions into Positive, Negative, and Neutral sentiments.
- To compare the performance of Logistic Regression and SVM algorithms.
- To identify the best-performing model using evaluation metrics.

## 3. Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **NLP Technique:** TF-IDF (Term Frequency–Inverse Document Frequency)
- **Algorithms:** Logistic Regression, Support Vector Machine (SVM)
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib
- **Dataset Format:** Excel (.xlsx)

## 4. Features

- Analyzes student hostel feedback.
- Processes text using NLP techniques.
- Converts text into numerical features using TF-IDF.
- Classifies feedback into Positive, Negative, and Neutral sentiments.
- Compares two machine learning algorithms.
- Displays model performance using evaluation metrics.
- Identifies the better-performing algorithm.
- ## 1. Algorithms Used

### Logistic Regression
Logistic Regression is a supervised machine learning classification algorithm used to classify student feedback into three sentiment categories: Positive, Negative, and Neutral. It learns patterns from the TF-IDF features and predicts the sentiment of the feedback.

### Support Vector Machine (SVM)
Support Vector Machine is a supervised machine learning algorithm that finds an optimal decision boundary to separate different sentiment categories. It is used to classify hostel feedback into Positive, Negative, and Neutral sentiments.

### TF-IDF (Term Frequency–Inverse Document Frequency)
TF-IDF is an NLP feature extraction technique that converts text feedback into numerical values based on the importance of words. It helps machine learning algorithms understand and process student opinions.

### Algorithm Comparison

| Algorithm | Accuracy |
|---|---:|
| Logistic Regression | 59.26% |
| SVM | 48.15% |

**Best Performing Algorithm:** Logistic Regression

## 2. Dataset Description

**Dataset Name:** `hostel_life_sentiment_dataset.xlsx`

**Total Records:** 131

**Target Column:** `Overall hostel experience?`

### Dataset Features
- Student feedback about hostel facilities.
- Overall hostel experience ratings.
- Suggestions for hostel improvements.
- Other available hostel-related survey responses.

### Sentiment Categories
- **Positive:** Represents positive student experiences.
- **Negative:** Represents negative student experiences.
- **Neutral:** Represents neutral student experiences.

### Dataset Processing
- Loaded and cleaned the dataset using Pandas.
- Converted overall experience ratings into sentiment labels.
- Used student feedback and suggestions as text features.
- Applied TF-IDF for text feature extraction.
- Split the dataset into 80% training and 20% testing data.

The processed dataset is used to train and evaluate Logistic Regression and SVM algorithms.

## 5. Inputs

The system uses the following inputs:

- Student feedback about hostel facilities.
- Overall hostel experience ratings.
- Suggestions and opinions about hostel improvements.
- Hostel-related survey responses available in the dataset.

## 6. Methodology

1. **Data Collection:** Load the hostel feedback dataset.
2. **Data Preprocessing:** Clean and prepare the dataset for analysis.
3. **Sentiment Labeling:** Convert ratings into Positive, Negative, and Neutral categories.
4. **Text Feature Extraction:** Apply TF-IDF to convert text feedback into numerical features.
5. **Data Splitting:** Divide the dataset into 80% training data and 20% testing data.
6. **Model Training:** Train Logistic Regression and SVM algorithms.
7. **Model Evaluation:** Evaluate both models using Accuracy, Precision, Recall, and F1-Score.
8. **Model Comparison:** Compare the results and identify the best-performing algorithm.
9. **Sentiment Prediction:** Predict the sentiment of student feedback.

## 7. Working Process

1. Load the hostel feedback dataset.
2. Process student feedback and assign sentiment labels.
3. Convert text data into numerical values using TF-IDF.
4. Train the Logistic Regression and SVM models.
5. Test both models using testing data.
6. Compare their evaluation metrics.
7. Use the trained model to classify feedback into Positive, Negative, or Neutral sentiments.

## 8. Model Performance

The project compares Logistic Regression and SVM using four evaluation metrics.

| Evaluation Metric | Logistic Regression | SVM |
|---|---:|---:|
| Accuracy | 59.26% | 48.15% |
| Precision | 0.5295 | 0.4293 |
| Recall | 0.5212 | 0.4303 |
| F1-Score | 0.5225 | 0.4285 |

**Best Performing Model: Logistic Regression**

Logistic Regression achieved better results across all four evaluation metrics compared to SVM.

## 9. Future Enhancements

- Collect more student feedback to improve model performance.
- Develop a user-friendly web application for sentiment prediction.
- Add real-time feedback analysis.
- Include more hostel-related aspects for detailed analysis.
- Improve sentiment classification accuracy using advanced NLP techniques.
- Generate graphical reports to understand student satisfaction.

## 10. Conclusion

The Hostel Life Sentiment Analysis project uses NLP and Machine Learning to understand students' opinions about hostel facilities. By applying TF-IDF and comparing Logistic Regression with SVM, the project identifies Logistic Regression as the better-performing model with 59.26% accuracy. It helps analyze student feedback and understand areas that require improvement in hostel facilities.

## 11. Author

**Namitha**

B.Tech – Artificial Intelligence and Data Science

The Apollo University

GitHub: [Add your GitHub Profile Link]
