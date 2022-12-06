def split_line_by_position(line):
    list_line = list()
    split_indexes = range(0, len(line) + 1, 4)
    for i in split_indexes:
        new_char = str(line[i : i + 4]).strip().replace("[", "").replace("]", "")
        list_line.append(new_char)
    return list_line


def read_starting_stacks(input_file):
    temp_stack = list()
    with open(input_file) as file:
        for line in file:
            if line[0] != "\n":
                temp_stack.append(list(split_line_by_position(line.rstrip())))
            else:
                break
    stack = dict()
    for i in temp_stack[-1]:
        stack[int(i)] = list()
    for row in temp_stack[0 : len(temp_stack) - 1]:
        for pile_index, elem in enumerate(row):
            if elem != "":
                stack[pile_index + 1].append(elem)
    for key, _ in stack.items():
        stack[key].reverse()
    return stack


def move_multiple_elems(instruction, stack):
    parse_instruction = list(instruction.split())
    num_moves = int(parse_instruction[1])
    from_stack = int(parse_instruction[3])
    to_stack = int(parse_instruction[5])
    elems_to_move = []
    for _ in range(num_moves):
        elems_to_move.append(str(stack[from_stack].pop(-1)))
    elems_to_move.reverse()
    stack[to_stack].extend(elems_to_move)
    return stack


def rearrangement_procedure(input_file):
    stack = read_starting_stacks(input_file)
    with open(input_file) as file:
        for line in file:
            if line[0] == "m":
                stack = move_multiple_elems(line, stack)
    # print(stack)
    top_elems = ""
    for i in stack.keys():
        top_elems += top_elems.join(stack[i][-1])

    return top_elems


if __name__ == "__main__":
    print(rearrangement_procedure("input.txt"))
