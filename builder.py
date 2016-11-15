from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon \
    ham mushrooms red_onion oregano')
STEP_DELAY = 3

class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.topping = []

        def __str__(self):
            return self.name

        def prepare_dough(self, dough):
            print('preparing the {} dough of your {}...'.format(
                self.dough.name, self))
            time.sleep(SETP_DELAY)
            print('donw with the {} dough'.format(self.dough.name))

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)

    def add_topping(self):
        self.pizza.topping.append([i for i in
            (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)

    def back(self):
        self.progress = PizzaProgress.baking
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready

class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough,
            builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza

def validate_style(builders):
    try:
        pizza_style = input('what pizza would you like, \
            [m]atgarita or [c]reamy bacon?')
        builder = builders[pizza_style]()
        validate_input = True
    except Exception as err:
        print("Sorry, only margarita (key m) and \
            creamy bacon (key c) are available")
        return (False, None)
    return (True, builder)

def main():
    builders = dict(m=MargaritaBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print('Enjoy your {}!'.format(pizza))

if __name__ == "__main__":
    main()



