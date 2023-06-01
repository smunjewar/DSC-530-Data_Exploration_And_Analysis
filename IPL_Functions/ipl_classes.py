class Ball:
    ballNumber = 0.0
    batsman = ""
    bowler = ""
    nonStriker = ""
    runsBat = 0
    runsExtras = 0
    runsTotal = 0

    def __init__(self, ball):
        for ballNumber, ballDetails in ball.items():
            self.ballNumber = float(ballNumber)
            self.batsman = ballDetails["batsman"]
            self.bowler = ballDetails["bowler"]
            self.nonStriker = ballDetails["non_striker"]
            self.runsBat = ballDetails["runs"]["batsman"]
            self.runsExtras = ballDetails["runs"]["extras"]
            self.runsTotal = ballDetails["runs"]["total"]

    def tostring(self):
        return (
            "Ball Number:"
            + self.ballNumber
            + " Batsman:"
            + self.batsman
            + " Bowler:"
            + self.bowler
            + " Non Striker:"
            + self.nonStriker
            + "Runs Bat:"
            + self.runsBat
            + "Runs Extras:"
            + self.runsExtras
            + "Runs Total:"
            + self.runsTotal
        )


class Innings:
    number = 0
    team = ""
    balls = []
    openingBatsman1 = ""
    openingBatsman2 = ""

    def __init__(self, inning, number):
        self.team = inning["team"]
        self.number = number
        self.balls = []
        count = 1
        for ball in inning["deliveries"]:
            ballObj = Ball(ball)
            self.balls.append(ballObj)
            if count == 1:
                self.openingBatsman1 = ballObj.batsman
                self.openingBatsman2 = ballObj.nonStriker
            count += 1

    def tostring(self):
        return (
            "Number:"
            + self.number
            + " Team:"
            + self.team
            + +" Opener 1:"
            + self.openingBatsman1
            + " Opener 2:"
            + self.openingBatsman2
        )


class MatchInfo:
    def __init__(self):
        self.matchId = 0
        self.innings = []
        self.city = ""
        self.date = ""
        self.winner = ""
        self.wonByRuns = 0
        self.wonByWickets = 0
        self.mom = ""
        self.team1 = ""
        self.team2 = ""
        self.tossWinner = ""
        self.tossDecision = ""
        self.innings = []

    def tostring(self) -> str:
        return (
            "MatchId:"
            + self.matchId
            + "City:"
            + self.city
            + " Date:"
            + str(self.date)
            + " Winner:"
            + self.winner
            + " Won By Runs:"
            + str(self.wonByRuns)
            + " Won By Wickets:"
            + str(self.wonByWickets)
            + " Mom:"
            + self.mom
            + " Team1:"
            + self.team1
            + " Team2:"
            + self.team2
            + " Toss Winner:"
            + self.tossWinner
            + " Toss Decision:"
            + self.tossDecision
        )

    def appendcsvdata(self, output, data) -> str:
        return output + "," + '"' + str(data) + '"'

    def getcsv(self) -> str:
        output = self.getcsvHeader()
        for inning in self.innings:
            for ball in inning.balls:
                row = '"' + str(self.matchId) + '"'
                row = self.appendcsvdata(row, self.date)
                row = self.appendcsvdata(row, self.city)
                row = self.appendcsvdata(row, self.team1)
                row = self.appendcsvdata(row, self.team2)
                row = self.appendcsvdata(row, self.tossWinner)
                row = self.appendcsvdata(row, self.tossDecision)
                row = self.appendcsvdata(row, self.mom)
                row = self.appendcsvdata(row, self.winner)
                row = self.appendcsvdata(row, self.wonByRuns)
                row = self.appendcsvdata(row, self.wonByWickets)
                row = self.appendcsvdata(row, inning.number)
                row = self.appendcsvdata(row, inning.team)
                row = self.appendcsvdata(row, inning.openingBatsman1)
                row = self.appendcsvdata(row, inning.openingBatsman2)
                row = self.appendcsvdata(row, ball.ballNumber)
                row = self.appendcsvdata(row, ball.batsman)
                row = self.appendcsvdata(row, ball.bowler)
                row = self.appendcsvdata(row, ball.nonStriker)
                row = self.appendcsvdata(row, ball.runsBat)
                row = self.appendcsvdata(row, ball.runsExtras)
                row = self.appendcsvdata(row, ball.runsTotal)

                output += row + "\n"

        return output

    def getcsvHeader(self) -> str:
        output = ""
        row = "MatchId"
        row = self.appendcsvdata(row, "Date")
        row = self.appendcsvdata(row, "City")
        row = self.appendcsvdata(row, "Team1")
        row = self.appendcsvdata(row, "Team2")
        row = self.appendcsvdata(row, "TossWinner")
        row = self.appendcsvdata(row, "TossDecision")
        row = self.appendcsvdata(row, "ManOfTheMatch")
        row = self.appendcsvdata(row, "Winner")
        row = self.appendcsvdata(row, "WonByRuns")
        row = self.appendcsvdata(row, "WonByWickets")
        row = self.appendcsvdata(row, "InningNo")
        row = self.appendcsvdata(row, "BattingTeam")
        row = self.appendcsvdata(row, "Opener1")
        row = self.appendcsvdata(row, "Opener2")
        row = self.appendcsvdata(row, "BallNo")
        row = self.appendcsvdata(row, "Batsman")
        row = self.appendcsvdata(row, "Bowler")
        row = self.appendcsvdata(row, "NonStriker")
        row = self.appendcsvdata(row, "RunsBat")
        row = self.appendcsvdata(row, "RunsExtras")
        row = self.appendcsvdata(row, "TotalRuns")

        output += row + "\n"

        return output