import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
# 1. Load dataset
df = pd.read_csv("data/fake_job_postings.csv")
# 2. Keep only required columns
df = df[['description', 'fraudulent']]

# 3. Remove missing values
df = df.dropna(subset=['description'])

print(df.shape)
print(df.head())
print(df.isnull().sum())

# 4. Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# 5. Preprocessing function
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    text = " ".join([
        lemmatizer.lemmatize(word) for word in text.split()
    ])
    
    return text

# 6. Apply preprocessing
df['clean_text'] = df['description'].apply(preprocess)

# 7. TF-IDF Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    max_features=10000,
    stop_words='english',
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.9
)

X = tfidf.fit_transform(df['clean_text'])

# 8. Target variable
y = df['fraudulent']