class Entity:
    """Class representing any player"""

    def __init__(self, name, action=-1):
        self.name = name
        self.action = action
        self.points = 0

    def fight(self, other_entity):
        """
        A single battle instance
        :params: another player
        """

        if (self.action - other_entity.action == 1 or
                self.action - other_entity.action == -2):
            self.points += 1
            self.win_prompt()
        elif self.action == other_entity.action:
            print("ITS A DRAW :-))")
        else:
            other_entity.points += 1
            other_entity.win_prompt()

    def win_prompt(self):
        print("{} WON !!!!".format(self.name))
