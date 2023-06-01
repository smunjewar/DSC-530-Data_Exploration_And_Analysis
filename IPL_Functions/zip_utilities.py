import concurrent.futures as cf
import time
from zipfile import ZipFile

import pandas as pd

from IPL_Functions import yaml_utilities as func_yamlutl


def extractZipAndProcess(zipName: str) -> pd.DataFrame:
    """
       Method to read all yaml files and combine them into pandas data frame and return data frame with
       additional MatchId column
    """
    start = time.perf_counter()
    yamlFileContents = []
    with ZipFile(zipName, "r") as zipObj:
        for fileName in zipObj.namelist():
            if fileName.endswith(".yaml"):
                fileContents = zipObj.read(fileName).decode("utf-8")
                yamlFileContents.append(fileContents)

    df = pd.DataFrame()
    matchIds = list(range(1, len(yamlFileContents) + 1))
    with cf.ProcessPoolExecutor() as executor:
        results = executor.map(func_yamlutl.readYamlsIntoDataFrame, yamlFileContents, matchIds)
    for result in results:
        df = pd.concat([df, result], ignore_index=True)
    end = time.perf_counter()
    print(f"Done processing in {end-start} seconds")
    return df