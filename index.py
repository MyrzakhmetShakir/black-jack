from logo import logo
import random
from colorama import Fore
import os
clear = lambda:os.system("clear")

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def randomNumber():
   return random.choice(card)

def ifTuz11(owner):
    random_c = randomNumber()
    if sum(owner) + random_c > 21 and random_c == 11:
        owner.append(1)
    else:
        owner.append(random_c)



def gaming():
    start = input(Fore.YELLOW + "Do you want play Black Jack game? 'y' - to play, 'n' - to not play " + Fore.WHITE)
    if start == "y":
        clear()
        print(Fore.CYAN + logo + Fore.WHITE)
        status = "playing"
        isBlackJack = False
        random_y1 = randomNumber()
        random_y2 = randomNumber()
        if random_y1 == 11 and random_y2 == 11:
            your_cards = [random_y1, 1]
        else:
            your_cards = [random_y1, random_y2]
        computer_cards = [randomNumber()]
        if sum(your_cards) == 21:
            isBlackJack = True
            print(f"Your cards: {your_cards} and sum is {sum(your_cards)} {Fore.LIGHTMAGENTA_EX} + B L A C K  J A C K + {Fore.WHITE}")
        else:
            print(f"Your cards: {your_cards} and sum is {sum(your_cards)}")
        print(f"Computer cards: {computer_cards}")
    
        while status == "playing":
            if isBlackJack == True:
                add_card = 'n'
            elif isBlackJack == False:
                add_card = input("If you want to add another card pick - 'y', but - to open dealers card pick - 'n' ")
            if add_card == "y":
                ifTuz11(your_cards)
                print(f"Your cards: {your_cards} and sum is {sum(your_cards)}")
                if sum(your_cards) > 21:
                    status = "Y O U   L O S E!"
                    print(Fore.RED + status + Fore.WHITE)
            elif add_card == "n":
                status = "changing"
                while sum(computer_cards) < 17:
                    ifTuz11(computer_cards)
                print (f"Your cards: {your_cards} and sum is {sum(your_cards)}")
                if len(computer_cards) == 2 and sum(computer_cards) == 21:
                    print(f"Computer's cards: {computer_cards} and sum is {sum(computer_cards)} {Fore.LIGHTMAGENTA_EX} + B L A C K  J A C K + {Fore.WHITE}")
                else:
                    print(f"Computer's cards: {computer_cards} and sum is {sum(computer_cards)}")
                if sum(computer_cards) > 21: 
                    print(Fore.GREEN + "Y O U   W I N!" + Fore.WHITE)
                elif sum(your_cards) > sum(computer_cards):
                    print(Fore.GREEN + "Y O U   W I N!" + Fore.WHITE)
                elif sum(your_cards) == sum(computer_cards):
                    print(Fore.CYAN + "D R A W  !!!" + Fore.WHITE)
                else:
                    print(Fore.RED + "Y O U   L O S E!" + Fore.WHITE)
        gaming()
gaming()


    
    

