from algorithms.components import Game
from algorithms.mm_strategies import FIFO_MM, SKILL_BASED_MM, MAX_RISK_MM, MIN_RISK_MM, WINNING_RATIO_BASED_MM

matchmakers = [FIFO_MM(), SKILL_BASED_MM(), WINNING_RATIO_BASED_MM(), MAX_RISK_MM(), MIN_RISK_MM()]
games_to_play = 500
players_nums = [50, 100, 150, 200, 250, 300]

file = open("results.txt", "w")

for players_num in players_nums:
    print(f'Number of players in game: {players_num}')

    player_retention_rate = [0] * len(matchmakers)
    # player_satisfaction_rate = [0] * len(matchmakers)
    for m, matchmaker in enumerate(matchmakers):
        game = Game(players_num)
        for games_played in range(games_to_play):
            retain_players_num = game.run(matchmaker)

            player_retention_rate[m] = (player_retention_rate[m] * games_played + retain_players_num) / (games_played + 1)
            # player_satisfaction_rate[m] = player_satisfaction_rate[m] + total_satisfaction

            data = f'MMA: {matchmaker} - GAMES PLAYED {games_played} - RETAINED PLAYERS NUM: {retain_players_num}'
            print(data)
            file.write(data)
            file.write('\n')

        file.write('===============================================================================\n')

        print('===============================================================================')


        # print(f"Average satisfaction for {players_num} players in {games_to_play} games: {player_satisfaction_rate}")

file.close()
