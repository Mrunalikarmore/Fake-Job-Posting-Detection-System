
print("NEW MULTI MODEL CODE IS RUNNING")
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    f1_score
)

# MODELS
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

# import from preprocessing file
from text_preprocessing import X, y, tfidf


# =====================================================
# 1. TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# =====================================================
# 2. MODELS
# =====================================================

models = {

    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        class_weight='balanced'
    ),

    "Naive Bayes": MultinomialNB(),

    "Linear SVM": LinearSVC(
        class_weight='balanced'
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight='balanced'
    )
}


# =====================================================
# 3. SAMPLE JOB DESCRIPTIONS
# =====================================================

samples = [

    # REAL JOBS
    "Hiring Python developer with experience in Django and SQL. Full time opportunity with health benefits.",

    "Looking for Data Analyst skilled in Power BI, Excel, SQL and machine learning.",

    "Software engineer required with 2 years of experience in Java and cloud computing.",


    # FAKE JOBS
    "Earn $7000 weekly from home without any skills. No interview required. Instant joining.",

    "Congratulations! You have been selected for a high paying remote job. Pay registration fee now.",

    "Work only 1 hour daily and earn unlimited income immediately."
]


# =====================================================
# 4. TRAIN & EVALUATE EACH MODEL
# =====================================================

for name, model in models.items():

    print("\n\n")
    print("=================================================")
    print(f"MODEL: {name}")
    print("=================================================")

    # TRAIN
    model.fit(X_train, y_train)

    # PREDICT
    y_pred = model.predict(X_test)

    # METRICS
    accuracy = accuracy_score(y_test, y_pred)

    f1 = f1_score(y_test, y_pred)

    print("\nAccuracy:", round(accuracy, 3))
    print("F1 Score:", round(f1, 3))

    # ROC AUC
    try:
        y_prob = model.predict_proba(X_test)[:, 1]

        roc_auc = roc_auc_score(y_test, y_prob)

        print("ROC-AUC Score:", round(roc_auc, 3))

    except:
        print("ROC-AUC Score: Not available for this model")


    # CLASSIFICATION REPORT
    print("\nClassification Report:\n")

    print(classification_report(y_test, y_pred))


    # CONFUSION MATRIX
    cm = confusion_matrix(y_test, y_pred)

    print("Confusion Matrix:")

    print(cm)


    # =================================================
    # SAMPLE PREDICTIONS
    # =================================================

    print("\n")
    print("--------------- SAMPLE PREDICTIONS ---------------")

    for text in samples:

        transformed = tfidf.transform([text])

        pred = model.predict(transformed)[0]

        print("\nJob Text:")
        print(text)

        print("\nPrediction:",
              "FAKE" if pred == 1 else "REAL")


        # probability if available
        try:
            prob = model.predict_proba(transformed)[0][1]

            print("Confidence:", round(prob, 3))

        except:
            print("Confidence: Not available")

        print("---------------------------------------------")