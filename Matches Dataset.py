import requests
import apiKey
import numpy as np
import matplotlib.pyplot as plt


region1: str = "jp1"
region2: str = "asia"
summonerId: str = apiKey.Id
apiKey = apiKey.Key

class RankedMatches:
    def __init__(self, region1: str, region2: str, summonerId: str, apiKey: str):
        self.puuid = self.retrievePuuid(region1, summonerId, apiKey)
        self.ListOfRankedMatches = self.retrieveListOfRankedMatches(region2, self.puuid, apiKey)
        self.data = self.matchData(region2, self.ListOfRankedMatches, apiKey)

    # Need puuid to retrieve match list for a summoner
    def retrievePuuid(self, region: str, summonerId: str, apiKey: str) -> str:
        ''''Retrieves puuid from Riot's API'''
        summonerDataURL: str = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerId + "?api_key=" + apiKey
        return requests.get(summonerDataURL).json()["puuid"]

    # Acceptable regions are asia, america, etc
    def retrieveListOfRankedMatches(self, region: str, puuid: str, apiKey: str) -> list:
        '''Retrieves list of ranked matches for a player'''
        summonerMatchesURL: str = "https://" + region + ".api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?api_key=" + apiKey
        return requests.get(summonerMatchesURL, params= {"type": "ranked", "count": "10"}).json()


    # Acceptable regions are asia, america, etc
    def matchData(self, region: str, matches: list, apiKey: str) -> list:
        '''Returns an array of match data, with n features and binary label'''
        matchList = []
        for match in matches:
            matchDataURL: str = "https://" + region + ".api.riotgames.com/lol/match/v5/matches/" + match + "?api_key=" + apiKey
            matchData = requests.get(matchDataURL).json()
            matchInfo = matchData["info"]
            participants = matchInfo["participants"]
            for participant in participants:
                if participant["summonerName"] == summonerId:
                    if participant["win"]:
                        matchList.append([match, 1])
                    else:
                        matchList.append([match, 0])
        return matchList


myMatchList = RankedMatches(region1, region2, summonerId, apiKey)
print(myMatchList.data)

# The output is an n-dimensional array of matches with win/loss in the nth position
# The first position is the match number, and one can add features like damage per minute to analyze later


# 1 represents win, 0 represents loss

xValues = []
yValues = []



for match in myMatchList.data:
    xValues.append(match[0])
    yValues.append(match[1])

plt.plot(xValues, yValues, 'ro')
plt.show()
