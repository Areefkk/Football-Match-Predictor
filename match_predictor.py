import pandas as pd
from bs4 import BeautifulSoup
import requests

## Creates a soup to extract the HTML code for the website
url = 'https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'
res = requests.get(url)
content = res.text
soup = BeautifulSoup(content, 'lxml')

match_data = soup.find_all('div', class_='footballbox')

## Extracts the data/scores for the home and away teams
for match in match_data:
    home_team.append(match.find('th', class_='fhome').get_text())
    score.append(match.find('th', class_='fscore').get_text())
    away_team.append(match.find('th', class_='faway').get_text())

dict_football = {'home_team': home_team, 'score': score, 'away_team': away_team}
df_football = pd.DataFrame(dict_football)

df_football.to_csv("fifa_worldcup_data.csv", index=False)

def predict(home_team, away_team):

    # Calculate the value of lambda (λ) for both Home Team and Away Team.
    if home_team in df_football.index and away_team in df_football.index:
        lambda_home_team = df_football.at[home_team,'GoalsScored'] * df_football.at[away_team,'GoalsConceded']
        lambda_away_team = df_football.at[away_team,'GoalsScored'] * df_football.at[home_team,'GoalsConceded']

p = poisson.pmf(x, lambda_home_team) * poisson.pmf(y, lambda_away_team)
if x == y:
    pr_draw += p
elif x > y:
    pr_home += p
else:
    pr_away += p

points_home_team = 3 * pr_home + pr_draw
points_away_team = 3 * pr_away + pr_draw