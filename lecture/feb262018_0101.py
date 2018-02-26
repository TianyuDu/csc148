"""
Feb 26 2018 10.00 am
Lecture 0101
"""

class Tree:
    
    value: float
    
    def __init__(self):
        self.children = []
    
    def __str__(self) -> str:
        pass
    
    def count_nodes(self) -> int:
        # if self.children == []:  # BASE CASE
        #     return 1
        # else:
        #     return 1 + sum([
        #         child.count_nodes()
        #         for child in self.children
        #         ])
        return 1 + sum([c.count_nodes] for c in self.children)
    
    def is_leaf(self) -> bool:
        return self.children == []
    
    def height(self) -> int:
        return 1 + max([
            c.height() for c in self.children
            ] + [0]
            )
            

def path_to_tree(path_name: str) -> Tree:
    return Tree((
        path_name, [f.name for f in scandir(path_name)]
        ),
        for f in scandir(path_name)
        if f.is_dir()
        )