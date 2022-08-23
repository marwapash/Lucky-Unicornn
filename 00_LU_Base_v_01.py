#Functions go here ------------------------------------------
def yes_no(question):...
def yes_no(question):
    valid = False
    while not valid:
        response = input (question).lower()

        if response == "yes" or response == "y":
            respose = "yes"
            return response
        
        elif response == "no" or response == "n":
            response = "no"
            return response 
        else:
            print("Please answer yes or no")

# --------------------------------------------------------
def intructions():...
def yes_no(question):...

def instructions():
    print ()
    print ()
    print("***** How to Play *****")
    print()
    print("[The rules of the game go here]")
    print()
    return""

def yes_no(question):
    valid = False
    while not valid:
        response = input (question).lower()

        if response == "yes" or response == "y":
            respose = "yes"
            return response
        
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes or no")
# -----------------------------------------------------------
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

def num_check(question, low, high):

    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question)) 

            # If the amounr is too low / too high give
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine goes here ------------------------------------------
#----------------
show_instructions = yes_no("Have you played this game before?   ")
print ()
print ("You chose {}".format(show_instructions))

if show_instructions == "no":
    instructions()


having_fun = yes_no("Are you having fun?")
print()
print ("You said {} to having having fun.".format(having_fun))

print ()
print ()
print ("Program continues...")
#---------------
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print()
print("You will be spending ${}".format(how_much))


