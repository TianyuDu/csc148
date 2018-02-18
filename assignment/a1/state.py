"""
revision 3
This file contains class types of State and its subclasses.
"""
from typing import List, Dict, Any


class State:
    """
    This base class for state object for game class.

    current_player: a string taken from "p1" and "p2" that representing
    the current acting player.
    """
    current_player: str

    def __init__(self) -> None:
        """
        This initializing method for State type object, and this method
        should not be called from this super class.
        """
        raise NotImplementedError("Subclass needed!")

    def __eq__(self, other: Any) -> bool:
        """
        This method returns True if and only if self and other has the
        same time and have the same current player.
        """
        return (type(self) == type(other)
                and self.current_player == self.current_player)

    def __str__(self) -> str:
        """
        This method returns a string representing the curretn state of
        this state object.
        This object should not be called directly fom this superclass.
        """
        raise NotImplementedError("Subclass neeeded!")

    def get_possible_moves(self) -> list:
        """
        This method returns a list containing possible move based
        on game time. This method should not be called from this
        superclass.
        """
        raise NotImplementedError("Subclass needed!")

    def is_valid_move(self, move: str) -> bool:
        """
        This method takes a str representing move to test and return
        True if and only if this move is in the current possible
        move set. This method should not be called from this
        superclass.
        """
        raise NotImplementedError("Subclass needed!")

    def get_current_player_name(self) -> str:
        """
        This method returns the current player name as a string.
        This method should not be called from this
        superclass.
        """
        raise NotImplementedError("Subclass needed!")

    def make_move(self, move_to_make: str) -> "State":
        """
        This method takes in move_to_make as a string and will return a
        new state object that the modified version (modified with the
        passed-in move_to_make) of the pervious state.
        This method should not be called from this
        superclass.
        """
        raise NotImplementedError("Subclass needed!")

    def get_next_player(self) -> str:
        """
        This method returns the next player, if the current player is
        player 1 then it returns "p2", else, it returns "p1".
        This method should not be called from this
        superclass.
        No example will be provided since the initializing method of this
        superclass will raise a NotImplementError.
        """
        if self.current_player == "p1":
            ret = "p2"
        else:
            ret = "p1"
        return ret


class ChopSticksState(State):
    """
    This is a subclass of State, and contains game state
    information of ChopStick games.

    hands: Dict[str, int]: represent the fingers on each hands of
    each players. The dict takes "p1_l", "p1_r", "p2_l" and "p2_r"
    as keys and return an integer representing the number of
    fingers on that hand, 0 finger means this hand is dead.
    """
    hands: Dict[str, int]

    def __init__(self, init_hands: Dict[str, int], start_player: str) -> None:
        """
        The initializing method for ChopStickState class.

        >>> init_hands = {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> css.hands == {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        True
        >>> css.current_player == "p1"
        True
        """
        self.hands = init_hands
        self.current_player = start_player

    def __str__(self) -> str:
        """
        The string method for ChopStickState, and will return a string
        in the format of "Player 1: {} - {}; Player 2: {} - {}" to
        represent the numbers of fingers currently on hands of each
        player.

        >>> init_hands = {"p1_l": 1, "p1_r": 2, "p2_l": 3, "p2_r": 4}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> print(css)
        Player 1: 1 - 2; Player 2: 3 - 4
        <BLANKLINE>

        >>> init_hands = {"p1_l": 0, "p1_r": 0, "p2_l": 0, "p2_r": 0}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> print(css)
        Player 1: 0 - 0; Player 2: 0 - 0
        <BLANKLINE>
        """
        hand_names = ['p1_l', 'p1_r', 'p2_l', 'p2_r']
        values = [self.hands[i] for i in hand_names]
        # Dict is unordered, to keep it safe, we don't use self.hands.values()
        state_string = "Player 1: {} - {}; Player 2: {} - {}\n".format(
            values[0],
            values[1],
            values[2],
            values[3]
        )
        return state_string

    def __eq__(self, other: Any) -> bool:
        """
        This method compares the self and other, and will return
        True if and only if self and other has the same type and
        the players' hands are the same in both of them.
        """
        return (type(self) == type(other)
                and self.hands == other.hands)

    def get_current_player_name(self) -> str:
        """
        This method will return the current player as a string.

        >>> init_hands = {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> css.get_current_player_name() == "p1"
        True
        """
        return self.current_player

    def get_possible_moves(self) -> List[str]:
        """
        This method will return the possible move based on current
        situation. No player can use a dead hand(with 0 finger) to attack
        other hands, no player can attack a dead hand. Also no player can
        attack his or her self's hand.

        >>> init_hands = {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> css.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']

        >>> init_hands = {"p1_l": 0, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> css.get_possible_moves()
        ['rl', 'rr']
        """
        possible_move = list()
        self_avaiable_hands = list()
        oppo_avaiable_hands = list()

        if self.current_player == "p1":
            self_avaiable_hands = [i for i in [
                "l", "r"
            ] if self.hands["p1_"+i] != 0]

            oppo_avaiable_hands = [i for i in [
                "l", "r"
            ] if self.hands["p2_"+i] != 0]

        elif self.current_player == "p2":
            self_avaiable_hands = [i for i in [
                "l", "r"
            ] if self.hands["p2_"+i] != 0]

            oppo_avaiable_hands = [i for i in [
                "l", "r"
            ] if self.hands["p1_"+i] != 0]

        for s_h in self_avaiable_hands:
            for o_h in oppo_avaiable_hands:
                possible_move.append(s_h+o_h)

        return possible_move

    def is_valid_move(self, move: str) -> bool:
        """
        This method takes a move string as input and return True
        if and only if the string of move is in the possible move
        of this game under current state.

        >>> init_hands = {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> css.is_valid_move("ll")
        True

        >>> init_hands = {"p1_l": 0, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> css.is_valid_move("lr")
        False
        """
        flag = bool(move in self.get_possible_moves())
        return flag

    def convert_move_to_make(self, move_to_make: str) -> List[str]:
        """
        Helper function convert a move string to the key of hands dict.

        >>> init_hands = {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> css.convert_move_to_make("ll")
        ['p1_l', 'p2_l']

        >>> init_hands = {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p2")
        >>> css.convert_move_to_make("rl")
        ['p2_r', 'p1_l']
        """
        # example of move_to_make: 'lr'
        if type(move_to_make) == list:
            move_to_make = move_to_make[0]
        # should be in format of "ll", "lr", "rl", "lr"
        assert len(move_to_make) == 2 and move_to_make in [
            "ll", "lr", "rl", "rr"]

        other_player = self.get_next_player()

        return [
            self.current_player + "_" + move_to_make[0],
            other_player + "_" + move_to_make[1]
        ]

    def make_move(self, move_to_make: str) -> "ChopSticksState":
        """
        This method takes a move to make string and returns
        a new state after the move is applied to the current state.
        Current state will now be modifie.

        >>> init_hands = {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> new_state = css.make_move("ll")
        >>> new_state.hands["p2_l"]
        2
        >>> new_state.hands["p1_l"]
        1

        >>> init_hands = {"p1_l": 1, "p1_r": 1, "p2_l": 1, "p2_r": 1}
        >>> css = ChopSticksState(init_hands, "p1")
        >>> new_state = css.make_move("lr")
        >>> new_state.hands["p2_r"]
        2
        """
        m = self.convert_move_to_make(move_to_make)
        # e.g. m: ["p1_l", "p2_r"]

        self_hand = m[0]
        oppo_hand = m[1]
        self_number = self.hands[self_hand]
        oppo_number = self.hands[oppo_hand]

        new_hands = self.hands.copy()
        new_oppo_number = (self_number + oppo_number) % 5
        new_hands[oppo_hand] = new_oppo_number
        new_player = self.get_next_player()

        # self.hands[m[1]] = new_oppo_number
        # self.current_player = self.get_next_player()
        # At this point, self.current_player has been updated.

        new_state = ChopSticksState(new_hands, new_player)
        return new_state


class SubstractSquareState(State):
    """
    This is a subclass of state and is used to describe the information
    about the SubstractSquare game.

    number: int: the current unmber state, when this number is zero,
    the game is ended.
    """
    number: int

    def __init__(self, init_number: str, start_player: str) -> None:
        """
        This initializing methods for SubstractSquareState.

        >>> sss = SubstractSquareState("30", "p1")
        >>> sss.number == 30
        True
        >>> sss.current_player == "p1"
        True

        >>> sss = SubstractSquareState("50", "p2")
        >>> sss.number == 50
        True
        >>> sss.current_player == "p2"
        True
        """
        self.number = int(init_number)
        self.current_player = start_player

    def __str__(self) -> str:
        """
        The string method of SubstractSquareState object and
        will return a string containing information about current
        numebr in this state.

        >>> sss = SubstractSquareState("30", "p1")
        >>> sss.__str__()
        'Current number: 30'

        >>> sss = SubstractSquareState("50", "p1")
        >>> sss.__str__()
        'Current number: 50'
        """
        state_report = "Current number: {0:d}".format(self.number)
        return state_report

    def __eq__(self, other: Any) -> bool:
        """
        This method returns a bool object and will return
        True if and only if self and other have the same
        type and have the same number.
        """
        return (
            type(self) == type(other)
            and self.number == other.number)

    def get_possible_moves(self) -> List[str]:
        """
        This string will return a list containing current possible move
        as string. This method will return all square number less than
        or equal to the current number of this state, also, 0 will
        NOT be returned.

        >>> sss = SubstractSquareState("20", "p1")
        >>> sss.get_possible_moves()
        ['1', '4', '9', '16']

        >>> sss = SubstractSquareState("10", "p2")
        >>> sss.get_possible_moves()
        ['1', '4', '9']
        """
        possible_moves = [str(i**2) for i in range(
            1, self.number + 1
        ) if i**2 <= self.number]
        return possible_moves

    def is_valid_move(self, move: str) -> bool:
        """
        This method will check if and only if the passed in move
        (as a string) is a valid move, specifically if the move is
        contained in the possible move of current state.

        >>> sss = SubstractSquareState("30", "p1")
        >>> sss.is_valid_move("16")
        True

        >>> sss = SubstractSquareState("50", "p1")
        >>> sss.is_valid_move("64")
        False

        >>> sss = SubstractSquareState("30", "p1")
        >>> sss.is_valid_move("15")
        False
        """
        flag = move in self.get_possible_moves()
        return flag

    def get_current_player_name(self):
        """
        This function will return the current player as string.

        >>> sss = SubstractSquareState("30", "p1")
        >>> sss.get_current_player_name() == "p1"
        True

        >>> sss = SubstractSquareState("30", "p2")
        >>> sss.get_current_player_name() == "p2"
        True
        """
        return self.current_player

    def make_move(self, move_to_make: str) -> "SubstractSquareState":
        """
        This method takes a move to make string and returns a new
        state after the move is applied to the current state.
        Current state will now be modified.

        >>> css = SubstractSquareState("30", "p1")
        >>> new_state = css.make_move("16")
        >>> new_state.number == 14
        True
        >>> css.number == 30
        True

        >>> css = SubstractSquareState("60", "p2")
        >>> new_state = css.make_move("1")
        >>> new_state.number
        59
        """
        number = self.number - int(move_to_make)
        if self.current_player == "p1":
            new_state = SubstractSquareState(str(number), "p2")
        else:
            new_state = SubstractSquareState(str(number), "p1")
        return new_state


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
