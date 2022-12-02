score_shape_player = {"Rock": 1, "Paper": 2, "Scissors": 3}
win_round = {("Scissors", "Rock"), ("Paper", "Scissors"), ("Rock", "Paper")}
must_lose_dict = {"Scissors": "Paper", "Paper": "Rock", "Rock": "Scissors"}
must_win_dict = {"Scissors": "Rock", "Paper": "Scissors", "Rock": "Paper"}

shape_map = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}


def calculate_outcome_round(shape_opponent, shape_player):
    if (shape_opponent, shape_player) in win_round:
        return 6
    elif shape_opponent == shape_player:
        return 3
    else:
        return 0


def score_single_round_known_outcome(shape_opponent, outcome):
    if outcome == "Y":  # draw
        return score_shape_player[shape_opponent] + 3
    elif outcome == "X":  # lose
        shape_player = must_lose_dict[shape_opponent]
        return score_shape_player[shape_player] + 0
    else:
        shape_player = must_win_dict[shape_opponent]
        return score_shape_player[shape_player] + 6


def score_rock_paper_scissors_game_known_outcome(input_file):
    total_score = 0
    with open(input_file) as file:
        for line in file:
            shape_opponent, expected_outcome = line.split()

            shape_opponent = shape_map[shape_opponent]
            total_score += score_single_round_known_outcome(
                shape_opponent, expected_outcome
            )
    return total_score


if __name__ == "__main__":
    print(score_rock_paper_scissors_game_known_outcome("input.txt"))
