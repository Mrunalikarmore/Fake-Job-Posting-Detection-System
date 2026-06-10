# 🚨 Fake Job Posting Detection System

An end-to-end Machine Learning and NLP project that detects whether a job posting is **Real** or **Fake** using TF-IDF Vectorization and a Linear Support Vector Machine (SVM).

The project includes data preprocessing, model training, database integration with MySQL, and a Streamlit web application for real-time predictions.

---

## 📌 Project Overview

Online job portals contain thousands of job postings every day. Unfortunately, some of these postings are fraudulent and designed to scam job seekers.

This project uses Natural Language Processing (NLP) and Machine Learning techniques to automatically classify job advertisements as:

* ✅ Real Job Posting
* ❌ Fake Job Posting

The goal is to help job seekers identify suspicious job listings before applying.

---

## 🎯 Problem Statement

Fake job advertisements can:

* Steal personal information
* Conduct financial scams
* Waste applicants' time
* Damage trust in online recruitment platforms

This project aims to build a machine learning system capable of detecting fraudulent job postings automatically.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn

### NLP

* TF-IDF Vectorization

### Classification Model

* Linear Support Vector Machine (SVM)

### Database

* MySQL

### Deployment

* Streamlit

### Model Persistence

* Joblib

---

## 📂 Project Structure

```text
fake_job_detector/
│
├── data/
│   └── fake_job_postings.csv
│
├── models/
│   ├── svm_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── eda_analysis.ipynb
│
├── sql/
│   └── Schema.sql
│
├── src/
│   ├── app.py
│   ├── compare_models.py
│   ├── db_connection.py
│   ├── load_data.py
│   ├── text_preprocessing.py
│   └── train_svm.py
│
└── README.md
```

---

## 🔄 Project Workflow

```text
Raw Job Posting Data
          │
          ▼
Data Cleaning & Text Preprocessing
          │
          ▼
TF-IDF Vectorization
          │
          ▼
Linear SVM Model Training
          │
          ▼
Model Evaluation
          │
          ▼
Save Model using Joblib
          │
          ▼
MySQL Database Integration
          │
          ▼
Streamlit Web Application
```

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Converted text to lowercase
* Removed punctuation
* Removed special characters
* Removed unnecessary whitespace
* Combined important text columns
* Prepared text for TF-IDF feature extraction

---

## 🔤 Feature Engineering

TF-IDF (Term Frequency-Inverse Document Frequency) was used to convert textual job descriptions into numerical features.

Benefits:

* Captures important keywords
* Handles high-dimensional text data efficiently
* Works effectively with machine learning algorithms

---

## 🤖 Model Selection

### Linear Support Vector Machine (SVM)

The final model selected was:

```python
SVC(
    kernel='linear',
    class_weight='balanced'
)
```

### Why SVM?

* Excellent performance on text classification tasks
* Handles sparse TF-IDF features efficiently
* Strong generalization ability
* Effective for binary classification problems

### Handling Class Imbalance

The dataset contained significantly more real jobs than fake jobs.

Instead of oversampling techniques such as SMOTE, the project uses:

```python
class_weight='balanced'
```

This allows the model to pay more attention to the minority class while preserving the original data distribution.

---

## 📊 Model Performance

### Evaluation Results

| Metric                | Score  |
| --------------------- | ------ |
| Accuracy              | 97.90% |
| Precision (Fake Jobs) | 76%    |
| Recall (Fake Jobs)    | 83%    |
| F1 Score (Fake Jobs)  | 79.34% |

### Classification Report

| Class         | Precision | Recall | F1 Score |
| ------------- | --------- | ------ | -------- |
| Real Jobs (0) | 0.99      | 0.99   | 0.99     |
| Fake Jobs (1) | 0.76      | 0.83   | 0.79     |

### Confusion Matrix

```text
[[3357   46]
 [  29  144]]
```

Interpretation:

* Correctly identified 3357 real job postings
* Correctly detected 144 fake job postings
* Missed 29 fake job postings
* Incorrectly flagged 46 real job postings as fake

---

## 🗄️ Database Integration

MySQL was used for storing job posting information and prediction-related data.

### Database Features

* Store raw job postings
* Store processed records
* Maintain prediction history
* Support future analytics and reporting

---

## 💻 Streamlit Web Application

The project includes a Streamlit dashboard that allows users to:

* Enter job posting details
* Predict whether a job is real or fake
* View results instantly
* Store records in MySQL

### Run Application

```bash
streamlit run src/app.py
```

---

## 📸 Application Screenshots


### Fake Job Prediction



### Real Job Prediction

(Add screenshot here)

### Model Performance

(Add evaluation screenshot here)

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/fake-job-detector.git
```

### Move into Project Directory

```bash
cd fake-job-detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run src/app.py
```

---

## 🔮 Future Improvements

* BERT-based text classification
* Explainable AI (SHAP)
* FastAPI deployment
* Docker containerization
* Cloud deployment using AWS or Azure
* Real-time job scraping and detection

---

## 📚 Key Learning Outcomes

* Natural Language Processing
* Text Preprocessing
* TF-IDF Vectorization
* Machine Learning Classification
* Handling Imbalanced Datasets
* Model Evaluation
* MySQL Integration
* Streamlit Deployment
* End-to-End ML Project Development

---

## 👨‍💻 Author

Mrunali Karmore

Artificial Intelligence & Data Science Student

Interested in:

* Data Science
* Machine Learning
* Artificial Intelligence
* NLP Projects
* Data Analytics

---

⭐ If you found this project useful, consider giving it a star.
