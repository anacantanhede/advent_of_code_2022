def index_first_four_different_characters(input):
    max_pos = len(input)
    for i in range(4, max_pos):
        if len(set(input[i - 4 : i])) == 4:
            return i
    return None


def process_datastream_buffer(input_file):
    with open(input_file) as file:
        for line in file:
            return index_first_four_different_characters(line.strip())


if __name__ == "__main__":
    print(process_datastream_buffer("input.txt"))
