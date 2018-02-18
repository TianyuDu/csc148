from tying import List

class Runner():

    '''This class representing a single runner and contains info about this runner
    speed - speed category of this runner.
    emial - email of this runner.
    '''
    speed: str
    email: str

    def __init__(self, speed: str, email: str) -> None:
        '''
        Initialize the runner.
        '''
        assert speed in [
        'under 20 min',
        'under 30 min',
        'under 40 min',
        '40 min or over']
        self.speed, self.email = speed, email

    def __eq__(self, other: "Runner") -> bool:
        '''
        Return True if and only if two runner are in the
        same speed category.
        '''
        return (type(self) == type(other)
            and self.speed == other.speed)

    def __str__(self) -> str:
        '''
        This function reports the speed category and email of this runner
        '''
        return "This runner is in category: {0:s}, this runner's email is {1:s}".\
        format(self.speed, self.email)

class RegList():
    '''
    This class contains object of runners and as a collection of runner.
    '''
    runners: List["Runner"]
    num_runners: int

    def __init__(self, email_list: List[str], speed_category_list: List[str]) -> None:
        '''
        Initialize RegList object.
        '''
        self.runners = list()
        assert len(email_list) == len(speed_category_list)
        for i in range(len(email_list)):
            self.runners.append(Runner(speed_category_list[i], email_list[i]))
        self.num_runners = len(self.runners)

    def update(self, email: str, new_speed: str) -> None:
        '''
        This method updates the speed category for the person with provied email.
        '''
        assert new_speed in [
        'under 20 min',
        'under 30 min',
        'under 40 min',
        '40 min or over'
        ]
        not_found = True
        for i in range(self.num_runners):
            if runners[i].email == email:
                runners[i].speed = new_speed
                not_found = False
                break

        if not_found:
            raise Exception("There's no runner in the runner pool with given email address.")

    def report(self, speed_category: str) -> List[str]:
        '''
        This method return a list of string containing emails of all runners
        in the given speed category. If no runner is in provided speed category,
        empty list will be returned.
        '''
        assert speed_category in [
        'under 20 min',
        'under 30 min',
        'under 40 min',
        '40 min or over'
        ]
        ret = list()
        for i in range(self.num_runners):
            if runners[i].speed == speed_category:
                ret.append(runners[i].email)
        return ret

    def find(self, email: str) -> str:
        '''
        This method return a list of string representing the speed category
        of the runner with the provided email address. If there's no runner
        associated with given email, None will be reutrned.
        '''
        for i in range(self.num_runners):
            if self.runners[i].email == email:
                return self.runners[i].speed
        return None



















