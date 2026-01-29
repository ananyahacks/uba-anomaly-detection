# User Behavior Anomaly Detection (UBA)

This project implements a User Behavior Anomaly Detection system using
synthetic data generation and unsupervised machine learning.

## Tech Stack
- Python
- Faker (Synthetic Data)
- Pandas, NumPy
- Scikit-learn
- Isolation Forest
- One-Class SVM

## Project Structure
     uba_project/
       ├── scripts/
       │ ├── generate_fake_data.py/
       │ ├── data_cleaning.py/
       │ ├── feature_engineering.py/
       ├── notebooks/
       ├── data/
       │ ├── raw/
       │ ├── processed/
       │ └── results/

### Scripts

The `scripts/` directory contains the core data pipeline components:
- `generate_fake_data.py`  
  Generates reproducible synthetic user and activity log datasets using Faker.
- `data_cleaning.py`  
  Performs basic data validation, type enforcement, and removal of duplicates and invalid records.
- `feature_engineering.py`  
  Extracts behavioral features (e.g., login frequency, access frequency, data transfer volume, time deviation) for downstream anomaly detection models.

## Data Generation & Preprocessing

This project uses reproducible synthetic data generated using the Faker library.

After cloning the repository, run the following commands from the project root
to generate and preprocess the datasets locally:

```bash
python scripts/generate_fake_data.py
python scripts/data_cleaning.py
python scripts/feature_engineering.py
