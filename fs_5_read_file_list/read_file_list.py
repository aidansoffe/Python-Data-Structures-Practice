def read_file_list(filename):
    with open(filename) as f:
        for line in f:
            # remove newline at end of line!
            line = line.strip()
            print(f"- {line}")