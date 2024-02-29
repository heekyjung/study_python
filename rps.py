import random


def replay():
    while True:
        reply = input("Do you want to REPLAY? (y/n) : ").lower()
        if reply in ['y', 'n']:
            return reply


def rps():
    rps_list = ['rock', 'paper', 'scissors']
    wins = 0
    losses = 0
    ties = 0

    while True:
        player = ""

        while player not in rps_list:
            player = input(
                "Enter one of rock, paper, scissors : ").lower()

        computer = random.choice(rps_list)

        if player == computer:
            ties += 1
            print(f"It's a tie! (you: {player} VS computer: {computer})")
        elif (player == "rock" and computer == 'scissors') or (player == "paper" and computer == 'rock') or (player == "scissors" and computer == 'paper'):
            wins += 1
            print(f"You win!! (you: {player} VS computer: {computer})")
        else:
            losses += 1
            print(f"You lose.. (you: {player} VS computer: {computer})")

        reply = replay()
        if reply == "n":
            print(f"{wins} win{'s' if wins > 1 else ''}, {ties} tie{'s' if ties > 1 else ''}, {losses} loss{'es' if losses > 1 else ''}")
            break


rps()
