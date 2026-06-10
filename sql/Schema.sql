USE fake_job_detector;

CREATE TABLE IF NOT EXISTS raw_job_posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    job_id TEXT,
    title TEXT,
    location TEXT,
    department TEXT,
    salary_range TEXT,
    company_profile LONGTEXT,
    description LONGTEXT,
    requirements LONGTEXT,
    benefits LONGTEXT,
    telecommuting INT,
    has_company_logo INT,
    has_questions INT,
    employment_type VARCHAR(100),
    required_experience VARCHAR(100),
    required_education VARCHAR(100),
    industry VARCHAR(255),
    function_field VARCHAR(255),
    fraudulent INT
);

CREATE TABLE IF NOT EXISTS predictions (
    prediction_id INT PRIMARY KEY AUTO_INCREMENT,
    job_id INT,
    predicted_label BOOLEAN,
    confidence_score FLOAT,
    model_used VARCHAR(100),
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);