
# 🏏 IPL Match Winner & Player Performance Predictor

An end-to-end Machine Learning project that predicts **IPL match outcomes** and identifies the **Player of the Match** using historical match and ball-by-ball data.

---

## 🚀 Project Overview

This project leverages historical IPL datasets to build a predictive system that can:

* 🔮 Predict the **winning team** of a match
* 🌟 Identify the **best performing player (Player of the Match)**
* 📊 Utilize both match-level and ball-by-ball data for deeper insights
* 🎨 Provide predictions through a **modern Streamlit web application**

The goal of this project is not just prediction, but building a **complete ML pipeline + deployable product**.

---

## 🧠 Key Features

* ✅ Match Winner Prediction using Machine Learning
* ✅ Player Performance Analysis using ball-by-ball data
* ✅ Feature Engineering (Team Form, Head-to-Head stats)
* ✅ Random Forest Model for robust predictions
* ✅ Clean and interactive Streamlit UI
* ✅ End-to-End ML workflow (Data → Model → UI)

---

## 📊 Dataset Used

This project uses two datasets:

1. **Matches Dataset**

   * Contains match-level information like teams, toss, venue, and winner

2. **Deliveries Dataset**

   * Ball-by-ball data used to compute player performance metrics

---

## ⚙️ Machine Learning Approach

### 🔹 Feature Engineering

Custom features were created to improve prediction accuracy:

* **Team Form** → Recent performance of teams
* **Head-to-Head Stats** → Historical dominance between teams
* **Toss Impact** → Influence of toss decisions
* **Venue Effect** → Ground-specific trends

---

### 🔹 Model Selection

* Baseline: Logistic Regression
* Final Model: **Random Forest Classifier**

Why Random Forest?

* Handles non-linear patterns
* Works well with categorical + engineered features
* Provides better accuracy compared to baseline

---

## 🌟 Player Performance Model

Instead of directly predicting Player of the Match, a **performance scoring system** was built:

### Metrics Used:

* Runs scored
* Strike rate
* Wickets taken

### Performance Score Formula:

```
Performance Score = Runs + (Wickets × 20) + (Strike Rate × 0.1)
```

The player with the highest score in a match is selected as the **Player of the Match**.

---

## 🏗️ Project Structure

```
IPL_Project/
│
├── app.py                # Streamlit frontend
├── backend.py            # Prediction logic
├── train_model.py        # Model training script
├── winner_model.pkl      # Trained model
├── columns.pkl           # Feature columns
│
├── data/
│   ├── data.csv
│   ├── deliveries.csv
│
└── requirements.txt
```

---

## 💻 How to Run the Project

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Train the Model

```
python train_model.py
```

### 3️⃣ Run the App

```
streamlit run app.py
```

---

## 🎨 UI Preview

The application provides:

* Clean input selection for teams, toss, and venue
* Prediction output with:

  * 🏆 Winning Team
  * 🌟 Player of the Match
* Modern gradient-based UI using Streamlit

---

## 📈 Future Improvements

* 🔄 Real-time feature calculation (dynamic team form)
* 📊 Win probability visualization
* 🧠 Advanced models (XGBoost, LightGBM)
* 🌐 Deployment on cloud (Streamlit Cloud / AWS)
* 🏏 Integration with live match APIs

---

## 💡 Key Learnings

* End-to-end ML pipeline development
* Feature engineering for sports analytics
* Model selection and evaluation
* Building deployable ML applications using Streamlit
* Structuring real-world ML projects

---

## 🤝 Acknowledgements

* IPL datasets from public sources
* Inspiration from real-world sports analytics

---

## 📬 Contact

If you liked this project or have suggestions, feel free to connect!

---

⭐ If you found this useful, consider giving this repo a star!
