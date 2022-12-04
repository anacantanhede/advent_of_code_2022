def item_priority(item):
    if item.islower():
        return ord(item) - ord("a") + 1
    elif item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return None


def split_compartment(all_items):
    first_compartment = all_items[: int(len(all_items) / 2)]
    second_compartment = all_items[int(len(all_items) / 2) :]
    return first_compartment, second_compartment


def find_common_item(first_compartment, second_compartment):
    return "".join(set(first_compartment) & set(second_compartment))


def elves_rucksack_priorities(input_file):
    sum_priorities = 0
    with open(input_file) as file:
        for line in file:
            first_compartment, second_compartment = split_compartment(line)
            common_item = find_common_item(first_compartment, second_compartment)
            priority = item_priority(common_item)
            sum_priorities += priority
    return sum_priorities


if __name__ == "__main__":
    print(elves_rucksack_priorities("input.txt"))
