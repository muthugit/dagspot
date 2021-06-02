from dagster import pipeline, repository, solid

from functools import wraps


def ddd():
    """Tees"""
    pass

@solid
def hello_world_solid(context, dagspot_context=None):
    """This is the hello world solid for quick try
    """
    context.log.info("Running from dagspot")
    if dagspot_context is None:
        context.log.info("No Dagspot context found")
    else:
        context.log.info("Dagspot context found")

@solid(
    name="Hello2"
)
def hello_world_v2_solid(context, dagspot_context=None):
    """This is the hello world solid for quick try
    """
    context.log.info("Running from dagspot")
    if dagspot_context is None:
        context.log.info("No Dagspot context found")
    else:
        context.log.info("Dagspot context found")

# assert hello_world_solid