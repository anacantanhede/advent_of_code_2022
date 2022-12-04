import day04_01
import day04_02


# the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8)
def test_calculate_assigned_sections():
    assert day04_01.calculate_assigned_sections("2-4") == [2, 3, 4]
    assert day04_01.calculate_assigned_sections("6-7") == [6, 7]
    assert day04_01.calculate_assigned_sections("6-6") == [6]


# 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6
def test_is_section_contained_in_other():
    assert day04_01.is_section_contained_in_other("2-8", "3-7") is True
    assert day04_01.is_section_contained_in_other("6-6", "4-6") is True
    assert day04_01.is_section_contained_in_other("6-8", "4-6") is False


# In this example, there are 2 such pairs.
def test_count_section_contained_in_other():
    assert day04_01.count_section_contained_in_other("example_input.txt") == 2


# the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap
def test_is_overlapping():
    assert day04_02.is_overlapping("2-4", "6-8") is False
    assert day04_02.is_overlapping("2-8", "3-7") is True

    # in this example, the number of overlapping assignment pairs is 4.


def test_count_section_overlaps_other():
    assert day04_02.count_section_overlaps_other("example_input.txt") == 4
