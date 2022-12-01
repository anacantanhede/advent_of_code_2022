import day01_01
import day01_02


def test_max_calories_a_elf_is_carrying():
    assert day01_01.max_calories_a_elf_is_carrying("example_input.txt") == 24000


def test_sum_calories_top_three_elfs():
    assert day01_02.sum_calories_top_three_elfs("example_input.txt") == 45000
