import requests

url = "https://api-nba-v1.p.rapidapi.com/games/teamId/2"

headers = {
    'x-rapidapi-key': "3131186340mshe8d1e6e635a70cfp124eb3jsnb07a63826178",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)