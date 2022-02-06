from datetime import datetime
from mlflow.tracking import MlflowClient

client = MlflowClient()
experiments = (
    client.list_experiments()
)  # returns a list of mlflow.entities.Experiment
print(experiments)
# get the run
_run = client.get_run(run_id="f4f6d47044514cb1a89240fe870b91e6")
print(_run)

# add a tag to the run
dt = datetime.now().strftime("%d-%m-%Y (%H:%M:%S.%f)")
client.set_tag(_run.info.run_id, "deployed", dt)
