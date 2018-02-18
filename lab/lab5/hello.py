def max_depth(obj):
    if not isinstance(obj, list):
        return 0  # No list found.
    elif obj == []:
        return 1  # Single list
    else:
        return 1 + max([max_depth(x) for x in obj])
        

def concat_strings(string_list):
    """
    Doc string
    """
    
    if isinstance(string_list, list):
        return "".join([concat_strings(x) for x in string_list])
    else:
        return string_list