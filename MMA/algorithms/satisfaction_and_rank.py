def calculate_satisfaction(is_winner, player_rank, opponent_rank, max_rank_diff):
    max_satisfaction = 1000

    rank_diff = player_rank - opponent_rank
    difficulty = rank_diff / max_rank_diff

    if is_winner:
        if difficulty < 0:
            satisfaction = (max_satisfaction / 2) * (1 + abs(difficulty))
        else:
            satisfaction = (max_satisfaction / 2) * (1 - abs(difficulty))
    else:
        if difficulty > 0:
            satisfaction = (max_satisfaction / 2) * (1 - abs(difficulty))
        else:
            satisfaction = (max_satisfaction / 2) * (1 + abs(difficulty))

    return satisfaction


def normalize_value(original_value, min_value, max_value):
    normalized_value = (2 * (original_value - min_value) / (max_value - min_value)) - 1
    return normalized_value


def rescale_waiting_time(waiting_time, min_waiting_time, max_waiting_time):
    rescaled_waiting_time = ((waiting_time - min_waiting_time) / (max_waiting_time - min_waiting_time)) * 250
    return rescaled_waiting_time

