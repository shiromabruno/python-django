import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:

    def __init__(self):
        self.drinks_feitos = 0
        self.flag_quebrado = False

    def repair(self):
        self.flag_quebrado = False
        self.drinks_feitos = 0
        print("Coffe machine is fully repaired! Now it is working!")
    
    def serve(self, objeto_hot_beverage):

        self.drinks_feitos += 1

        if self.flag_quebrado:
            raise BrokenMachineException()

        if self.drinks_feitos > 9:
            self.flag_quebrado = True
            self.drinks_feitos = 0

        
        #Random retorna algum elemento aleatorio da lista random.choice([lista, com, os, elementos])
        if random.choice([True, False]):
            return objeto_hot_beverage()
        else:
            return EmptyCup()


class EmptyCup(HotBeverage):
    name = "empty cup"
    price = 0.90

    def description(self):
        return "An empty cup?! Gimme my money back!"


class BrokenMachineException(Exception):
    def __init__(self, mensagem_quebrado="This coffee machine has to be repaired."):
        #self.message = mensagem_quebrado
        super().__init__(mensagem_quebrado)

    

if __name__ == '__main__':
    coffee_machine = CoffeeMachine()

    try:
        for x in range(25):
            drink = coffee_machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
            print(drink)
            flag_continua = False
    except BrokenMachineException as ex:
        print(ex)
        coffee_machine.repair()
    
    try:
        for x in range(5):
            drink = coffee_machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
            print(drink)
            flag_continua = False
    except BrokenMachineException as ex:
        print(ex)
    



    
