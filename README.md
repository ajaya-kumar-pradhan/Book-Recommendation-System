# 📚 Kindle Book Recommendation System

> **Unsupervised Learning · Collaborative Filtering · Streamlit · Hugging Face Deployment**

## 🚀 Live Demo
**Click the link below to try the recommendation system instantly (Free & Always On):**

### 👉 [**Launch Book Recommendation System**](https://huggingface.co/spaces/ajayapradhanconnect/Book-Recommendation-System)

---

## 📌 Project Overview
This project builds a **Collaborative Filtering recommendation engine** to provide personalized book suggestions for Amazon Kindle users. By analyzing over **5.2 Lakh ratings** from 900+ power users, the system achieves a **95.76% Recall@10**—meaning it successfully finds books you'll love nearly every single time.

### 🌟 Key Features
- **Smart Search**: Select any book from a database of thousands.
- **Instant Recommendations**: Get 5 similar books with cover images instantly.
- **Data Insights**: Interactive charts showing top publishers and authors.
- **Zero Hibernation**: Hosted on Hugging Face Spaces for 24/7 availability.

---

## 🤖 The Model (Collaborative Filtering)
The system uses a **k-Nearest Neighbors (k-NN)** approach with **Cosine Similarity**. It finds "neighbor" users who have similar reading tastes and recommends books that they highly rated but you haven't read yet.

- **Dataset**: Merged data from Books, Users, and Ratings.
- **Accuracy**: 95.76% Recall rate.
- **Speed**: Optimized using Python's `pickle` for instant model loading.

---

## 🛠️ Tech Stack
- **Backend**: Python, Scikit-learn, Pandas, NumPy.
- **Frontend**: Streamlit (with Custom CSS glassmorphism).
- **Deployment**: Hugging Face Spaces.
- **Serialization**: Pickle-mixin.

---

## 📁 Project Structure
```text
Book-Recommendation-System/
├── app.py                # Main Streamlit Application
├── requirements.txt      # Dependency List
├── model.pkl            # Trained k-NN Model
├── book_pivot.pkl       # Book-User Matrix
├── books.pkl            # metadata for display
├── logo.png             # UI branding
└── README.md            # You are here!
```

---

## 📦 Run Locally
1. **Clone the repo**
   ```bash
   git clone https://github.com/ajaya-kumar-pradhan/Book-Recommendation-System.git
   cd Book-Recommendation-System
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the app**
   ```bash
   streamlit run app.py
   ```

---

## 👤 Author
**Ajaya Kumar Pradhan**  
Data Analyst · Power BI Developer · ML Engineer  
📍 Bhubaneswar, Odisha, India

[![GitHub](https://img.shields.io/badge/GitHub-ajaya-181717?style=flat-square&logo=github)](https://github.com/ajaya-kumar-pradhan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/)

---
*Built as a Capstone Project for Unsupervised Learning.*
