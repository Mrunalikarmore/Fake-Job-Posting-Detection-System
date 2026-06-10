import streamlit as st

import joblib

from db_connection import conn, cursor


# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load(

    "models/svm_model.pkl"
)

tfidf = joblib.load(

    "models/tfidf_vectorizer.pkl"
)


# =====================================================
# PAGE TITLE
# =====================================================

st.title("AI-Powered Fake Job Detector")


st.write(

    "Detect whether job postings are REAL or FAKE using NLP and Machine Learning."
)


# =====================================================
# USER INPUT
# =====================================================

job_text = st.text_area(

    "Enter Job Description"
)


# =====================================================
# PREDICT BUTTON
# =====================================================

if st.button("Detect Job"):


    # =========================================
    # TF-IDF TRANSFORMATION
    # =========================================

    transformed_text = tfidf.transform(

        [job_text]
    )


    # =========================================
    # PREDICTION
    # =========================================

    prediction = model.predict(

        transformed_text
    )[0]


    # =========================================
    # CONFIDENCE SCORE
    # =========================================

    confidence_score = 0.0

    try:

        decision_score = model.decision_function(

            transformed_text
        )[0]

        confidence_score = abs(

            float(decision_score)
        )

    except:

        confidence_score = 0.0


    # =========================================
    # LABEL
    # =========================================

    prediction_label = (

        True
        if prediction == 1
        else False
    )


    # =========================================
    # SHOW RESULT
    # =========================================

    if prediction == 1:

        st.error(

            "This Job Posting Looks FAKE"
        )

    else:

        st.success(

            "This Job Posting Looks REAL"
        )


    # =========================================
    # SHOW CONFIDENCE
    # =========================================

    st.write(

        f"Confidence Score: {confidence_score:.2f}"
    )


    # =========================================
    # SAVE PREDICTION TO MYSQL
    # =========================================

    query = """

    INSERT INTO predictions (

        job_id,
        predicted_label,
        confidence_score,
        model_used

    )

    VALUES (%s, %s, %s, %s)

    """


    values = (

        None,
        prediction_label,
        confidence_score,
        "Linear SVM"
    )


    cursor.execute(

        query,
        values
    )

    conn.commit()


    st.info(

        "Prediction Saved To Database"
    )