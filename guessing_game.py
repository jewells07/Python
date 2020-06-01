import random
def game(cpu):
    i=1
    while i <= 6:
        inputt=int(input(f"Please guess the number between {a} & {b}:  "))
        if inputt == cpu:
            print(f"Correct you took {i} trials to guess the number")
            return i
            break
        elif inputt > cpu:
            print("Wrong, guess a smaller number again")
        elif inputt < cpu:
            print("Wrong, guess a greater number again")
        i+=1
    
if __name__ == '__main__':
    print("Welcome... Player1 and Player2")
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))

        cpu1 = random.randint(a,b)
        print("\nPlayer1 you have 5 chance to guess the number")
        player1 = game(cpu1)

        cpu2 = random.randint(a,b)
        print("\nPlayer2 you have 5 chance to guess the number")
        player2 = game(cpu2)
        if player1 < player2:
            print("\nplayer1 won")
        elif player1 == player2:
            print("Game TIE")
        else:
            print("player2 won")
        print(f"\nThe number for player1 was {cpu1} and for player2 was {cpu2}\n")
    except Exception as e:
        print("\nYour Input is a String Error\nYou must enter integer")
        exit()
