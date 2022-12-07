def read_in_chunks(filename, chunk_size=1):
    with open(filename, 'r') as file_object:
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data


def tuner(generator, length_of_marker=4):
    buf = []

    for i,ch in enumerate(generator):
        buf.append(ch)
        if i == length_of_marker - 1:
            break
    marker = length_of_marker
    while(len(set(buf)) < len(buf)):
        del buf[0]
        buf.append(next(generator))
        marker += 1

    return marker
        


if __name__ == '__main__':
    start_of_pakcket = tuner(read_in_chunks('input.txt'))
    print(f"Puzzle 1: {start_of_pakcket}")
    start_of_message = tuner(read_in_chunks('input.txt'), 14)
    print(f"Puzzle 2: {start_of_message}")