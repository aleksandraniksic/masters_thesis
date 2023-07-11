import csv
import random

import networkx as nx

from algorithms.prediction import predict_total_churn, play_the_match
from algorithms.satisfaction_and_rank import calculate_satisfaction


# MAX_RANK = 1
# MIN_RANK = 750


def create_players_from_csv(file_path, players_num):
    players = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)  # Skip the header
        count_players = 0
        for row in reader:
            if count_players >= players_num:
                break
            username = row['username']
            strength = int(row['strength'])
            rank = float(row['rank'])
            wins = int(row['wins'])
            losses = int(row['losses'])
            draws = int(row['draws'])
            penultimatеOutcome = int(row['penultimatеOutcome'])
            lastOutcome = int(row['lastOutcome'])

            player = Player(username, strength, rank, wins, losses, draws, penultimatеOutcome, lastOutcome)
            players.append(player)
            count_players += 1
    return players


class Player:
    def __init__(self, username, strength, rank, wins, losses, draws, penultimatеOutcome, lastOutcome):
        self.username = username
        self.strength = strength
        self.rank = rank
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.penultimatеOutcome = penultimatеOutcome
        self.lastOutcome = lastOutcome


class PlayersGraph(nx.Graph):
    def __init__(self):
        super().__init__()

    def add_nodes_and_compute_edge_weights(self, players):
        self.add_players(players)
        self.compute_edge_weights(players)
        return self

    def add_players(self, players):
        for p in players:
            self.add_node(p)

    # _compute_edge_weights prodje kroz listu igraca i racuna tezinu grane izmedju svaka dva igraca baziranu na riziku od odliva
    def compute_edge_weights(self, players):
        for i in range(len(players)):
            pi = players[i]
            for j in range(i + 1, len(players)):
                pj = players[j]
                churn_risk = predict_total_churn(pi, pj)
                self.add_edge(pi, pj, churn_weight=churn_risk,
                              retain_weight=2 - churn_risk)

class Game():
    def __init__(self, players_num):
        self.players = None
        self.players_graph = None
        self.players_num = players_num
        self.load_players(players_num)

    def load_players(self, players_num):
        self.players = create_players_from_csv("../data/player_info.csv", players_num)
        self.players_graph = PlayersGraph().add_nodes_and_compute_edge_weights(self.players)

    def run(self, matchmaker):

        if matchmaker in ['MIN_RISK_MM', 'MAX_RISK_MM']:
            list_of_paired_players = matchmaker.run(self.players_graph)
        else:
            list_of_paired_players = matchmaker.run(self.players)
        retain_players_num = 0

        retain_edges = nx.get_edge_attributes(self.players_graph, 'retain_weight')
        for pair in list_of_paired_players:
            # print(pair[0].username, pair[1].username)
            if pair not in retain_edges.keys():
                pair = (pair[1], pair[0])
            retain_players_num += retain_edges[pair]

        players = update_player_data(list_of_paired_players)
        players_graph = PlayersGraph().add_nodes_and_compute_edge_weights(players)

        self.players = players
        self.players_graph = players_graph

        # total_satisfaction = 0
        # for player in players:
        #     total_satisfaction += player.satisfaction

        return retain_players_num  # , total_satisfaction/self.players_num


def update_player_data(list_of_paired_players):
    updated_list_of_players = []
    for pair in list_of_paired_players:
        winner = play_the_match(pair)

        if winner == "draw":
            pair[0].draws += 1
            pair[1].draws += 1

            pair[0].penultimatеOutcome = pair[0].lastOutcome
            pair[0].lastOutcome = 0

            pair[1].penultimatеOutcome = pair[1].lastOutcome
            pair[1].lastOutcome = 0

            updated_list_of_players.append(pair[0])
            updated_list_of_players.append(pair[1])

            continue

        if winner == pair[0]:
            loser = pair[1]
        else:
            loser = pair[0]

        rank_diff = winner.rank - loser.rank

        if rank_diff > 0:
            # Won against a lower ranked opponent
            rank_gain = 0.125 * rank_diff
        elif rank_diff < 0:
            # Won against a higher ranked opponent
            rank_gain = 0.25 * abs(rank_diff)
        else:
            rank_gain = random.uniform(0, 0.1)

        # print(f'rank gain: {rank_gain}')

        # After all, increase rank of the winner and decrease the loser rank
        winner.rank += rank_gain
        winner.penultimatеOutcome = winner.lastOutcome
        winner.lastOutcome = 1
        winner.wins += 1

        loser.rank -= rank_gain
        loser.penultimatеOutcome = loser.lastOutcome
        loser.lastOutcome = -1
        loser.losses += 1

        updated_list_of_players.append(winner)
        updated_list_of_players.append(loser)

    return updated_list_of_players
