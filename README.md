# 🚗 Vehicle Classification MLOps Project

Welcome to the **Vehicle Classification MLOps Pipeline** – a production-grade, end-to-end Machine Learning system that leverages cutting-edge tools in data engineering, model training, evaluation, CI/CD, and cloud deployment. This project not only demonstrates ML model lifecycle management but also exhibits real-world MLOps principles built from scratch.

---

## 🌟 Key Features

- 🛠️ Project Scaffolding with Python Templates
- 📦 Local Packaging with `setup.py` and `pyproject.toml`
- 🧪 Modular Data Engineering Pipeline (Ingestion ➡️ Validation ➡️ Transformation)
- 📈 Model Training, Evaluation & S3 Pusher
- 🧾 Experiment Tracking and Logging
- 🌐 MongoDB Atlas for Cloud Data Storage
- ☁️ AWS S3 Integration for Model Registry
- 🐳 Dockerized + CI/CD Workflow via GitHub Actions
- 🚀 Deployed via EC2 + Self-Hosted GitHub Runner
- 🔮 Interactive Prediction Web App (Flask)

---

## 📁 Project Setup

```bash
# 1. Create project structure
python template.py

# 2. Enable local module import
# Code already available in setup.py & pyproject.toml
````

Learn more: [`crashcourse.txt`](./crashcourse.txt)

---

## 🐍 Virtual Environment & Dependencies

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list  # ✅ Verify local packages
```

---

## 🍃 MongoDB Atlas Integration

1. Sign up and create a free project & cluster (M0).
2. Setup Database User, open network access (0.0.0.0/0).
3. Retrieve connection string for Python (3.6+ driver).
4. Add dataset in `notebook/`, push to MongoDB using:

   ```ipynb
   mongoDB_demo.ipynb
   ```
5. Verify data at: MongoDB Atlas → Database → Browse Collections

---

## 📓 Logging & Exception Handling

* ✅ Built-in logger module for centralized logs
* ✅ Exception class for clean debugging
* 📊 EDA and feature engineering notebooks provided

---

## 🔁 Data Pipeline Components

### 📥 Data Ingestion

* Configuration: `constants/__init__.py`, `config/mongo_db_connection.py`
* Ingestion logic: `data_access/proj1_data.py`, `components/data_ingestion.py`
* Config Entities: `entity/config_entity.py`, `entity/artifact_entity.py`
* Run via `demo.py`

### 🧪 Data Validation

* Schema: `config/schema.yaml`
* Logic: `components/data_validation.py`
* Utility: `utils/main_utils.py`

### 🔄 Data Transformation

* Transformation & Imputation logic
* Add `estimator.py` to `entity/`

### 🧠 Model Trainer

* Model training pipeline setup
* Custom logic in `estimator.py`

---

## ☁️ AWS S3 & Model Registry

### IAM & Environment Setup

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```

### Configuration

* Bucket: `my-model-mlopsproj`
* Key: `model-registry`
* Region: `us-east-1`

### AWS Files

* `configuration/aws_connection.py`
* `aws_storage/s3_handler.py`
* `entity/s3_estimator.py`

---

## 📊 Model Evaluation & Model Pusher

* Evaluate new models
* If accuracy improvement > 0.02 ➡️ Replace existing model
* Push best model to S3 for serving

---

## 🧠 Prediction Pipeline

* Flask backend: `app.py`
* Routes:

  * `/` → Home
  * `/predict` → Model Inference
  * `/training` → Trigger training pipeline

Static assets in `static/`
Frontend templates in `template/`

---

## ⚙️ CI/CD Pipeline via GitHub Actions

### 🐳 Docker & GitHub Setup

* `Dockerfile`, `.dockerignore`
* `github/workflows/aws.yaml`

### AWS Services

* IAM User (usvisa-user)
* ECR Repository: `vehicleproj`
* EC2 Ubuntu Instance (T2 Medium)

### 🔧 GitHub Runner on EC2

1. Connect EC2 Terminal
2. Register as Self-Hosted GitHub Runner
3. Run `./run.sh`

---

## 🔐 GitHub Secrets

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_DEFAULT_REGION`
* `ECR_REPO`

---

## 🌐 Web App Deployment

1. Open EC2 Security Groups → Add Inbound TCP Rule: Port 5080
2. Access Web App:

   ```
   http://<EC2-PUBLIC-IP>:5080
   ```

---

## 🧪 Sample Routes

| Route       | Description           |
| ----------- | --------------------- |
| `/`         | Web Interface         |
| `/training` | Trigger ML Training   |
| `/predict`  | Make a New Prediction |

---

## 📌 Tech Stack

| Category           | Tools / Services               |
| ------------------ | ------------------------------ |
| Language           | Python 3.10                    |
| Data Source        | MongoDB Atlas                  |
| Web Framework      | Flask                          |
| Packaging          | `setup.py`, `pyproject.toml`   |
| Cloud Storage      | AWS S3                         |
| Model Deployment   | Docker, EC2, GitHub Runner     |
| CI/CD              | GitHub Actions + AWS ECR + EC2 |
| Environment Config | dotenv, conda                  |

---


## 🌟 Final Thoughts

This project exemplifies **ML Engineering Best Practices** using **MLOps concepts** — from **development to deployment**.
It’s a one-stop template to **productionize ML pipelines** with real-world tools.

Give it a ⭐ if you like the work!


