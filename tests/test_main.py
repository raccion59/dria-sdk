import json
import os
import asyncio
from dria.factory import (Simple, StructRAGAlgorithm, StructRAGGraph, StructRAGCatalogue, StructRAGTable,
                          StructRAGSynthesize, StructRAGSimulate, StructRAGJudge,
                          StructRAGAnswer, StructRAGDecompose, StructRAGExtract, SubTopicPipeline)
from dria.client import Dria
from dria.models import Task, Model

from dria.factory import SubTopicPipeline
from dria.pipelines import PipelineConfig
from dria.client import Dria
from dria.factory import Simple
from dria.models import Model
from dria.batches import ParallelSingletonExecutor
import asyncio
from itertools import chain

dria = Dria(rpc_token=os.environ["DRIA_RPC_TOKEN"])


async def batch(instructions, singleton_instance):
    dria_client = Dria()
    singleton = singleton_instance()
    executor = ParallelSingletonExecutor(dria_client, singleton)
    executor.set_models([Model.GEMINI_15_FLASH, Model.GEMINI_15_PRO, Model.QWEN2_5_32B_FP16, Model.LLAMA3_1_8B_FP16])
    executor.load_instructions(instructions)
    return await executor.run()


def batch_run(instructions, instance):
    results = asyncio.run(batch(instructions, instance))
    with open("results.json", "w") as f:
        f.write(json.dumps(results, indent=2))
    print(results)


StructRAGSimulate

if __name__ == "__main__":
    #seeds = ['History', 'Psychology', 'Economics', 'Political Science', 'Linguistics', 'Astronomy', 'Chemistry', 'Biology', 'Environmental Science', 'Culinary Arts', 'Architecture', 'Wildlife', 'Computers', 'Food', 'Physics', 'Communication', 'Music', 'Sociology', 'Art', 'Modern Art', 'Mechanical Physics', 'Mathematics', 'Philosophy', 'Geography', 'Anthropology', 'Literature', 'Theater', 'Film', 'Education', 'Business', 'Engineering', 'Medicine', 'Law', 'Public Health', 'Data Science', 'Artificial Intelligence', 'Robotics', 'Genetics', 'Neuroscience', 'Astrophysics', 'Oceanography', 'Meteorology', 'Geology', 'Agronomy', 'Zoology', 'Botany', 'History', 'Psychology', 'Economics', 'Political Science', 'Linguistics', 'Astronomy', 'Chemistry', 'Biology', 'Environmental Science', 'Culinary Arts', 'Architecture', 'Wildlife', 'Computers', 'Food', 'Physics', 'Communication', 'Music', 'Sociology', 'Art', 'Modern Art', 'Mechanical Physics']
    #main(seeds)


    with open("results.json", "r") as f:
        data = json.load(f)
    datax = list(chain(*data))
