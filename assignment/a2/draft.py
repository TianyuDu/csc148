"""
...
"""
def create_graph(n=3):
    """
    Total @ : (n + 1) * 3
    Sequence: [Horizontal, left to right, right to left]
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

def create_keys(g):
    k = dict()
    for i in range(len(g)):
        for j in range(len(g[i])):
            k[g[i][j]] = (i, j)
    return k

zz = 3

l = [
    ("@ " * (zz + 1)).split()
    for i in range(3)
]

g = create_graph(n=zz)


def illustrate_graph(g: list, lls: list) -> str:
    present_list, side_length = [], len(g[-1])
    # containing string representing each row.
    # get the side length from from graph.
    for i in range(side_length + 1):
        hline = g[i]
        link = str()
        present = " - ".join(
            sum(
                [[str(lls[0][i])], hline], []
            )
        )
        link = ["/ \\" for _ in range(len(hline))]
        link = " ".join(link)
        link = "    " + link
        present_list.append(present)
        present_list.append(link)

    lls_2_link = "  ".join(["\\" for _ in range(side_length - 1)])
    for i in range(len(present_list)):
        present_list[i] = " " * abs(2 * side_length - 2 - i) + present_list[i]
    illustrate = "\n".join(present_list)

    return illustrate


print(illustrate_graph(g, l))
