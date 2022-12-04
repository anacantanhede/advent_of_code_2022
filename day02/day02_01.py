score_shape_player = {"Rock": 1, "Paper": 2, "Scissors": 3}
win_round = {("Scissors", "Rock"), ("Paper", "Scissors"), ("Rock", "Paper")}

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


def score_single_round(shape_opponent, shape_player):
    score = score_shape_player[shape_player] + calculate_outcome_round(
        shape_opponent, shape_player
    )
    return score


def score_rock_paper_scissors_game(input_file):
    total_score = 0
    with open(input_file) as file:
        for line in file:
            shape_opponent, shape_player = line.split()

            shape_opponent = shape_map[shape_opponent]
            shape_player = shape_map[shape_player]
            total_score += score_single_round(shape_opponent, shape_player)
    return total_score


if __name__ == "__main__":
    print(score_rock_paper_scissors_game("input.txt"))
