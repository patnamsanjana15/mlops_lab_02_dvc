

#  DVC Lab — Data Version Control with Google Cloud Storage + ML

## Overview

This project demonstrates how **Data Version Control (DVC)** can be used to manage and version large datasets in a machine learning workflow, while storing data remotely in **Google Cloud Storage (GCS)** and tracking code/metadata with **GitHub**.

The **CC_GENERAL credit card dataset** is tracked using DVC.
Multiple dataset versions are created and stored in Google Cloud.
A simple **KMeans clustering model** is added to show ML integration.

This lab simulates a real MLOps pipeline:

* Git → code + metadata
* DVC → dataset hashes + tracking
* Google Cloud → actual data storage

---

## Tools Used

* Python
* DVC
* Google Cloud Storage
* Google Cloud CLI
* scikit-learn
* pandas
* Git / GitHub

---

## Project Structure

```
mlops_lab_02_dvc/
│
├── data/
│   └── CC_GENERAL.csv.dvc
│
├── train.py
├── .dvc/
├── README.md
└── .gitignore
```

> Note: The raw CSV file is **not stored in GitHub**.
> It is stored remotely in Google Cloud via DVC.

---

## How to Reproduce This Lab

### 1. Clone Repository

```bash
git clone https://github.com/patnamsanjana15/mlops_lab_02_dvc.git
cd mlops_lab_02_dvc
```

---

### 2. Install Dependencies

```bash
pip install dvc[gs] pandas scikit-learn
```

---

### 3. Authenticate with Google Cloud

```bash
gcloud init
gcloud auth application-default login
```

---

### 4. Pull Dataset from DVC

```bash
dvc pull
```

This downloads the dataset from Google Cloud into local workspace.

---

### 5. Run ML Model

```bash
python train.py
```

This runs a **KMeans clustering model** on:

* BALANCE
* PURCHASES
* CREDIT_LIMIT

and prints cluster counts and sample results.

---

## Machine Learning Modification

### Model Used

**KMeans Clustering**

### Features

* BALANCE
* PURCHASES
* CREDIT_LIMIT

### Steps:

1. Load CSV
2. Select numeric features
3. Scale using StandardScaler
4. Apply KMeans (3 clusters)
5. Print cluster distribution

This demonstrates basic preprocessing + ML on DVC-managed data.

File: `train.py`

---

## Data Versioning with DVC

### Initial Dataset Tracking

```bash
dvc add data/CC_GENERAL.csv
git add data/CC_GENERAL.csv.dvc data/.gitignore
git commit -m "Track dataset with DVC"
dvc push
```

---

### Updating Dataset

After deleting a few rows from the CSV:

```bash
dvc add data/CC_GENERAL.csv
git commit -m "Updated dataset version"
dvc push
```

This created a **second dataset version** in Google Cloud.

---

### Rolling Back to Older Dataset Version

```bash
git checkout <old_commit_hash>
dvc checkout
```

This restores the dataset associated with that Git commit.

Then return to latest:

```bash
git checkout main
dvc checkout
```

This demonstrates full dataset reproducibility.

---

## Challenges Faced & How They Were Solved

This lab involved real-world cloud and MLOps issues.

### 1. Google Cloud Authentication Errors

**Problem:**
DVC could not authenticate using JSON keys and SSL errors occurred on macOS.

**Solution:**
Installed Google Cloud CLI and switched to OAuth authentication:

```bash
gcloud auth application-default login
```

Removed JSON credential paths from DVC and used native Google auth.

---

### 2. SSL Certificate Errors on macOS

**Problem:**
Python failed SSL verification when connecting to Google Cloud.

**Solution:**

Installed certifi and exported certificates:

```bash
export SSL_CERT_FILE=$(python -m certifi)
```

Later resolved fully by using Google Cloud CLI authentication.

---



### 3. Detached HEAD Confusion During Rollback

**Problem:**
Git showed “detached HEAD” when checking old commits.

**Solution:**
Learned this is expected during rollback testing.
Returned to main branch afterward:

```bash
git checkout main
dvc checkout
```

---

These challenges provided hands-on experience with:

* Cloud authentication
* Permissions
* SSL certificates
* DVC configuration
* Dataset reproducibility

---

## Final Outcome

* Successfully integrated DVC with Google Cloud Storage
* Created multiple dataset versions
* Demonstrated rollback using Git + DVC
* Added ML clustering model
* Documented full workflow

This lab represents a complete mini MLOps pipeline.

---

## Author

Sanjana Patnam
MLOps Lab Assignment — Northeastern University

