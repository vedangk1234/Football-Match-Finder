import requests

# Enter your API key here
api_key = "01197cf3977a4f4c8ebd22db4224e89b"

# Ask for the date you want to retrieve matches for (in format YYYY-MM-DD)
match_date = input("Enter the date you want to retrieve matches for (in format YYYY-MM-DD): ")

# Send a request to the API to retrieve matches for the specified date
url = f"https://api.football-data.org/v2/matches?dateFrom={match_date}&dateTo={match_date}"
headers = {
    "X-Auth-Token": api_key
}
response = requests.get(url, headers=headers)

# Check if the API returned any data and process it if so
if response.status_code == 200:
    data = response.json()["matches"]
    if data:
        for match in data:
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            home_score = match["score"]["fullTime"]["homeTeam"]
            away_score = match["score"]["fullTime"]["awayTeam"]
            print(f"{home_team} {home_score} - {away_score} {away_team}")
    else:
        print("No matches found for the specified date.")
else:
    print(f"Error retrieving matches: {response.status_code}")
