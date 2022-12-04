def item_priority(item):
    if item.islower():
        return ord(item) - ord("a") + 1
    elif item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return None


def find_badge_item(rucksack_1, rucksack_2, rucksack_3):
    return "".join(set(rucksack_1) & set(rucksack_2) & set(rucksack_3))


def elves_priorities_badges(input_file):
    sum_priorities = 0
    elem = [""] * 3
    with open(input_file) as file:
        for index, line in enumerate(file):
            if index != 0 and index % 3 == 0:
                common_item = find_badge_item(elem[0], elem[1], elem[2])
                priority = item_priority(common_item)
                sum_priorities += priority
                elem[0] = line.strip()
            else:
                elem[index % 3] = line.strip()
    common_item = find_badge_item(elem[0], elem[1], elem[2])
    priority = item_priority(common_item)
    sum_priorities += priority
    return sum_priorities


if __name__ == "__main__":
    print(elves_priorities_badges("input.txt"))
