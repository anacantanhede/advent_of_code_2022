def calculate_assigned_sections(sections):
    start, end = sections.split("-")
    return list(range(int(start), int(end) + 1))


def is_section_contained_in_other(section1, section2):
    assigned_section_1 = set(calculate_assigned_sections(section1))
    assigned_section_2 = set(calculate_assigned_sections(section2))
    if assigned_section_1.issubset(assigned_section_2) or assigned_section_2.issubset(
        assigned_section_1
    ):
        return True
    return False


def count_section_contained_in_other(input_file):
    sum_contained = 0
    with open(input_file) as file:
        for line in file:
            first_section, second_section = line.strip().split(",")
            if is_section_contained_in_other(first_section, second_section):
                sum_contained += 1

    return sum_contained


if __name__ == "__main__":
    print(count_section_contained_in_other("input.txt"))
