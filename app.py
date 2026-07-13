from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "spam.csv"


@st.cache_resource
def load_pipeline():
    df = pd.read_csv(
        DATA_PATH,
        encoding="latin-1",
        usecols=[0, 1],
        names=["label", "message"],
        skiprows=1,
    )
    df = df.dropna(subset=["label", "message"])
    df["label"] = df["label"].map({"ham": 0, "spam": 1}).astype(int)

    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer(stop_words="english")),
            ("classifier", MultinomialNB()),
        ]
    )
    pipeline.fit(df["message"].astype(str), df["label"])
    return pipeline


pipeline = load_pipeline()

st.set_page_config(page_title="Spam Classifier", page_icon="📧")
st.title("Email/SMS Spam Classifier")

input_sms = st.text_area(
    "Enter the message",
    value="Congratulations! You have won a free prize. Claim now.",
)

if st.button("Predict"):
    if not input_sms.strip():
        st.warning("Please enter a message before predicting.")
    else:
        result = pipeline.predict([input_sms])[0]
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")
