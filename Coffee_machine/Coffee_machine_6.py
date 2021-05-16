class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.status = ''

    def write_action(self):
        action = input("Write action (buy, fill, take, remaining, exit):")  #types of actions
        self.status = action
        return self.status

    def buy(self):
        type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        print('')
        
        if type == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            if self.coffee_beans < 16:
                print('Sorry, not enough coffe beans!')
            if  self.cups < 1:
                print('Sorry, not enough cups!')
            if self.water >= 250 and self.coffee_beans >= 16 and self.cups >= 1:
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
        if type == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            if self.milk < 75:
                print('Sorry, not enough milk!')
            if self.coffee_beans < 20:
                print('Sorry, not enough coffe beans!')
            if  self.cups < 1:
                print('Sorry, not enough cups!')
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
        if type == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            if self.milk < 100:
                print('Sorry, not enough milk!')
            if self.coffee_beans < 12:
                print('Sorry, not enough coffe beans!')
            if  self.cups < 1:
                print('Sorry, not enough cups!')
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
                print('I have enough resources, making you a coffee!')
        if type == 'back':
            None
                    
    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.coffee_beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))
        
    def take(self):
        print('')
        print('I gave you ${}'.format(self.money)) 
        self.money = 0   
        
    def remaining(self):
        print('')
        print('The coffee machine has:')
        print('{} of water'.format(self.water))
        print('{} of milk'.format(self.milk))
        print('{} of coffee beans'.format(self.coffee_beans))
        print('{} of disposable cups'.format(self.cups))
        print('${} + of money'.format(self.money))
             
coffeemachine = CoffeeMachine()

while coffeemachine.write_action() != 'exit':
    print()
    if coffeemachine.status == 'buy':
        coffeemachine.buy()
        print()
    elif coffeemachine.status == 'fill':
        coffeemachine.fill()
    elif coffeemachine.status == 'take':
        coffeemachine.take()
    elif coffeemachine.status == 'remaining':
        coffeemachine.remaining()
        print()
