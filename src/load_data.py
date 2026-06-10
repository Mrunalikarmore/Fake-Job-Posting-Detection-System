import pandas as pd
import mysql.connector

import pandas as pd
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="Mrunaliuser",
    password="Project@123",
    database="fake_job_detector"
)

cursor = conn.cursor()

# Read CSV
df = pd.read_csv(
    "data/fake_job_postings.csv",
    encoding='utf-8'
)

print(df.shape)
print(df.head())

# Replace NaN with empty strings
df = df.fillna("")

# Insert Query
query = """
INSERT INTO raw_job_posts (
    job_id,
    title,
    location,
    department,
    salary_range,
    company_profile,
    description,
    requirements,
    benefits,
    telecommuting,
    has_company_logo,
    has_questions,
    employment_type,
    required_experience,
    required_education,
    industry,
    function_field,
    fraudulent
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Insert Rows
for _, row in df.iterrows():

    values = (
        str(row.get('job_id', '')),
        str(row.get('title', '')),
        str(row.get('location', '')),
        str(row.get('department', '')),
        str(row.get('salary_range', '')),
        str(row.get('company_profile', '')),
        str(row.get('description', '')),
        str(row.get('requirements', '')),
        str(row.get('benefits', '')),
        int(row.get('telecommuting', 0)),
        int(row.get('has_company_logo', 0)),
        int(row.get('has_questions', 0)),
        str(row.get('employment_type', '')),
        str(row.get('required_experience', '')),
        str(row.get('required_education', '')),
        str(row.get('industry', '')),
        str(row.get('function', '')),
        int(row.get('fraudulent', 0))
    )

    cursor.execute(query, values)

# Commit Changes
conn.commit()

print("✅ Data Imported Successfully!")

# Close Connection
cursor.close()
conn.close()

print(df.shape)