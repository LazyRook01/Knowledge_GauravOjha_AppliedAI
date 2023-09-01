from logic import *

# Define logical symbols for characters, rooms, and weapons
mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

# Combine all symbols into a single list
symbols = characters + rooms + weapons

# Function to check knowledge and print results
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: YES")
        elif model_check(knowledge, Not(symbol)):
            print(f"{symbol}: NO")
        else:
            print(f"{symbol}: MAYBE")

# Create an initial knowledge base
knowledge = And(
    Or(mustard, plum, scarlet),   # There must be a person
    Or(ballroom, kitchen, library),  # There must be a room
    Or(knife, revolver, wrench)  # There must be a weapon
)

# Add more information to the knowledge base
knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

# Check and print the possible values of each card
check_knowledge(knowledge)
