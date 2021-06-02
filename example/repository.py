from dagster import pipeline, repository, solid

from dagspot.solids.hello_world import hello_world_solid
from dagspot.pipelines.hello_world import my_pipeline

@solid
def second():
    return "done"

@pipeline
def hello_world_pipeline():
    res=second()
    hello_world_solid(res)


@repository
def hello_world_repository():
    return [hello_world_pipeline, my_pipeline]