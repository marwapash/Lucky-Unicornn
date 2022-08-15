

# functions go here...

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


# main routine goes here

show_instructions = yes_no("Have you played this game before? ")
print ("You chose {}".format(show_instructions))


having_fun = yes_no("Are you having fun?")
print ("You said {} to having having fun".format(having_fun))




   



 




