def index_first_n_different_characters(input, n):
    max_pos = len(input)
    for i in range(n, max_pos):
        if len(set(input[i - n : i])) == n:
            return i
    return None


def process_datastream_buffer(input_file):
    with open(input_file) as file:
        for line in file:
            return index_first_n_different_characters(line.strip(), 14)


if __name__ == "__main__":
    print(process_datastream_buffer("input.txt"))
