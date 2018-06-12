from typing import List


class Animal:

    name: str
    breed: str

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, self.name, self.breed)

    def __add__(self, other):
        return isinstance(other, Animal) and \
                self.name == other.name and \
                self.breed == other.breed

    def shout(self):
        raise NotImplementedError

    def get_owner_title(self):
        return "Owner"

    def bite_damage(self):
        return 10


class Dog(Animal):

    rewards: List[str]

    def __init__(self, name, breed, rewards=None):
        Animal.__init__(self, name, breed)
        self.rewards = rewards.copy() if rewards else []

    def __repr__(self):
        return "Dog({}, {}, {})".format(self.name, self.breed, self.rewards)

    def shout(self):
        return "Bark"

    def get_owner_title(self):
        return "ShitPicker"

    def bite_damage(self):
        return Animal.bite_damage(self) * 5

    def __add__(self, other):
        if not isinstance(self, Dog) or \
                not isinstance(other, Dog):
            raise Exception("You can only mate two dogs you maniac")
        return Dog(self.name[0: len(self.name) // 2] + other.name[len(other.name) // 2:], self.breed + " - " + other.breed)

    def add_reward(self, reward):
        self.rewards.append(reward)

class Cat(Animal):

    def shout(self):
        return "Meow"

    def get_owner_title(self):
        return "SandChanger"

    def bite_damage(self):
        return Animal.bite_damage(self) * 2


if __name__ == "__main__":
    d1 = Dog("Gun", "Frenchie")
    d2 = Dog("ZouKai", "BullDog")
    d3 = d1 + d2
    d3.add_reward("Runner")
    print(d3)
    print(d3.shout())
    print(d3.get_owner_title())

    c1 = Cat("MM", "Persian")
    print(c1)
    print(c1.get_owner_title())

    print(d3.bite_damage())
    print(c1.bite_damage())
