# https://www.football-data.co.uk/englandm.php

import matplotlib.pyplot as plt
import pandas as pd

# Path to your CSV file
file_path = "football-data-premier-league-2024-2025.csv"

# Read the CSV into a DataFrame
matches = pd.read_csv(file_path)

# print("Dataset overview:")
# print(matches.head())
# print("\nData shape:", matches.shape)
# print("\nColumns:", matches.columns.tolist())

results = matches['FTR'].value_counts(normalize=True) * 100

print(results)

results_by_team = {}
teams = sorted(list(set(matches['HomeTeam'].unique()) | set(matches['AwayTeam'].unique())))

for team in teams:
    # Home games
    home_games = matches[matches['HomeTeam'] == team]
    home_wins = home_games[home_games['FTR'] == 'H'].shape[0]
    home_draws = home_games[home_games['FTR'] == 'D'].shape[0]
    home_losses = home_games[home_games['FTR'] == 'A'].shape[0]

print(home_games)
print(home_wins)
print(home_draws)
print(home_losses)

man_utd_matches = matches[(matches['HomeTeam'] == 'Man United') | (matches['AwayTeam'] == 'Man United')]



