from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "{}, {}, {}, {}".format(self.face, self.body, self.arm, self.leg)


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

    @abstractmethod
    def builder(self):
        self.build_body()
        self.build_face()
        self.build_arm()
        self.build_leg()
        return self


class Beauty(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "可爱的脸蛋"

    def build_body(self):
        self.player.body = "性感的身材"

    def build_arm(self):
        self.player.arm = "纤细的手臂"

    def build_leg(self):
        self.player.leg = "大长腿"

    def builder(self):
        super().builder()
        return self.player


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "丑陋的脸蛋"

    def build_body(self):
        self.player.body = "巨大"

    def build_arm(self):
        self.player.arm = "粗壮的手臂"

    def build_leg(self):
        self.player.leg = "一瘸一拐的腿"

    def builder(self):
        super().builder()
        return self.player


if __name__ == "__main__":
    # client
    beauty = Beauty().builder()
    print(beauty)

    monster = Monster().builder()
    print(monster)
