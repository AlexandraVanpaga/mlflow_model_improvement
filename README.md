Здравствуйте!



Здесь лежит проект по улучшению Baseline-модели ля определения цен на недвижимость.
Цель: улучшить базовую catboost-модель через отбор фичей и настройку гиперпараметров.
Данные: датасет с инфо о недвижимости в г. Москва.
Доступ к проекту:
git clone https://github.com/AlexandraVanpaga/mle-project-sprint-2-v001.git
cd mle-project-sprint-2-v001
pip install -r requirements.txt

ЭТАП 1:

- Инструкция по поднятию Mlflow: запускается командой sh run_mlflow.sh
- id эксперимента с базовой моделью в MLflow: 7
- название эксперимента с базовой моделью в Mlflow: baseline_model_experiment
- Залогирована базовая модель, метрики, initial_data, параметры из файла params.yaml

ЭТАП 2:
- id эксперимента с EDA в MLflow: 9
- название эксперимента в Mlflow: eda
- notebook_path = "/home/mle-user/mle_projects/mle-project-sprint-2-v001/EDA.ipynb"
- summary_path = "/home/mle-user/mle_projects/mle-project-sprint-2-v001/eda_summary.md"
- data_path = "/home/mle-user/mle_projects/mle-project-sprint-2-v001/df_filtered.csv" - также залогировала очищенные данные



