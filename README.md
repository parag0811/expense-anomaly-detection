# Behavioral Anomaly Detection for Expense App

This repository contains the machine learning pipeline powering anomaly detection in my live QuickSplit expense splitter application.

Instead of relying only on global spending patterns, the system models user-specific behavior and detects deviations using a time-aware Isolation Forest approach.

# 🚀 About QuickSplit

QuickSplit is a group-based expense splitting application where users:

Create groups

Add shared expenses

Track balances

Settle payments

This ML module enhances QuickSplit by automatically identifying suspicious or unusual spending behavior.

## Problem

Detect suspicious or unusual expenses in a group-based expense tracking system.

-Key Challenges

Users have different spending habits.

Large amounts are not always anomalies.

Behavioral baselines differ across users.

Data leakage must be strictly avoided when computing user-level statistics.

## Approach

The system simulates real-time behavior by processing expenses chronologically.

-For each expense, it:

Computes past transaction count (per user)

Calculates user average spending using past data only

Measures deviation from the user’s normal behavior

Computes time gap between transactions

Updates user state after feature computation

-This ensures:

No future information leaks into past predictions

Realistic production-like behavioral modeling

User-relative anomaly detection rather than global-only detection

## Engineered Features

- amount
- hour
- day_of_week
- past_transaction_count
- user_avg_amount
- amount_minus_user_avg
- time_gap_minutes

## Model

Algorithm: Isolation Forest  
Library: scikit-learn  

The model detects behavioral anomalies by identifying deviations from learned patterns.

The inference pipeline returns:
{
  "anomaly_score": float,
  "is_suspicious": boolean
}


## Project Structure

data/
  raw/
  processed/

models/
  anomaly_model.pk
  scaler.pk

notebooks/

src/
  data_prep/
  inference/
  training/

generate_data

## How to Run

1. Create virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Run training script:
   python src/training/train.py
4. Run inference:
   python src/inference/inference.py

## Results

The upgraded model with user-aware features reduces false positives for high-spending users and better detects sudden deviations from normal behavior.
