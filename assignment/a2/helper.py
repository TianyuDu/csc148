"""
Collection of helper functions.
"""
from typing import List, Dict


def create_keys(g: List[List[str]]) -> Dict[str, tuple]:
    """
    This helper function creates a dictionary maps from
    a capital letter to a tuple of size two representing the index of
    this letter in original graph.
    """
    k = dict()
    for i in range(len(g)):
        for j in range(len(g[i])):
            k[g[i][j]] = (i, j)
    return k


def create_graph(n=3) -> List[List[str]]:
    """
    Total @ : (n + 1) * 3
    Sequence: [Horizontal, left to right, right to left]
    This creates a graph of side-length n.
    """
    source = [chr(i) for i in range(65, 91)]  # Letter from A to Z.
    assert 1 <= n <= 5
    current_len = 2
    current_letter = 0
    graph = []
    while current_len <= n + 1:
        graph.append([
            source[i] for i in range(
                current_letter, current_letter + current_len
            )
        ])
        current_letter += current_len
        current_len += 1
    graph.append([
        source[i] for i in range(current_letter, current_letter + n)
    ])
    return graph


def illustrate_graph(graph: List[List[str]], lls: List[List[str]]) -> str:
    """
    The helper function to return a string illustrating the layout
    of the board given graph and ley line states.
    """
    side_length = len(graph) - 1
    central_line_position = side_length - 1
    present_list = []
    # Construct row 1:
    present = " " * (4 + 2 * side_length)
    lls_info = "   ".join(lls[2][:2])
    present += lls_info
    present_list.append(present)

    # Construct row 2:
    present = " " * (4 + 2 * side_length - 1)
    present += "   ".join(["/"]*2)
    present_list.append(present)

    # Internal rows
    for i in range(len(graph)):
        present = " - ".join(
            list(lls[0][i]) + graph[i]
        )
        present = " " * (2 * abs(central_line_position - i)) + present
        link = " ".join(["/ \\"] * len(graph[i]))
        link = " " * (2 * abs(central_line_position - i) + 3) + link
        try:
            present += (
                " " * 3 + lls[2][i+2]
            )
            link += " /"
        except IndexError:
            pass
        present_list.append(present)
        present_list.append(link)
    # Take care last row

    present_list[-1] = present_list[-1].replace("/", " ")
    present_list[-2] += (" " * 3 + lls[1][-1])
    last_row = " " * 8 + (" " * 3).join(lls[1][:-1])
    present_list.append(last_row)

    present_list[-4] = present_list[-4].replace("/", " ", 1)

    illustration = "\n".join(present_list)
    illustration = "\n" + illustration
    return illustration


def get_ley_line_id(lls: List[List[str]],
                    ley_line_direction: int) -> List[List[str]]:
    """
    Return the keys
    """
    assert ley_line_direction in [0, 1, 2]
    size = len(lls[1])  # Total number ley line in follow this direction.
    graph_size = size - 1
    sample_graph = create_graph(n=graph_size)
    if ley_line_direction == 0:
        # Horizontal case.
        return sample_graph[:]
    elif ley_line_direction == 1:
        # Left-top to right-bottom case.
        result_list = []
        for i in range(1, size+1):
            node_list = []
            for row in sample_graph[:-1]:  # Exclude the last row
                try:
                    node_list.append(row[-i])
                except IndexError:
                    pass
            result_list.append(node_list)
        result_list.reverse()
        last_row = sample_graph[-1]
        for i in range(len(result_list) - 1):
            result_list[i].append(last_row[i])
        return result_list
    elif ley_line_direction == 2:
        result_list = []
        for i in range(size):
            node_list = []
            for row in sample_graph[:-1]:
                try:
                    node_list.append(row[i])
                except IndexError:
                    pass
            result_list.append(node_list)
        last_row = sample_graph[-1]
        for i in range(len(last_row)):
            result_list[i + 1].append(last_row[i])
        return result_list
