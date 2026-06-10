print("trin_svmmm")
from sklearn.model_selection import train_test_split

from sklearn.svm import LinearSVC

from sklearn.metrics import (

    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score
)

import joblib

from text_preprocessing import X, y, tfidf


# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)


# =====================================================
# MODEL
# =====================================================

model = LinearSVC(

    class_weight='balanced'
)


# =====================================================
# TRAIN MODEL
# =====================================================

print("\nTraining SVM Model...\n")

model.fit(X_train, y_train)

print("Training Completed!")


# =====================================================
# PREDICTIONS
# =====================================================

y_pred = model.predict(X_test)


# =====================================================
# EVALUATION
# =====================================================

print("\nAccuracy:")

print(

    accuracy_score(y_test, y_pred)
)

print("\nF1 Score:")

print(

    f1_score(y_test, y_pred)
)

print("\nClassification Report:\n")

print(

    classification_report(y_test, y_pred)
)

print("\nConfusion Matrix:\n")

print(

    confusion_matrix(y_test, y_pred)
)


# =====================================================
# =====================================================
# SAVE MODEL
# =====================================================
import os

# print where Python is currently running from
print("Current working directory:", os.getcwd())

# print the full path where it will save
print("Saving model to:", os.path.abspath("../models/svm_model.pkl"))



# build the path dynamically — works from anywhere
base_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(base_dir, '..', 'models')

os.makedirs(models_dir, exist_ok=True)

joblib.dump(model, os.path.join(models_dir, 'svm_model.pkl'))
joblib.dump(tfidf, os.path.join(models_dir, 'tfidf_vectorizer.pkl'))

print("Models saved to:", models_dir)