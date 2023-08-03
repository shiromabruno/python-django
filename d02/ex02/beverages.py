class HotBeverage:

    price = 0.30
    name =  "hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    #In Python, to print 2 decimal places we will use str.format() with “{:.2f}” 
    #Exemplo: float = 2.154327
    #         format_float = "{:.2f}".format(float)
    # OUTPUT: 2.15
    def __str__(self):
        return f"name : {self.name} \nprice : {self.price:.2f}\ndescription : {self.description()}"

# como parametro precisa ter a CLASSE PAI
class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    description = "A coffee, to stay awake."

    def description(self):
        return "A coffee, to stay awake."

# como parametro precisa ter a CLASSE PAI
class Tea(HotBeverage):
    name = "tea"
    price = 0.30
    description = "Just some hot water in a cup."

    def description(self):
        return "Just some hot water in a cup."


# como parametro precisa ter a CLASSE PAI
class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    description = "Chocolate, sweet chocolate..."

    def description(self):
        return "Chocolate, sweet chocolate..."


# como parametro precisa ter a CLASSE PAI
class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    description = "Un po’ di Italia nella sua tazza!"

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__ == '__main__':
    hot_beverage = HotBeverage()
    print(hot_beverage)

    coffee = Coffee()
    print(coffee)

    tea = Tea()
    print(tea)

    chocolate = Chocolate()
    print(chocolate)

    cappuccino = Cappuccino()
    print(cappuccino)