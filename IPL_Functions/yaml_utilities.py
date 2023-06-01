from io import StringIO

import pandas as pd
import yaml

from IPL_Functions.ipl_classes import Ball, Innings, MatchInfo


def readYamlToDataFrame(matchId: int, fileContent: str) -> pd.DataFrame:

    match = MatchInfo()
    match.matchId = matchId
    for key, value in fileContent.items():
        # print (key + " : " + str(value))
        if key == "info":
            if "city" in value:
                match.city = value["city"]
            elif "neutral_venue" in value:
                match.city = str(value["neutral_venue"])
                if "venue" in value:
                    match.city += "-" + str(value["venue"])

            match.date = value["dates"][0]
            if "result" in value["outcome"]:
                match.winner = value["outcome"]["result"]
            if "by" in value["outcome"]:
                match.winner = value["outcome"]["winner"]
                if "runs" in value["outcome"]["by"]:
                    match.wonByRuns = value["outcome"]["by"]["runs"]
                elif "wickets" in value["outcome"]["by"]:
                    match.wonByWickets = value["outcome"]["by"]["wickets"]
            if "player_of_match" in value:
                match.mom = value["player_of_match"][0]
            match.team1 = value["teams"][0]
            match.team2 = value["teams"][1]
            match.tossWinner = value["toss"]["winner"]
            match.tossDecision = value["toss"]["decision"]
        if key == "innings":
            inningCount = 0
            for inning in value:
                inningCount += 1
                match.innings.append(Innings(inning[getFirstKey(inning)], inningCount))

    fileDf = pd.read_csv(StringIO(match.getcsv()))
    return fileDf


def getFirstKey(dictionar):
    for key in dictionar:
        return key


def readYamlsIntoDataFrame(yamlFileContent, matchId) -> pd.DataFrame:
    """
       method to read zip file and read all yaml files and combine them into pandas data frame  and return data frame
       also adding MatchId column
    """
    yamlFile = yaml.load(yamlFileContent, Loader=yaml.FullLoader)
    fileDf = readYamlToDataFrame(matchId, yamlFile)

    return fileDf
