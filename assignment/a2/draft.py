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

size = 5

ley_line_state = [
    ("@ " * (size + 1)).split()
    for i in range(3)
]

""" ley_line_state = [
    ["a", "d", "o", "r", "e", "!"],
    ["c", "s", "c", "1", "4", "8"],
    ["@", "@", "@", "@", "@", "@"]
]"""

g = create_graph(n=size)


# def illustrate_graph(g: list, lls: list) -> str:
present_list = []
for i in range(len(g)):
    hline = g[i]
    present = str()
    link = str()
    for j in range(len(hline)):
        node = hline[j]
        present += str(node)
        if i != len(g) - 1:
            link += "/ \\"
        if j != len(hline) - 1:
            present += " - "
            link += " "
    present = str(ley_line_state[0][i]) + " - " + present
    if i != len(g) - 1:
        present = "  "*(len(g) - i) + present
        link = "  "*(len(g) - i) + link
    else:
        present = " "*6 + present
        link = " "*5 + link
    link = link[1:]
    link = "    " + link
    if i <= size - 2:
        present += "   {}".format(ley_line_state[2][i + 2])
        link += " /"
    present_list.append(present)
    present_list.append(link)
    # present_list.append(ley_line_state[2][i])
present_list[-2] += "   {}".format(str(ley_line_state[1][-1]))
present_list[-3] = present_list[-3].lstrip(" /")
present_list[-3] = "         " + present_list[-3]

present_list.insert(0, "                 /   /")
present_list.insert(0, "                  {}   {}".format(
    ley_line_state[2][0],
    ley_line_state[2][1]
))

#  present_list[-3] = present_list[-3].rstrip("\\")

connect_row = [" \\ " for i in range(size + 1)]
connect_line = "".join(connect_row)
connect_line = "           " + connect_line
present_list[-1] = connect_line

last_row = [str(item) for item in ley_line_state[1][:-1]]
last_line = " - ".join(last_row)
last_line = "             " + last_line
present_list.append(last_line)


illustrate = "\n".join(present_list)
print(illustrate)


    # return illustrate
