from dotenv import load_dotenv
import os

# --- Загружаем переменные окружения из .env ---
load_dotenv()

os.environ["MLFLOW_S3_ENDPOINT_URL"] = "https://storage.yandexcloud.net"
os.environ["AWS_ACCESS_KEY_ID"] = os.getenv("AWS_ACCESS_KEY_ID")
os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv("AWS_SECRET_ACCESS_KEY")

import mlflow
import mlflow.sklearn
import pandas as pd
import joblib
import json
import yaml
from mlflow.models.signature import infer_signature
from utils import bool_to_int

# Пути к файлам
BASE_PATH = "baseline_model"
MODEL_PATH = os.path.join(BASE_PATH, "fitted_model.pkl")
DATA_PATH = os.path.join(BASE_PATH, "initial_data.csv")
CV_RESULTS_PATH = os.path.join(BASE_PATH, "cv_res.json")
PARAMS_PATH = os.path.join(BASE_PATH, "params.yaml")

# 0. Указываем MLflow сервер
mlflow.set_tracking_uri("http://localhost:5000")  # если сервер локальный

# 1. Загружаем модель, данные и метрики
model = joblib.load(MODEL_PATH)
data = pd.read_csv(DATA_PATH)
with open(CV_RESULTS_PATH, "r") as f:
    metrics = json.load(f)

with open(PARAMS_PATH, "r") as f:
    params = yaml.safe_load(f)

# 2. Определяем X и y для сигнатуры
target_col = params.get("target_col", "price")  # берём target из params.yaml
X = data.drop(columns=[target_col])
y = data[target_col]

signature = infer_signature(X, model.predict(X))

# 3. Логируем в MLflow на сервере
mlflow.set_experiment("baseline_model_experiment")

with mlflow.start_run(run_name="baseline_model_run"):

    # --- Логируем параметры из params.yaml ---
    for k, v in params.items():
        if isinstance(v, dict):
            for subk, subv in v.items():
                mlflow.log_param(f"{k}.{subk}", subv)
        else:
            mlflow.log_param(k, v)
    
    # --- Логируем метрики ---
    for k, v in metrics.items():
        mlflow.log_metric(k, v)
    
    # --- Логируем модель с сигнатурой ---
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        signature=signature,
        registered_model_name="Baseline_CatBoost_Model"
    )
    
    # --- Логируем артефакты ---
    mlflow.log_artifact(DATA_PATH, artifact_path="data")
    mlflow.log_artifact(CV_RESULTS_PATH, artifact_path="cv_results")
    mlflow.log_artifact(PARAMS_PATH, artifact_path="params")

print("Модель, параметры, метрики и артефакты успешно залогированы и зарегистрированы в MLflow на сервере!")
