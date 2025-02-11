"""
Make this a function:
Input values: num_for_loops, lines, filename
Output value: num_while_loops
(NB: "Output" doesn't mean "stuff we print")
"""
def read_file():
    """
    Read file and return filename and lines
    :return: filename, lines
    """
    filename = input("Enter program filename: ")

    with open(filename, 'r', encoding='utf-8') as f:  # Add encoding='utf-8'
        lines = f.readlines()
    return filename, lines

def count_label(lines, filename, label):
    """
    Count loops for a given label
    :param label:
    :param lines:
    :param filename:
    :return:
    """
    num_loops = 0

    for line in lines:
        if line.strip().startswith(label):
            num_loops += 1

    print(f"Program {filename} contain {num_loops} {label} loops")
    return num_loops

def main():
    """
    Main function. Read file. Count required attributes
    :return:
    """

    filename, lines = read_file()

    count_label(lines, filename, "for")
    count_label(lines, filename, "while")
    count_label(lines, filename, "if")


if __name__ == "__main__":
    main()
