play = True
def win_check():
    return bl[1]==bl[4]==bl[7]!=' ' or bl[7]==bl[8]==bl[9]!=' ' or bl[3]==bl[6]==bl[9]!=' ' or bl[1]==bl[2]==bl[3]!=' ' or bl[2]==bl[5]==bl[8]!=' ' or bl[4]==bl[5]==bl[6]!=' ' or bl[1]==bl[5]==bl[9]!=' ' or bl[3]==bl[5]==bl[7]!=' '
def player_inp():
    def make_correct_choice():
        if n not in '123456789':
            print("\nPlease make a correct choice.")
            return True
        elif n in '123456789' and ' ' not in bl[int(n)]:
            print("\nPlease make a correct choice.")
            return True
        else:
            return False
    entry = True
    while entry:
        if i%2!=0:
            n = input(f'\n{a} enter your choice(1-9): ')
            entry = make_correct_choice()
            mark = 'X'
        else:
            n = input(f'\n{b} enter your choice(1-9): ')
            entry = make_correct_choice()
            mark = 'O'
    bl[int(n)] = mark
def msg(won):
    def yes_no():
        global play
        ans = input("\nDo you want to play again? Y/N: ").upper()
        if ans == 'Y':
            play = True
        else:
            play = False
            print("\nThank you for playing!")
    if won and i%2!=0:
        print(f"\nCongrats! {a} has won.\nBetter luck next time {b}.")
        yes_no()
    if won and i%2==0:
        print(f"\nCongrats! {b} has won.\nBetter luck next time {a}.")
        yes_no()
    if not won and i==9:
        print("\nThe match is a draw!")
        yes_no()
while play:
    print("\nTHE GAME STARTS NOW!")
    bl = ['#']+[' ']*9
    i = 1
    a = input("\nEnter name of Player 1(X): ")
    b = input("Enter name of Player 2(O): ")
    print(f'''
            7 | 8 | 9
           -----------
            4 | 5 | 6
           -----------
            1 | 2 | 3 ''')
    print("make your choice accordingly")
    while i<=9:
        player_inp()
        print(f'''
         {bl[7]} | {bl[8]} | {bl[9]}
        -----------
         {bl[4]} | {bl[5]} | {bl[6]}
        -----------
         {bl[1]} | {bl[2]} | {bl[3]} ''')
        msg(win_check())
        if win_check() == True:
            break
        i += 1
