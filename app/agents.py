class Agent:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.preferences = {}
        self.constraints = {}

class BuyerAgent(Agent):
    def __init__(self, id):
        super().__init__(id, 'buyer')

    def getInformation(self, preferences, constraints):
        self.preferences = preferences
        self.constraints = constraints

class SupplierAgent(Agent):
    def __init__(self):
        super().__init__(id, 'supplier')
        self.services = []

    def getInformation(self, preferences, constraints, services):
        self.preferences = preferences
        self.constraints = constraints
        self.services = services


