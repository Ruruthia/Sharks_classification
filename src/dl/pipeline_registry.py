"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from .pipelines import data_split, data_processing


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_split_pipeline = data_split.create_pipeline()
    data_processing_pipeline = data_processing.create_pipeline()

    return {
        "__default__": pipeline([data_split_pipeline, data_processing_pipeline]),
        "data_split": data_split_pipeline,
        "data_processing": data_processing_pipeline,
    }
