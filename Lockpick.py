class Lockpick(object):

    def __init__(self,player):
        self.player = player
        self.durability = 100

    def pick (self):
        durability  -= random.randint(5,10)
