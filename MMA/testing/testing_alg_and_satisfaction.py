import csv
from algorithms.mm_strategies import FIFO_MM, SKILL_BASED_MM, MAX_RISK_MM, MIN_RISK_MM
from algorithms.components import Player
from algorithms.prediction import play_the_match
from algorithms.satisfaction_and_rank import calculate_satisfaction

num_of_iterations = 100


def find_max_rank(matched_players):
    max_difference = 0

    for p1, p2 in matched_players:
        rank1 = p1.rank
        rank2 = p2.rank
        rank_difference = abs(rank1 - rank2)
        max_difference = max(max_difference, rank_difference)

    return max_difference


def find_satisfaction(matched_players, individual_satisfactions):
    max_rank = find_max_rank(matched_players)

    for (p1, p2) in matched_players:
        match = (p1, p2)
        winner = play_the_match(match)
        if winner == p1:
            satisfaction_winner = calculate_satisfaction(1, p1.rank, p2.rank, max_rank)
            satisfaction_loser = calculate_satisfaction(0, p2.rank, p1.rank, max_rank)

            individual_satisfactions[p1.username] = individual_satisfactions.get(p1.username, 0) + satisfaction_winner
            individual_satisfactions[p2.username] = individual_satisfactions.get(p2.username, 0) + satisfaction_loser

            # print(f"satisfaction winner: {satisfaction_winner}, satisfaction loser {satisfaction_loser}")
        elif winner == p2:
            satisfaction_winner = calculate_satisfaction(1, p2.rank, p1.rank, max_rank)
            satisfaction_loser = calculate_satisfaction(0, p1.rank, p2.rank, max_rank)

            individual_satisfactions[p2.username] = individual_satisfactions.get(p2.username, 0) + satisfaction_winner
            individual_satisfactions[p1.username] = individual_satisfactions.get(p1.username, 0) + satisfaction_loser

    return individual_satisfactions


def find_avg_individual_satisfaction(individual_satisfactions):
    for key in individual_satisfactions.keys():
        individual_satisfactions[key] /= num_of_iterations
    return individual_satisfactions


# TODO: get
def create_players_from_csv(file_path):
    players = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)  # Skip the header row if it exists
        for row in reader:
            username = row['username']
            rank = int(row['rank'])
            wins = int(row['wins'])
            losses = int(row['losses'])
            draws = int(row['draws'])
            lastMatchOutcome = int(row['lastMatchOutcome'])
            previousMatchOutcome = int(row['previousMatchOutcome'])

            player = Player(username, rank, wins, losses, draws, lastMatchOutcome, previousMatchOutcome)
            players.append(player)
    return players


#

players = create_players_from_csv("../data/player_info.csv")
print(f"Players to match:{players}")


def simulate_1():
    individual_satisfactions = {}

    for _ in range(num_of_iterations):
        mma_random = FIFO_MM()
        matched_players = mma_random.run(players)
        # print(f"Matched pairs:{matched_players}")

        individual_satisfactions = find_satisfaction(matched_players, individual_satisfactions)

    avg_individual_satisfaction = find_avg_individual_satisfaction(individual_satisfactions)
    avg_individual_satisfaction = dict(sorted(avg_individual_satisfaction.items()))
    print(f"satisfaction FIFO:{avg_individual_satisfaction}")

    values = avg_individual_satisfaction.values()
    average = sum(values) / len(values)

    print("Average:", average)
    print(f"average player satisfaction: {average}")


def simulate_2():
    individual_satisfactions = {}

    for _ in range(num_of_iterations):
        mma_skill = SKILL_BASED_MM()
        matched_players = mma_skill.run(players)
        # print(f"Matched pairs:{matched_players}")

        individual_satisfactions = find_satisfaction(matched_players, individual_satisfactions)

    avg_individual_satisfaction = find_avg_individual_satisfaction(individual_satisfactions)
    avg_individual_satisfaction = dict(sorted(avg_individual_satisfaction.items()))

    print(f"avg satisfaction SkillBased:{avg_individual_satisfaction}")

    values = avg_individual_satisfaction.values()
    average = sum(values) / len(values)

    print("Average:", average)
    print(f"average player satisfaction: {average}")


def simulate_3():
    individual_satisfactions = {}

    for _ in range(num_of_iterations):
        mma_worst = MAX_RISK_MM()
        matched_players = mma_worst.run(players)
        # print(f"Matched pairs:{matched_players}")

        individual_satisfactions = find_satisfaction(matched_players, individual_satisfactions)

    avg_individual_satisfaction = find_avg_individual_satisfaction(individual_satisfactions)
    avg_individual_satisfaction = dict(sorted(avg_individual_satisfaction.items()))

    print(f"satisfaction WORST:{avg_individual_satisfaction}")

    values = avg_individual_satisfaction.values()
    average = sum(values) / len(values)

    print("Average:", average)
    print(f"average player satisfaction: {average}")


def simulate_4():
    individual_satisfactions = {}

    for _ in range(num_of_iterations):
        mma_MIN_RISK_MM = MIN_RISK_MM()
        matched_players = mma_MIN_RISK_MM.run(players)
        # print(f"Matched pairs:{matched_players}")

        individual_satisfactions = find_satisfaction(matched_players, individual_satisfactions)

    avg_individual_satisfaction = find_avg_individual_satisfaction(individual_satisfactions)
    avg_individual_satisfaction = dict(sorted(avg_individual_satisfaction.items()))

    print(f"satisfaction MIN_RISK_MM:{avg_individual_satisfaction}")

    values = avg_individual_satisfaction.values()
    average = sum(values) / len(values)

    print("Average:", average)
    print(f"average player satisfaction: {average}")


simulate_1()
print("-----------------------------------")
simulate_2()
print("-----------------------------------")
simulate_3()
print("-----------------------------------")
simulate_4()
print("-----------------------------------")
