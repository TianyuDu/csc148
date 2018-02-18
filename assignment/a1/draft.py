def random_strategy(z) -> str:
    possible_moves =  z# List
    choice_idx = random.randrange(len(possible_moves))
    return possible_moves[choice_idx]
