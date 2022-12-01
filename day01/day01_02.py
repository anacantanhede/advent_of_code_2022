def update_top_three_elfs(new_elf, top_three_list):
    min_calories = min(top_three_list)
    if new_elf > min_calories:
        index_min = top_three_list.index(min_calories)
        top_three_list[index_min] = new_elf
    return top_three_list


def sum_calories_top_three_elfs(input_file):
    top_three_calories = [0, 0, 0]
    with open(input_file) as file:
        calories = 0
        for line in file:
            if line != "\n":
                calories += int(line)
            else:
                top_three_calories = update_top_three_elfs(calories, top_three_calories)
                calories = 0
    # last set is not being picked up because the last line is not read
    top_three_calories = update_top_three_elfs(calories, top_three_calories)
    sum_top_three_calories = sum(top_three_calories)
    return sum_top_three_calories


if __name__ == "__main__":
    print(sum_calories_top_three_elfs("input.txt"))
