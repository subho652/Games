import random,time,sys
def yes_no():
    global play
    if plr_chip.chip == 0:
        print("Sorry! You lost all your chips.")
        play = False
    else:
        ans = input("\nDo you want to play another hand? Y/N: ").upper()
        if ans == 'Y':
            play = True
        else:
            play = False
            print("\nThank you for playing!")
class Dlr_Plr():
    card_dict = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'King': 10, 'Queen': 10}
    suits = ['Hearts','Spades','Diamonds','Clubs']
    ranks = list(card_dict.keys())
    def __init__(self):
        self.hand = []
        self.count = []
    def pick_card(self,n): #Pick n cards and store in self.hand & store the values too
        for _ in range(n):
            a = random.choice(self.ranks)
            b = self.card_dict[a]
            c = random.choice(self.suits)
            self.hand.append(a +' of '+ c)
            self.count.append(b)
    def add(self):
        for i in self.count:
            if i == 11 and sum(self.count)>21:
                self.count[self.count.index(i)] = 1
        return sum(self.count)
class Chips():
    def __init__(self):
        self.chip = 5000
    def add_chip(self,n):
        self.chip += n
    def sub_chip(self,n):
        self.chip -= n
def excp():
    print("Please enter the correct value.")
def bet_inp():
    global plr_chip,bet
    while True:
        try:
            while True:
                bet = int(input(("\nEnter the no. of chip to bet : ")))
                if bet<=plr_chip.chip:
                    break
                else:
                    print("Your bet exceeds the chip you have.")
        except:
            excp()
        else:
            break
def print_hand():
    global playing
    if playing:
        print("\nDealer's Hand:")
        print(dlr.hand[0],'\n<Card Hidden>')
        print(f"\nPlayer's Hand:{plr.add()}")
        print(*plr.hand,sep='\n')
    else:
        print(f"\nDealer's Hand:{dlr.add()}")
        print(*dlr.hand,sep='\n')
        print(f"\nPlayer's Hand:{plr.add()}")
        print(*plr.hand,sep='\n')
def plr_check():
    global playing
    if plr.add() == 21:
        playing = False
        print_hand()
        plr_chip.add_chip(bet*1.5)
        print(f"\nBLACKJACK!\nYou have {plr_chip.chip} chips.")
        yes_no()
    elif plr.add()>21:
        playing = False
        print_hand()
        plr_chip.sub_chip(bet)
        print(f"\nPlayer Busts!\nYou have {plr_chip.chip} chips.")
        yes_no()
    else:
        print_hand()
        hit_stand()
def dlr_check():
    def delay():
        print("\nDealer is playing",end='')
        for _ in range(3):
            print(".",end='')
            sys.stdout.flush()
            time.sleep(1)
        print('')
    if dlr.add() == 21:
        print_hand()
        plr_chip.sub_chip(bet)
        print(f"\nDealer wins!\nYou have {plr_chip.chip} chips.")
        yes_no()
    elif dlr.add() > 21:
        print_hand()
        plr_chip.add_chip(bet)
        print(f"\nDealer Busts!\nYou have {plr_chip.chip} chips.")
        yes_no()
    else:
        if dlr.add()<=16:
            delay()
            dlr.pick_card(1)
            if not dlr.add() >=21 or not dlr.add()>=17:
                print_hand()
            dlr_check()
        elif dlr.add()>=17:
            if dlr.add() > plr.add():
                print_hand()
                plr_chip.sub_chip(bet)
                print(f"\nDealer wins!\nYou have {plr_chip.chip} chips.")
                yes_no()
            elif dlr.add() < plr.add():
                print_hand()
                plr_chip.add_chip(bet)
                print(f"\nPlayer Wins!\nYou have {plr_chip.chip} chips.")
                yes_no()
            else:
                print_hand()
                print(f"It's a draw!\nYou have {plr_chip.chip} chips.")
                yes_no()
def hit_stand():
    global playing
    while True:
        stat = input('\nWould you like to hit or stand? (H/S) : ').upper()
        if stat == 'H':
            plr.pick_card(1)
            plr_check()   
        elif stat == 'S':
            playing = False
            dlr_check()
        else:
            excp()
            continue
        break    
play = True
plr_chip = Chips()
print("\nWelcome to BLACKJACK!\nGet as close to 21 as you can without going over!\nYou are being given 5000 chips to play with.")
while play:
    dlr = Dlr_Plr()
    plr = Dlr_Plr()
    playing = True
    bet_inp() #Input the bet
    dlr.pick_card(2)
    plr.pick_card(2)
    while True:
        plr_check()
        break