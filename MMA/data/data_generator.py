import csv
from faker import Faker
import random

fake = Faker()

num_players = 300
filename = 'player_info.csv'


def generate_players_data(num_players):
    players_data = []
    generated_usernames = set()

    while len(players_data) < num_players:
        username = fake.user_name()
        if username not in generated_usernames:
            # rank = random.randint(0, 750)
            strength = random.randint(0, 1000) #random.random()
            rank = 0
            wins = 1
            losses = 1
            draws = 1
            penultimate_outcome = 0
            last_outcome = 0

            player_data = [username, strength, rank, wins, losses, draws, penultimate_outcome, last_outcome]
            players_data.append(player_data)
            generated_usernames.add(username)

    return players_data


def write_players_data_to_csv(players_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['username', 'strength', 'rank', 'wins', 'losses', 'draws', 'penultimatеOutcome', 'lastOutcome'])
        writer.writerows(players_data)


players_data = generate_players_data(num_players)
write_players_data_to_csv(players_data, filename)

print(f"CSV file '{filename}' with {num_players} players generated.")
