import mlflow
import mlflow.sklearn

from src.package.ingest_data import data_ingest
from src.package.score import score_values
from src.package.train import train

remote_server_uri = "http://127.0.0.1:5000"
mlflow.set_tracking_uri(remote_server_uri)
exp_name = "Housing_Price_Pred"
mlflow.set_experiment(exp_name)

with mlflow.start_run(
    experiment_id=1, run_name="House Price Prediction"
) as run:
    data_ingest()
    train()
    result = score_values()
