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

def count_for_loops(lines, filename):
    """
    Count for loops
    :param lines:
    :param filename:
    :return:
    """
    num_for_loops = 0

    for line in lines:
        if line.strip().startswith("for"):
            num_for_loops += 1

    print(f"Program {filename} contain {num_for_loops} for loops")
    return num_for_loops


def count_while_loops(lines, filename):
    """
    Count while loops
    :param lines:
    :param filename:
    :return:
    """
    num_while_loops = 0
    for line in lines:
        if line.strip().startswith("while"):
            num_while_loops += 1

    print(f"Program {filename} contain {num_while_loops} while loops")
    return num_while_loops

def count_if_loops(lines, filename):
    """
    Count if loops
    :param lines:
    :param filename:
    :return:
    """

    num_if_loops = 0
    for line in lines:
        if line.strip().startswith("if"):
            num_if_loops += 1

    print(f"Program {filename} contain {num_if_loops} if loops")
    return num_if_loops


def main():
    """
    Main function. Read file. Count required attributes
    :return:
    """

    filename, lines = read_file()

    count_for_loops(lines, filename)
    count_while_loops(lines, filename)
    count_if_loops(lines, filename)


if __name__ == "__main__":
    main()
