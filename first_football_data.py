import pandas as pd
import matplotlib.pyplot as plt

# Sample football player data
data = {
    'Player': ['Messi', 'Ronaldo', 'Haaland', 'Mbappé', 'Salah'],
    'Goals': [30, 28, 35, 29, 25],
    'Assists': [14, 6, 8, 10, 12]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the data
print("Football Player Stats:")
print(df)

# Calculate goal contributions (goals + assists)
df['Goal_Contributions'] = df['Goals'] + df['Assists']

# Create a simple bar chart of goal contributions
plt.figure(figsize=(10, 6))
plt.bar(df['Player'], df['Goal_Contributions'], color='blue')
plt.title('Total Goal Contributions by Player')
plt.xlabel('Player')
plt.ylabel('Goal Contributions (Goals + Assists)')
plt.savefig('player_contributions.png')
plt.show()

print("Analysis complete! Check the current folder for the saved chart.")