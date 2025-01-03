class Participant:
    def __init__(self, name):        #Initializing the name, points and choice
        self.name = name
        self.points = 0
        self.choice = ""
    
    def choose(self):
        self.choice = input("{name}, select rock, paper, scissor, lizard or Spock: ".format(name=self.name)).lower()
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))
    
    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,           #Converting the player choices to numeric values to simplify the comparing process
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice]
    
    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1 ,1, -1],  # Rock
            [1, 0, -1, -1, 1],  # Paper
            [-1, 1, 0, 1, -1],  # Scissors
            [-1, 1, -1, 0, 1],  # Lizard
            [1, -1, 1, -1, 0]   # Spock
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)        #Passing the players choices for comparision
        print("Round resulted in a {result}".format(result=self.getResultAsString(result)))   
        if result > 0:
            p1.incrementPoint()               #Adding points according to win or loss
        elif result < 0:
            p2.incrementPoint()
    
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    
    def getResultAsString(self, result):
        res = {
            0: "draw",                           #Reconversion from numeric to string for better readability
            1: "win",
            -1: "loss"
        }
        return res[result]

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")
    
    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)  #Passing the two players that are playing 
    
    def checkEndCondition(self):
        response = input("Continue the game (Y/n)? ")
        if response.lower() == "y":
            return True
        else:
            return False
    
    def determineWinner(self):
        if self.participant.points > self.secondParticipant.points:
            print(f"{self.participant.name} is the Winner")
        elif self.secondParticipant.points > self.participant.points: 
            print(f"{self.secondParticipant.name} is the Winner")
        else:
            print("It's a draw!")


game = Game()

try:
    game.start()
    while game.checkEndCondition():
        game.start()                       # Start the game loop
    
    game.determineWinner()    
except KeyError:
    print("Please enter appropriate item")




