def max_calories_a_elf_is_carrying(input_file):
    max_calories = -1
    with open(input_file) as file:
        calories = 0
        for line in file:
            if line != "\n":
                calories += int(line)
            else:
                if calories > max_calories:
                    max_calories = calories
                calories = 0
    # last set is not being picked up because the last line is not read
    if calories > max_calories:
        max_calories = calories
    return max_calories


if __name__ == "__main__":
    print(max_calories_a_elf_is_carrying("input.txt"))
