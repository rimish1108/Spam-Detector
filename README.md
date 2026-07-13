# 📧 Email/SMS Spam Detector using Machine Learning

A Machine Learning-based web application that classifies **Email** and **SMS** messages as **Spam** or **Not Spam (Ham)**. This project leverages **Natural Language Processing (NLP)** techniques and supervised Machine Learning algorithms to detect unwanted messages with high accuracy.

---

# 📖 Table of Contents

* Project Overview
* Features
* Tech Stack
* Project Structure
* Dataset
* Machine Learning Workflow
* Installation
* Execution Steps
* Model Training
* How to Use
* Results
* Future Improvements
* Contributing
* License
* Author

---

# 🚀 Project Overview

Spam messages are one of the most common problems in digital communication. This project demonstrates how Machine Learning can automatically classify incoming Email or SMS messages into:

* ✅ Ham (Legitimate Message)
* ❌ Spam (Unwanted Message)

The model is trained using a labeled dataset and employs Natural Language Processing (NLP) techniques to preprocess text before making predictions.

---

# ✨ Features

* Detects Spam and Ham messages.
* Supports Email and SMS text.
* Real-time prediction.
* Clean and interactive web interface.
* Text preprocessing using NLP.
* High accuracy Machine Learning model.
* Easy to extend with larger datasets.

---

# 🛠 Tech Stack

## Programming Language

* Python 3.x

## Libraries

* Pandas
* NumPy
* Scikit-learn
* NLTK
* Matplotlib
* Seaborn
* Pickle

## Frontend

* HTML
* CSS

## Backend

* Flask

## Development Environment

* Jupyter Notebook
* VS Code

---

# 📂 Project Structure

```text
Email-SMS-Spam-Detector/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── spam.csv
├── requirements.txt
├── README.md
│
├── templates/
│     └── index.html
│
├── static/
│     ├── style.css
│     └── images/
│
├── notebook/
│     └── Spam_Detection.ipynb
│
└── utils/
      └── preprocessing.py
```

---

# 📊 Dataset

The project uses a labeled Spam dataset containing:

* Message
* Label (Spam / Ham)

Example:

| Label | Message                                                |
| ----- | ------------------------------------------------------ |
| Ham   | Hey, are we meeting today?                             |
| Spam  | Congratulations! You have won ₹50,000. Click here now. |

---

# 🤖 Machine Learning Workflow

## Step 1: Import Libraries

Load all required Python libraries.

---

## Step 2: Load Dataset

Read the dataset using Pandas.

---

## Step 3: Data Cleaning

* Remove duplicate records
* Handle missing values
* Rename columns
* Convert labels into numerical values

---

## Step 4: Exploratory Data Analysis (EDA)

* Class distribution
* Word frequency
* Message length analysis
* Visualizations

---

## Step 5: Text Preprocessing

The following NLP operations are performed:

* Lowercase conversion
* Remove punctuation
* Tokenization
* Stopword removal
* Stemming

---

## Step 6: Feature Extraction

Convert text into numerical vectors using:

* CountVectorizer
  or
* TF-IDF Vectorizer

---

## Step 7: Train-Test Split

Split the dataset into:

* Training Set
* Testing Set

---

## Step 8: Model Training

Train the Machine Learning model.

Common algorithms:

* Naive Bayes
* Logistic Regression
* Random Forest
* Support Vector Machine

---

## Step 9: Model Evaluation

Evaluate using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Step 10: Save Model

Save the trained model using Pickle.

```python
pickle.dump(model, open("model.pkl","wb"))
```

---

## Step 11: Deploy

Use Flask to create a web application for real-time predictions.

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Email-SMS-Spam-Detector.git
```

```bash
cd Email-SMS-Spam-Detector
```

---

## Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Execution Steps

### 1. Open Terminal

Navigate to the project directory.

```bash
cd Email-SMS-Spam-Detector
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Flask Application

```bash
python app.py
```

---

### 4. Open Browser

Visit:

```text
http://127.0.0.1:5000/
```

---

### 5. Enter Message

Example:

```text
Congratulations!
You have won a FREE iPhone.
Claim now.
```

---

### 6. Click Predict

Output:

```text
Spam
```

or

```text
Not Spam
```

---

# 💻 How to Train the Model Again

Run the notebook:

```bash
jupyter notebook
```

Open

```text
Spam_Detection.ipynb
```

Execute all cells.

New files generated:

* model.pkl
* vectorizer.pkl

---

# 📈 Results

Typical model performance:

| Metric    | Score   |
| --------- | ------- |
| Accuracy  | 97%–99% |
| Precision | High    |
| Recall    | High    |
| F1 Score  | High    |

> *Actual performance may vary depending on the dataset, preprocessing pipeline, and selected Machine Learning algorithm.*

---

# 🎯 Future Improvements

* Deep Learning (LSTM/GRU)
* BERT-based Spam Detection
* Email attachment scanning
* URL analysis
* Multi-language spam detection
* Cloud deployment (AWS/Azure/GCP)
* REST API integration
* User authentication
* Spam confidence score
* Docker containerization

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📜 License

This project is intended for educational and learning purposes. You may use, modify, and share it with appropriate attribution.

---

# 👨‍💻 Author

**Rimish Chandra Srivastava**

* AI Project Engineer
* Machine Learning Enthusiast
* Python Developer
* Full Stack Developer
* Passionate about AI, Machine Learning, and Data Science

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
