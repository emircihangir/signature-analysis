# ✍️ Signature Authenticator – AI Model (Time Series Classification)

This repository contains the code and files related to training and evaluating the AI model used in my **Signature Authenticator** project. The model is trained to recognize temporal patterns in my handwriting and distinguish it from others.

For simplicity, the input is based on writing the uppercase letter **"A"** by hand. The data is treated as a time series — capturing pen movement over time — rather than static images.

> 📁 Note: This repo only includes the AI model. Data collection and inference apps are available in separate repositories.

---

## 🔍 Project Overview

- **Goal:** Train a model that can identify whether a handwriting sample (of the letter "A") was written by me or someone else.
- **Approach:** Treat handwriting as a time series (e.g., pen stroke coordinates, velocities).
- **Context:** Part of a multi-repo project including:
  - The **data collection app** for recording handwriting samples
  - The **inference app** that uses this model for real-time signature authentication

---

## 🧠 Model Details

- **Input:** Sequences of pen coordinates over time (`x`, `y`, `timestamp`)
- **Model Type:** Time Series Classifier
- **Architecture:** Variants experimented with include:
  - 1D Convolutional Networks (Conv1D)
  - Recurrent Networks (e.g., LSTM, GRU)
- **Output:** Binary classification — *Written by me* vs. *Not written by me*
- **Evaluation:** Training loss, training accuracy, validation loss, validation accuracy

---

## 🔧 Tools & Libraries

- **Python**
- **TensorFlow / Keras**
- **NumPy, Matplotlib** for data manipulation and visualization
- **Jupyter Notebook** for prototyping and training
- **Git** for version control

---

## ✅ Skills Demonstrated

- Time series preprocessing and normalization  
- Model architecture design and training using Keras  
- Avoiding overfitting with regularization and data balancing  
- Evaluating binary classifiers with real-world, user-collected data
- Detailed data inspection for dataset analysis
- Working with a modular architecture across separate apps (data collection, training, inference)

---

## 🔬 Results

- **Validation Accuracy:** ~91%  
- **Observations:** The model can effectively learn personal handwriting patterns, even from a single character, when represented as sequential data.
