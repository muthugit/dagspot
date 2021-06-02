from dagster import pipeline, repository, solid
from dagspot.solids.hello_world import hello_world_solid

@pipeline
def my_pipeline():
    hello_world_solid()
