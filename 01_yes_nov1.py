# Ask the user if they have played before
show_instructions = input ("Have you played this game before before? ").lower()


# If they say yes, output 'programe continues'
if show_instructions == "yes":
                           print("program continues")


elif show_instructions == "no":
    print("display instructions")

# If they say no, output 'display instructions'
else:
    print("Please answer yes/no")

# Formatting

print("You chose {}".format(show_instructions))
