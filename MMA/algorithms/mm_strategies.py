from random import shuffle

from networkx.algorithms.matching import max_weight_matching

from algorithms.components import PlayersGraph


class FIFO_MM:
    def __repr__(self):
        return "FIFO_MM"
    def run(self, players):
        num_of_players = int(len(players))
        list_of_paired_players = []
        # for p in players:
        #     print(f"{p.username} {p.rank}")
        # TODO players = list(shuffle(players))
        for i in range(0, num_of_players-1, 2):
            pair = (players[i], players[i+1])
            list_of_paired_players.append(pair)
        return list_of_paired_players


class SKILL_BASED_MM:
    def __repr__(self):
        return "SKILL_BASED_MM"
    def run(self, players):
        pair_num = int(len(players) / 2)
        list_of_paired_players = []
        players_sort = sorted(players, key=lambda p: p.rank)
        # for p in players_sort:
        #     print(f"{p.username} {p.rank}")
        for i in range(pair_num):
            pair = (players_sort.pop(), players_sort.pop())
            list_of_paired_players.append(pair)
        return list_of_paired_players

class WINNING_RATIO_BASED_MM:
    def __repr__(self):
        return "WINNING_RATIO_BASED_MM"
    def run(self, players):
        pair_num = int(len(players) / 2)
        list_of_paired_players = []
        players_sort = sorted(players, key=lambda p: p.wins / (p.wins+p.losses+p.draws), reverse=True)
        # for p in players_sort:
        #     print(f"{p.username} {p.rank}")
        #     print(f'igrac {p.username}, {p.wins}, {p.losses}, {p.draws}')

        for i in range(pair_num):
            pair = (players_sort.pop(), players_sort.pop())
            list_of_paired_players.append(pair)
        return list_of_paired_players


class MAX_RISK_MM:
    def __repr__(self):
        return "MAX_RISK_MM"
    def run(self, players):
        if not isinstance(players, PlayersGraph):
            players = PlayersGraph().add_nodes_and_compute_edge_weights(players)
            # for p in players:
                # print(f"{p.username} {p.rank}")
        return max_weight_matching(players, maxcardinality=True, weight="churn_weight")


class MIN_RISK_MM:
    def __repr__(self):
        return "MIN_RISK_MM"
    def run(self, players):
        if not isinstance(players, PlayersGraph):
            players = PlayersGraph().add_nodes_and_compute_edge_weights(players)
            # for p in players:
                # print(f"{p.username} {p.rank}")
        return max_weight_matching(players, maxcardinality=True,
                                   weight="retain_weight")  # ovde se korsiti atribut retain_weight = 2-churn_risk
