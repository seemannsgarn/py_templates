import random

while True:
    choises = ["rock","paper","scissors","lizard","spock"]

    computer = random.choice(choises)
    player = None

    while player not in choises:
        player = input("rock, paper, scissors, lizard, or spock: ").lower()

        if player == computer:
            print("computer: ",computer)
            print("player: ",player)
            print("Tie!")

        elif player == "rock":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "lizard":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "spock":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")

        elif player == "lizard":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "spock":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")

        elif player == "spock":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "lizard":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")

        elif player == "scissors":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "lizard":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "spock":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")

        elif player == "paper":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "lizard":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "spock":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")