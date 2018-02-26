# TODO: import the modules needed to make game_interface run.
from strategy_old import *
from typing import List, Any, Callable, Dict


class GameInterface:
    """
    A game interface for a two-player, sequential move, zero-sum,
    perfect-information game.

    game - the  game to be played
    p1_strategy - strategy for player 1
    p2_strategy - strategy for player 2
    """
    game: "Game"
    p1_strategy: Callable[[Any], Any]
    p2_strategy: Callable[[Any], Any]

    def __init__(self, game: "Game", p1_strategy: Callable[[Any], Any],
                 p2_strategy: Callable[[Any], Any]) -> None:
        """
        Initialize this GameInterface, setting its active game to game, and
        using the strategies p1_strategy for Player 1 and p2_strategy for
        Player 2.
        """
        first_player = input("Type y if player 1 is to make the first move: ")
        is_p1_turn = False
        if first_player.lower() == 'y':
            is_p1_turn = True

        self.game = game(is_p1_turn)
        self.p1_strategy = p1_strategy
        self.p2_strategy = p2_strategy

    def play(self) -> None:
        """
        Play the game.
        """
        current_state = self.game.current_state

        print(self.game.get_instructions())
        print(current_state)

        # Pick moves until the game is over
        while not self.game.is_over(current_state):
            move_to_make = None

            # Print out all of the valid moves
            possible_moves = current_state.get_possible_moves()
            print("The current available moves are:")
            for move in possible_moves:
                print(move)

            # Pick a (legal) move.
            while not current_state.is_valid_move(move_to_make):
                current_strategy = self.p2_strategy
                if current_state.get_current_player_name() == 'p1':
                    current_strategy = self.p1_strategy
                move_to_make = current_strategy(self.game)

            # Apply the move
            current_player_name = current_state.get_current_player_name()
            new_game_state = current_state.make_move(move_to_make)
            self.game.current_state = new_game_state
            current_state = self.game.current_state # Update current state.

            print("{} made the move {}. The game's state is now:".format(
                current_player_name, move_to_make))
            print(current_state)

        # Print out the winner of the game
        if self.game.is_winner("p1"):
            print("Player 1 is the winner!")
        elif self.game.is_winner("p2"):
            print("Player 2 is the winner!")
        else:
            print("It's a tie!")


class Game():

    current_state: "State"

    def __str__(self):
        raise NotImplementedError("Subclass needed!")

    def __eq__(self, other):
        return (type(self) == type(other)
                and self.current_state == other.current_state)


class SubstractSquare(Game):
    """
    This class is a SubstractSquare game.
    Inherited from a super-class Game.
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the SubstractSquare game, if the is_p1_turn is set as true,
        then the new game will be initialized with current_player as "p1".
        Elsewise, the current_player will be initialized to "p2".

        This method contains user input, so no example will be provided.
        """
        init_number = input('Set initial number for the game'
                            '(non-negative whole number):')
        init_number = str(int(init_number))
        # Correct type.
        # TODO: Add try method to ensure the input type is an int as str type.
        if is_p1_turn:
            self.current_state = SubstractSquareState(init_number, "p1")
        else:
            self.current_state = SubstractSquareState(init_number, "p2")

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
        instruction = '''
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
        return instruction

    def str_to_move(self, move: str) -> str:
        """
        This function takes an user input move, a str, then it returns a
        reformatted string used. In this case, the input str will be
        returned since our program will recongnize it.

        >>> str_to_move("9")
        "9"
        >>> str_to_move("16")
        "16"
        """
        # In my version, moves are stored
        # as str, so it's not needed to be converted.
        return move

    def is_over(self, current_state: "State") -> bool:
        """
        This function takes a state as input and will return True if and only if
        the game is over (current number is 0) in the provided current state.

        This method involves user input in the intializing method of state, so
        no example is provided.
        """
        return bool(current_state.number == 0)

    def is_winner(self, player_to_check: str) -> bool:
        """
        This function take input as str, specifically, "p1" or "p2" and will
        return True if and only if the game is over now and this player is
        the winner of at the point.

        Specifically, if the opponent of this player is the current player
        after the updating, then this player is the winner.

        This method involve other attributes and methods of this class,
        So no example is provided.
        """
        if not self.is_over(self.current_state):
            return False
        return bool(self.current_state.current_player != player_to_check)


class ChopSticks(Game):
    """
    This class is a ChopSticks game.
    Inherited from a super-class Game.
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the ChopSticks game, if the is_p1_turn is get as true,
        then the new game will be initialized with current_player as "p1".
        Elsewise, the current_player will be initialized to "p2".

        This method contains user input, so no example is provided.
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

    def get_instructions(self) -> str:
        instruction = '''
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
        return instruction

    def str_to_move(self, move: str) -> str:
        """
        This method takes input move as a string and reformat
        it into the format that could be understood by our program.
        In this case, we don't have to reformat it.

        >>> str_to_move('ll')
        'll'
        >>> str_to_move('rl')
        'rl'
        """
        return move

    def is_over(self, current_state: "State") -> bool:
        """
        This method will return True if and only there is at least one
        player, according to the current state passed in as parameter,
        has his or her both hands dead (number of finger is 0).
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

        This method involve other attributes and methods of this class,
        So no example is provided.
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


class State():

    current_player: str  # 'p1' or 'p2'

    def __eq__(self, other):
        return (type(self) == type(other)
                and self.current_player == self.current_player)

    def get_possible_moves(self) -> List["..."]:
        raise NotImplementedError("Subclass needed!")

    def is_valid_move(self, move: str) -> bool:
        raise NotImplementedError("Subclass needed!")

    def get_current_player_name(self):
        raise NotImplementedError("Subclass needed!")

    def make_move(self, move_to_make):
        raise NotImplementedError("Subclass needed!")

    def get_next_player(self) -> str:
        if self.current_player == "p1":
            return "p2"
        else:
            return "p1"


class ChopSticksState(State):
    hands: Dict[str, int]

    def __init__(self, init_hands: Dict[str, int], start_player: str) -> None:
        self.hands = init_hands
        self.current_player = start_player

    def __str__(self) -> str:
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

    def get_current_player_name(self) -> str:
        return self.current_player

    def get_possible_moves(self) -> List[str]:
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

        flag = bool(move in self.get_possible_moves())
        return flag

    def convert_move_to_make(self, move_to_make: str) -> List[str]:
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

    def make_move(self, move_to_make: str) -> State:
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

    number: int

    def __init__(self, init_number, start_player) -> None:
        self.number = int(init_number)
        self.current_player = start_player

    def __str__(self) -> str:
        state_report = "Current number: {0:d}".format(self.number)
        return state_report

    def get_possible_moves(self) -> List[str]:
        possible_moves = [str(i**2) for i in range(
            1, self.number + 1
        ) if (i**2 <= self.number)]
        return possible_moves

    def is_valid_move(self, move: str) -> bool:
        flag = move in self.get_possible_moves()
        return flag

    def get_current_player_name(self):
        return self.current_player

    def make_move(self, move_to_make) -> State:
        number = self.number - int(move_to_make)
        if self.current_player == "p1":
            new_state = SubstractSquareState(number, "p2")
        else:
            new_state = SubstractSquareState(number, "p1")
        return new_state

# TODO: Replace None with the corresponding class name for your games.

# 's' should map to your implementation of Subtract Square, and 'c' should map
# to Chopsticks.
playable_games = {'s': SubstractSquare,
                  'c': ChopSticks}

# The strategies you are to implement.  See strategy_old.py, and then decide
# how to modify this.
usable_strategies = {'r': random_strategy,
                     'i': interactive_strategy}

if __name__ == '__main__':
    games = ", ".join(["'{}': {}".format(key, playable_games[key].__name__) if
                       playable_games[key] is not None else
                       "'{}': None".format(key) for key in playable_games])

    strategies = ", ".join(["'{}': {}".format(key,
                                              usable_strategies[key].__name__)
                            if usable_strategies[key] is not None else
                            "'{}': None".format(key)
                            for key in usable_strategies])

    chosen_game = ''
    while chosen_game not in playable_games.keys():
        chosen_game = input(
            "Select the game you want to play ({}): ".format(games))

    p1 = ''
    p2 = ''

    while p1 not in usable_strategies.keys():
        p1 = input("Select the strategy for Player 1 ({}): ".format(strategies))

    while p2 not in usable_strategies.keys():
        p2 = input("Select the strategy for Player 2 ({}): ".format(strategies))

    GameInterface(playable_games[chosen_game], usable_strategies[p1],
                  usable_strategies[p2]).play()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
