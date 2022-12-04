import day03_01
import day03_02

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def test_item_priority():
    assert day03_01.item_priority("a") == 1
    assert day03_01.item_priority("z") == 26
    assert day03_01.item_priority("A") == 27
    assert day03_01.item_priority("Z") == 52


# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp.
def test_split_compartment():
    first, second = day03_01.split_compartment("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert first == "vJrwpWtwJgWr"
    assert second == "hcsFMMfFFhFp"


# The only item type that appears in both compartments is lowercase p.
def test_find_common_item():
    assert day03_01.find_common_item("vJrwpWtwJgWr", "hcsFMMfFFhFp") == "p"


# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
def test_rucksack_priorities():
    assert day03_01.elves_rucksack_priorities("example_input.txt") == 157


## Part Two

# The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.
# In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges
def test_badge_item():
    assert (
        day03_02.find_badge_item(
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        )
        == "r"
    )


# Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.
def test_priorities_badges():
    assert day03_02.elves_priorities_badges("example_input.txt") == 70
