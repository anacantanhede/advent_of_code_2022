import day05_01
import day05_02


def test_split_line_by_position():
    assert day05_01.split_line_by_position("[Z] [M] [P]") == ["Z", "M", "P"]
    assert day05_01.split_line_by_position("    [D]    ") == ["", "D", ""]


def test_reading_starting_stacks():
    assert day05_01.read_starting_stacks("example_input.txt") == {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"],
    }


def test_move_elems():
    assert day05_01.move_elems(
        "move 1 from 2 to 1",
        {
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"],
        },
    ) == {
        1: ["Z", "N", "D"],
        2: ["M", "C"],
        3: ["P"],
    }
    assert day05_01.move_elems(
        "move 3 from 2 to 1",
        {
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"],
        },
    ) == {
        1: ["Z", "N", "D", "C", "M"],
        2: [],
        3: ["P"],
    }


def test_move_multiple_elems():
    assert day05_02.move_multiple_elems(
        "move 1 from 2 to 1",
        {
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"],
        },
    ) == {
        1: ["Z", "N", "D"],
        2: ["M", "C"],
        3: ["P"],
    }
    assert day05_02.move_multiple_elems(
        "move 3 from 2 to 1",
        {
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"],
        },
    ) == {
        1: ["Z", "N", "M", "C", "D"],
        2: [],
        3: ["P"],
    }


def test_rearrangement_procedure():
    assert day05_01.rearrangement_procedure("example_input.txt") == "CMZ"
    assert day05_02.rearrangement_procedure("example_input.txt") == "MCD"
