import day02_01
import day02_02


def test_win_using_paper():
    assert day02_01.score_single_round("Rock", "Paper") == 8


def test_score_rock_paper_scissors_game():
    assert day02_01.score_rock_paper_scissors_game("example_input.txt") == 15


def test_must_lose():
    assert day02_02.score_single_round_known_outcome("Paper", "X") == 1


def test_score_rock_paper_scissors_game_known_outcome():
    assert (
        day02_02.score_rock_paper_scissors_game_known_outcome("example_input.txt") == 12
    )
