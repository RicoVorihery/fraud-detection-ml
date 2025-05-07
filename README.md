# 🛡️ Fraud Detection – IEEE-CIS ML Project

This repository contains a complete Machine Learning pipeline for fraud detection, using the IEEE-CIS dataset (Kaggle).  
It includes data preprocessing, feature engineering, LightGBM modeling, and a clean project structure.

## 🔧 Project Structure

- `data/raw/` – Original CSV files from Kaggle (not tracked by Git)
- `data/processed/` – Clean dataset ready for training
- `src/features.py` – Script for preprocessing & feature encoding
- `src/modeling/train.py` – LightGBM training script (coming soon)
- `notebooks/` – Exploratory analysis and modeling

## 🚀 Getting Started

# Create virtual env and install dependencies
pip install -r requirements.txt

# Generate processed data
python src/features.py

# Train model (coming soon)
python src/modeling/train.py

## 📦 Output

- **Processed dataset**: `data/processed/train_processed.csv`
- **Model artifact (soon)**: `models/model.pkl`

## 🤖 Tools Used

- Python / Pandas / Scikit-learn
- LightGBM
- Cookiecutter Data Science structure (simplified)

## 📁 .gitignore

This project excludes all CSV and model files from Git to keep the repo lightweight and secure.
