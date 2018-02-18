"""
revision 3
This file contains super and subclasses for gmae objects.
"""
from typing import Any
from state import State, ChopSticksState, SubstractSquareState


class Game:
    """
    The base class for game object.

    current_state: a State object describing the current state of
        this game.

    instruction: a string containing essential information about
    what this game is about, and shows what to do and the goal of
    this game.
    """
    current_state: State
    instruction: str

    def __init__(self) -> None:
        """
        This function initialize the Game object,
        and this method should not be called directly
        from a Game base class.
        """
        raise NotImplementedError("Subclass needed!")

    def __str__(self) -> str:
        """
        This function reports the current state.
        This methond need subclass to be implemented.
        """
        raise NotImplementedError("Subclass needed!")

    def __eq__(self, other: Any) -> bool:
        """
        This method examines whether two game are objects are identical,
        it returns True if and only if the type of two comparing objects
        has the identical type and same state attribute.
        """
        return (type(self) == type(other)
                and self.current_state == other.current_state)

    def get_instructions(self) -> str:
        """
        This method returns a string containing instructions about
        this game to show the instruction to player.
        """
        raise NotImplementedError("Subclass needed!")


class SubstractSquare(Game):
    """
    This class is a SubstractSquare game.
    Inherited from a super-class Game.

    current_state: a SubstractSquareState object that describing the
    the current state of this game.
    """
    current_state: SubstractSquareState

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the SubstractSquare game, if the is_p1_turn is set  as true,
        then the new game will be initialized with current_player as "p1".
        Elsewise, the current_player will be initialized to "p2".

        This method contains user input, so no example will be provided.
        """
        init_number = input('Set initial number for the game'
                            '(non-negative whole number):')
        init_number = str(int(init_number))

        if is_p1_turn:
            self.current_state = SubstractSquareState(init_number, "p1")
        else:
            self.current_state = SubstractSquareState(init_number, "p2")

        self.instruction = '''
        [Instruction for Substract Square Game]
        [Game Description]
        1). A positive whole number is randomly chosen as the starting value
            by some neutral entity. In our case, the user will choose it.

        2). The player whose turn it is chooses some square of a positive whole
            number (such as 1, 4, 9, 16, ... ) to substract from the value,
            provided the chosen square is not larger. After substracting, we
            have a new value and the next player chooses a square to substract
            from it.

        3). Play continues to alternate between the two players until no moves 
            are possible. Whoever is about to play at that point loses!

        4). Input: a positive whole number you would like to substract
            from the provided action choice set.
        '''

    def __eq__(self, other: Any) -> bool:
        """
        This method return True if and only if self and other has
        the same type and the same *.current_state attribute.
        """
        return (type(self) == type(other)
                and self.current_state == other.current_state)

    def __str__(self) -> str:
        """
        This method returns the string containing information about this game
        itself and the information about the current state of this game, also
        it returns the current player of this game.
        """
        game_str = "A SubstractSquare Game object, \n with current state: "
        state_str = self.current_state.__str__()
        player_str = "\n {}".format(self.current_state.current_player)
        return game_str + state_str + player_str

    def get_instructions(self) -> str:
        """
        This method returns the instruction of this game to the
        user to show how this game works.

        To provide examples of this method we have to implement an
        object to call this method, but the initialzation method
        of the type of object involves user input call, so no
        example for this method will be provided.
        """
        return self.instruction

    def str_to_move(self, move: str) -> str:
        """
        This function takes an user input move, a str, then it returns a
        reformatted string used. In this case, the input str will be
        returned since our program will recongnize it.

        To provide examples of this method we have to implement an
        object to call this method, but the initialzation method
        of the type of object involves user input call, so no
        example for this method will be provided.
        """
        return move

    def is_over(self, current_state: SubstractSquareState) -> bool:
        """
        This function takes a state as input and will return True if and only if
        the game is over (current number is 0) in the provided current state.

        To provide examples of this method we have to implement an
        object to call this method, but the initialzation method
        of the type of object involves user input call, so no
        example for this method will be provided.
        """
        return bool(current_state.number == 0)

    def is_winner(self, player_to_check: str) -> bool:
        """
        This function take input as str, specifically, "p1" or "p2" and will
        return True if and only if the game is over now and this player is
        the winner of at the point.

        Specifically, if the opponent of this player is the current player
        after the updating, then this player is the winner.

        To write example for this method, we need to create a new
        SubstractSquare object, the initializing method of
        this class involves user input, so no exmaple will be
        provided.
        """
        if not self.is_over(self.current_state):
            return False
        return bool(self.current_state.current_player != player_to_check)


class ChopSticks(Game):
    """
    This class is a ChopSticks game.
    Inherited from a super-class Game.

    current_state: the current state for ChopStick game to describe
    the current situation of this game.
    """

    current_state: ChopSticksState

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the ChopSticks game, if the is_p1_turn is get as true,
        then the new game will be initialized with current_player as "p1".
        Elsewise, the current_player will be initialized to "p2".

        >>> cs = ChopSticks(True)
        >>> print(cs.current_state.current_player)
        p1
        >>> cs = ChopSticks(False)
        >>> print(cs.current_state.current_player)
        p2
        """
        init_hands = {
            "p1_l": 1,
            "p1_r": 1,
            "p2_l": 1,
            "p2_r": 1
        }
        if is_p1_turn:
            self.current_state = ChopSticksState(init_hands, "p1")
        else:
            self.current_state = ChopSticksState(init_hands, "p2")

        self.instruction = '''
        [Instruction for Chop Sticks Game]
        1). Each of two players begins with one finger pointed up on each
            of their hands.

        2). Player A touches one hand to one of Player B's hands,
            increasing the number of fingers pointing up on Player B's
            hand by the number on Player A's hand. The number pointing up
            on Player A's hand remains the same.

        3). If Player B now has five fingers up, that hand becomes "dead"
            or unplayable. If the number of fingers should exceed five,
            substract five from the sum.

        4). Now Player B touches one hand to one of Player A's hands, and
            the distribution of fingers proceeds as above, increasing 
            the possibility of a "dead" hand.

        5). Play repeats steps 2-4 until some player has two "dead" hands,
            thus losing.

        6). Input: a string from possible move set promoted. In the format
            of 'll', 'lr', 'rl', 'rr'.
            For example, 'lr' means use yours left hand to touch the other
            player's right hand. If you have a hand with 0 fingers(dead), 
            you then could not use this hand to touch. Also, you could 
            not touch a dead hand of the other player.
        '''

    def __str__(self) -> str:
        """
        This method returns the string containing information about this gmae
        itself and the information about the current state of this game,
        also it returns the current player of this game.
        """
        game_str = "A ChopSticks Game object, \n with current state: "
        state_str = self.current_state.__str__()
        player_str = "\n {}".format(self.current_state.current_player)
        return game_str + state_str + player_str

    def __eq__(self, other: Any) -> bool:
        """
        This method return True if and only if self and other has
        the same type and the same *.current_state attribute.
        """
        return (type(self) == type(other)
                and self.current_state == other.current_state)

    def get_instructions(self) -> str:
        """
        This method will returns the instruction of this game to the
        user to show how this game works.
        >>> cs = ChopSticks(True)
        >>> cs.get_instructions() == cs.instruction
        True
        """
        return self.instruction

    def str_to_move(self, move: str) -> str:
        """
        This method takes input move as a string and reformat
        it into the format that could be understood by our program.
        In this case, we don't have to reformat it.
        >>> cs = ChopSticks(True)
        >>> cs.str_to_move('ll')
        'll'
        >>> cs = ChopSticks(True)
        >>> cs.str_to_move('rl')
        'rl'
        """
        return move

    def is_over(self, current_state: ChopSticksState) -> bool:
        """
        This method will return True if and only there is at least one
        player, according to the current state passed in as parameter,
        has his or her both hands dead (number of finger is 0).

        >>> cs = ChopSticks(True)
        >>> state = ChopSticksState({"p1_l": 1, "p1_r": 1, "p2_l": 1,\
        "p2_r": 1}, "p1")
        >>> cs.is_over(state)
        False

        >>> cs = ChopSticks(True)
        >>> state = ChopSticksState({"p1_l": 0, "p1_r": 0, "p2_l": 1,\
        "p2_r": 1}, "p1")
        >>> cs.is_over(state)
        True
        """
        flag_1 = (current_state.hands["p1_l"]
                  == current_state.hands["p1_r"]
                  == 0)

        flag_2 = (current_state.hands["p2_l"]
                  == current_state.hands["p2_r"]
                  == 0)
        return flag_1 or flag_2

    def is_winner(self, player_to_check: str) -> bool:
        """
        This function take input as str, specifically, "p1" or "p2" and will
        return True if and only if the game is over now and this player is
        the winner of at the point.

        Specifically, if this opponent of this player has two dead hand,
        then is player is the winner.
        >>> cs = ChopSticks(True)
        >>> cs.is_winner("p1")
        False

        >>> cs.current_state.hands["p1_l"] = 0
        >>> cs.current_state.hands["p1_r"] = 0
        >>> cs.is_winner("p2")
        True
        """
        if not self.is_over(self.current_state):
            # If not over, return False anyway.
            return False
        oppo = str()
        if player_to_check == "p1":
            oppo = "p2"
        if player_to_check == "p2":
            oppo = "p1"
        return (
            self.current_state.hands[oppo + "_l"] == 0
            and self.current_state.hands[oppo + "_r"] == 0
        )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
