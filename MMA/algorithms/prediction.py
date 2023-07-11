import random
import math


def predict_win_elo(pi, pj):
    rank_diff = pj.rank - pi.rank
    if rank_diff > 10000:
        rank_diff = 10000
    elif rank_diff < -10000:
        rank_diff = -10000
    # print(f'RANKOVICI {pi.rank} {pj.rank}')
    pi_win = 1 / (1 + math.pow(10, (rank_diff) / 400))
    pi_draw = 0
    pi_lose = 1 - pi_win - pi_draw
    return pi_win, pi_draw, pi_lose

def predict_individual_churn(p, next_outcome):
    outcome_seq = [p.penultimatеOutcome, p.lastOutcome, next_outcome]

    if outcome_seq == [1, 1, 1]:
        churn_risk = 0.37
    elif outcome_seq == [1, 1, -1]:
        churn_risk = 0.49
    elif outcome_seq == [1, -1, 1]:
        churn_risk = 0.46
    elif outcome_seq == [-1, 1, 1]:
        churn_risk = 0.43
    elif outcome_seq == [-1, 1, -1]:
        churn_risk = 0.37
    elif outcome_seq == [-1, -1, 1]:
        churn_risk = 0.27
    elif outcome_seq == [1, -1, -1]:
        churn_risk = 0.56
    elif outcome_seq == [-1, -1, -1]:
        churn_risk = 0.61
    else:
        churn_risk = 0.5
    return churn_risk

def predict_total_churn(pi, pj):
    pi_win, pi_draw, pi_lose = predict_win_elo(pi, pj)

    total_churn = pi_win * (predict_individual_churn(pi, next_outcome=1)
                            + predict_individual_churn(pj, next_outcome=-1)) \
                  + 0 \
                  + pi_lose * (predict_individual_churn(pi, next_outcome=-1)
                               + predict_individual_churn(pj, next_outcome=1))
    return total_churn


def calculate_streak(outcomes):
    return sum(outcomes)


def play_the_match(pair):
    player1, player2 = pair

    # Assign weights to each factor
    strength_weight = 0.4
    streak_weight = 0.3
    random_weight = 0.3

    player1_streak = calculate_streak([player1.penultimatеOutcome, player1.lastOutcome])
    player2_streak = calculate_streak([player2.penultimatеOutcome, player2.lastOutcome])

    player1_score = (strength_weight * player1.strength) + (streak_weight * player1_streak) + (
            random_weight * random.random())
    player2_score = (strength_weight * player2.strength) + (streak_weight * player2_streak) + (
            random_weight * random.random())

    if player1_score > player2_score:
        return player1
    elif player2_score > player1_score:
        return player2
    else:
        return "draw"
