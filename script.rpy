# Reference
# https://openpsychometrics.org/tests/OEJTS/

# Title: Camping Trip

# Characters
define me = Character("Me", kind=nvl)
define may = Character("May", kind=nvl)
define amy = Character("Amy", kind=nvl)
define mark = Character("Mark", kind=nvl)

# Other variables
define menu = nvl_menu
define narrator = nvl_narrator

define solo = False

define introversion = 3
define perceiving = False

define location = ""

# Cognitive Functions
define Si = False   # Introverted Sensing
define Se = False   # Extraverted Sensing

define Ni = False   # Introverted Intuition
define Ne = False   # Extraverted Intuition

define Ti = False   # Introverted Thinking
define Te = False   # Extraverted Thinking

define Fi = False   # Introverted Feeling
define Fe = False   # Extraverted Feeling

# Endgame results
define Primary = ""     # Primary Function
define Auxiliary = ""   # Secondary Function

define Result = ""

init python:
    # config.empty_window = nvl_show_core
    config.window_hide_transition = None
    config.window_show_transition = None

label start:

    # Should ask for some player info
    # Name
    # Gender

    jump common

    return

label common:

    "The weekend came, I planned to stay at home and do some house cleaning."
    "While cleaning, I found some old camping equipment that was tucked away in a corner."
    "I take the equipments out to check if it can still be used or not." 
    "While checking, a nostalgic feeling came back to me."
    
    "Seems like it can still be used, nice!"
    
    "I take the equipment out from the store and started cleaning it."
    "I should try camping again."
    "But when?"

    menu:
        "I should go camping tomorrow.":
            call .tomorrow
        
        "I should go camping next week":
            call .next_week
    
    "But before doing anything, I need to figure out where I should go."

    menu:
        "A less crowded location.":

            $ introversion += 1

            "There is a place near a lake outside of town that I usually go when I was little."
            "Usually the place is empty as it is not a famous location."
            "It should be a good place to calm down even though it lacks some facilities"

        "A famous location.":

            $ introversion -= 1

            "There is a place just outside of town that has just recently opened."
            "The facilities there are great by looking at the reviews of the place."
            "It should be okay for me even if there are a lot of people."
    
    jump camp

    return

label .tomorrow:

    $ perceiving = True

    "I can camp tomorrow, since I don't have anything to do."
    "Should I ask somebody to join me?"

    menu:
        "Go solo.":

            $ introversion += 1
            $ solo = True

        "Ask your close friends":

            $ introversion -= 1
            $ solo = False

    return

label .next_week:

    $ perceiving = False

    "I need time to prepare some stuff before going on a trip."
    "Next week will probably be okay if I can manage everything well."
    "Should I ask someone to join me?"

    menu:
        "Go solo.":

            $ introversion += 1
            $ solo = True

        "Ask your close friends":

            $ introversion -= 1
            $ solo = False

    return

label .solo:

    "I think I will be okay on my own."

    return

label .friends:

    "I "

    return

#========== Camping Trip Start ==========#
label camp:
    "Test before camp"

    if  solo:

        call .solo
    
    else:

        call .friends

    "Test after camp"

    jump end

    return

label .solo:

    "In solo."

    return

label .friends:

    "In group."

    return


#========== Camping Trip End ==========#
label end:

    "The END"

    return