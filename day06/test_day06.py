import day06_01
import day06_02

# mjqjpqmgbljsphdztnvjfqwrcgsmlb - your subroutine should report the value 7
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
#     nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
#     nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
#    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
def test_index_first_four_different_characters():
    assert (
        day06_01.index_first_four_different_characters("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
        == 7
    )
    assert (
        day06_01.index_first_four_different_characters("bvwbjplbgvbhsrlpgdmjqwftvncz")
        == 5
    )
    assert (
        day06_01.index_first_four_different_characters("nppdvjthqldpwncqszvftbrmjlhg")
        == 6
    )
    assert (
        day06_01.index_first_four_different_characters(
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        )
        == 10
    )
    assert (
        day06_01.index_first_four_different_characters(
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        )
        == 11
    )


"""
    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
"""


def test_index_first_n_different_characters():
    assert (
        day06_02.index_first_n_different_characters(
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14
        )
        == 19
    )
    assert (
        day06_02.index_first_n_different_characters("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)
        == 23
    )
    assert (
        day06_02.index_first_n_different_characters("nppdvjthqldpwncqszvftbrmjlhg", 14)
        == 23
    )
    assert (
        day06_02.index_first_n_different_characters(
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14
        )
        == 29
    )
    assert (
        day06_02.index_first_n_different_characters(
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14
        )
        == 26
    )
