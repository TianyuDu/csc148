from typing import Union, List

def depth(list_):
    """
    DocStringExample
    >>> depth([])
    1
    >>> depth(17)
    0
    >>> depth([3, 17, 1])
    1
    >>> depth([5, [3, 17, 1], [2, 4], 6])
    2
    >>> depth([14, 7, [5, [3, 17, 1], [2, 4], 6], 9])
    3
    """
    if list_ == []:  # Base case 1
        return 1  # To avoid ValueError from max([]).
    elif not isinstance(list_, list):  # Base case 2
        return 0
    else:  # General case
        return 1 + max([depth(x) for x in list_])
        
        
def flatten(list_: list) -> list:
    """
    DocStringExample
    >>> flatten([1, [2, [3, 4]]])
    [1, 2, 3, 4]
    """
    return sum([flatten(i) if isinstance(i, list) else [i] for i in list_], [])


def rec_max(obj):
    
    if isinstance(obj, list):
        return max([rec_max(x) for x in obj])
    else:
        return obj
        

def concat_strings(string_list: Union[List[str], str]) -> str:
    
    if not isinstance(string_list, list):
        return string_list
    else:
        return "".join([concat_strings(x) for x in string_list])
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()