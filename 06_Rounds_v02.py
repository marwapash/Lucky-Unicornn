import random

# Set bal for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...  ").lower()
while play_again == "":


    # Increase # of rounds played
    rounds_played += 1


    # Print round number
    print()
    print("**** Round #{} ****".format(rounds_played))
  
    chosen_num = random.randint(1, 100)

    # Adjuest balance if the random # is between 1 and 5.
    # user gets a unicorn (+4 to bal)

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # If the random # is between 6 and 36, user gets a donkey (-1 from bal)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # The token is either horse or zebra, in both cases subrtarct 0.5 from bal
    else:
        # If the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # Otherwise, set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    if balance <1:
        # If balance is too low, exit game, output suitable message.
        play_again = "xxx"
        print("Sorry you have run out of money")


    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again, or xxx to quit  ")

    print()
