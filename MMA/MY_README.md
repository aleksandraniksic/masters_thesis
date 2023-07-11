classes:
Player
- fields: username, rank, latest_win_seq, wins, loses, draws, games_played, satifaction
PlayersGraph(nx.Graph)
- add_nodes_and_compute_edge_weights
- add_players
- compute_edge_weights
Game
- load_players
- get_matches
- evaluate
- run
methods:
- predict_win_elo
- predict_individual_churn
- predict_total_churn
- calculate_satisfaction
- normalize_value
- rescale_waiting_time
- update_player_data


python3 manage.py runserver
python3 manage.py createsuperuser
python3 manage.py makemigrations
python3 manage.py migrate

