import mysql.connector


# =====================================================
# MYSQL CONNECTION
# =====================================================

conn = mysql.connector.connect(

    host="localhost",

    user="Mrunaliuser",

    password="Project@123",

    database="fake_job_detector"
)


# =====================================================
# CURSOR
# =====================================================

cursor = conn.cursor()


print("MySQL Connected Successfully!")