# Reference
# https://openpsychometrics.org/tests/OEJTS/

# Title: Camping Trip

# Characters
define me = Character("Me", kind=nvl, color="#dc143c")
define may = Character("May", kind=nvl, color="#ffa500")
define mark = Character("Mark", kind=nvl)

# Other variables
define menu = nvl_menu
define narrator = nvl_narrator

define introversion = 3
define judging = False

# Story Flags (if needed)
define missing = False

# Personality Flags
define Fi = False
define Se = False
define Ti = False
define Ne = False

define Fe = False
define Si = False
define Te = False
define Ni = False

# Endgame results
define Dominant = ""
define Auxiliary = ""
define Tertiary = ""
define Inferior = ""

define Result = "" # Four letter combination

init:
    image black = Solid((0, 0, 0, 255))
    image green = Solid((75, 139, 59, 255))

init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = None
    config.window_show_transition = None

label start:

    # Should ask for some player info
    # Name
    # Gender

    jump common

    return

label common:

    scene black with dissolve
    show text "Part 1 \n\t Memories" with Pause(3)
    scene black with dissolve

    scene green with dissolve

    "The weekend came, I planned to stay at home and do some house cleaning."
    "While cleaning, I found some old camping equipment that was tucked away in a corner."
    "I take the equipments out to check if it can still be used or not."
    
    menu:
        "Imagine the memories.":    # Si

            "I close my eyes and let my memories came back."
            "I can feel the surrounding like the slow breeze of the wind carrying the smell of meat cooking nearby, and the sounds of birds chirping away on the trees."
            # $ Si = True

        "Search for pictures.":    # Se

            "I search around the store for old albums."
            "Looking at the pictures, I remember the moments when I went camping with my family."
            "The funny expressions that they make, and the beautiful scenary kept in the photo."
            # $ Se = True

    "So I decide that I want to relive those moments."
    "I take the equipments out from the store and start cleaning it."

    "I want to go camping, but when?"
    menu:
        "I should go camping tomorrow.":    # Judger
            $ judging = False
            call .tomorrow
        
        "I should go camping next week":    # Perceiver
            $ judging = True
            call .next_week
    
    "As for the location."
    "There is a place near a lake outside of town that I usually go when I was little."
    "Usually the place is empty as it is not a famous location."
    "It should be a good place to calm down even though it lacks some facilities."
    
    call .preparation
    
    jump camp

    return

label .tomorrow:

    "I can camp tomorrow, since I don't have anything to do."
    "Should I ask somebody to join me though?"

    menu:
        "Go solo.":

            call .solo
            $ introversion += 1

        "Ask your close friends":

            call .friends
            $ introversion -= 1

    return

label .next_week:

    "I need time to prepare some stuff before going on a trip."
    "Next week will probably be okay if I can manage everything well."
    "Should I ask someone to join me though?"

    menu:
        "Go solo.":

            $ introversion += 1
            call .solo

        "Ask your close friends":

            $ introversion -= 1
            call .friends

    return

label .preparation:

    if judging:
        me "Okay, what should I prepare first?"
        "Since it has been a while, I need to do some research to find more information on camping."
        ".   .   ."
        "After a few hours researching, I have come out with a checklist of things to bring."

    else:
        "I'll focus on the important things first."

    "I take a look again at the camping equipment to make sure that everything is good, and continue on preparing for other stuffs."

    return

label .solo:

    "I think I will be okay on my own."
    "It's not that I don't like anyone to join."
    "It's just my personal preference."
    "And this is also a good time to laid back and relax on my own accord."

    return

label .friends:

    "I call some of my best friends and asked them if they can join me or not."
    "First, I call May and ask her whether she wants to join or not."
    ".  .   ."

    # Can add the conversation if you're able to

    "After that, I call Mark to ask the same thing."
    ".  .   ."

    "Unfortunately, both of them are unable to join the trip because they are busy with work."
    "It means that I have to go alone."

    return

#========== Camping Trip Start ==========#
label camp:

    nvl clear

    scene black with dissolve
    show text "Part 2 \n\t The Day Arrives!" with Pause(3)
    scene black with dissolve

    scene green with dissolve

    "\"Ring, ring, ring!\", the loud noise of my alarm breaks me out of my slumber."
    "It is still early, but I have to get up and ready myself"
    "I get out of bed and look out the window."
    "It's still dark outside."
    "I take my phone and start checking the weather prediction for today and tomorrow."
    me "Nice everything is good."
    
    nvl clear
    
    if judging:
        "Checking the list again, I make sure to not forget anything behind."
        $ missing = False
    else:
        "Since, I didn't make any plans other than what I did yesterday, I just take everything important and will buy anything that I miss later."
        $ missing = True

    "I leave my home at around eight in the morning and start moving to my destination with my trusty bike."
    me "It has been a while. Hope that I can make it without any issues."

    nvl clear

    "Following the main route, I've noticed that the scenary looks familiar somehow."
    "I look around while cycling."

    "I noticed that the landscape around here have changed quite a bit since the last time I came here."
    menu:
        "Recall memories.":    # Si
            "I recall back some memories when I was a child."
            "The sensation that I take in during the journey is still the same as it was."
            # $ Si = True
        "Take in the view.":     # Se
            "I stop by a location where people stopped to take in the view."
            "The view of the mountains from here is a sight to behold."
            "After that brief rest, I continued on with my journey."
            # $ Se = True
    
    # =========== At Camping Ground (Noon) ========== #

    nvl clear

    scene black with dissolve
    show text "Camping Ground (Noon)" with Pause(3)
    scene black with dissolve

    scene green with dissolve

    "I arrived at the camping ground before noon."
    "I check in with the camping lodge before searching for a place to set up camp."
    
    ".   .   ."
    
    # Note: Find a hobby for introvert / extrovert
    # This is only for storytelling purpose
    "After setting the camp up, I sit at my chair and do something"

    # =========== At Camping Ground (Evening) ========== #

    nvl clear

    scene black with dissolve
    show text "Camping Ground (Evening)" with Pause(3)
    scene black with dissolve

    scene green with dissolve

    "Evening arrives, I see that there are some other campers nearby starting to prepare for the night."
    me "I should follow suit."

    # Note: This is for storytelling point
    # Consequence for preparing for camping trip
    
    if not missing:
        "My preparation for the night was done in a short time."
    else:
        "Well I forgot to bring my firewood."
        me "Guess I'll have to find some woods nearby."
        "And I quickly went out for wood gathering."
        ".   .   ."
        "I managed to finish set up my campfire as the sun begins to fall."

    "Now I need to start making dinner for myself."
    "While preparing dinner, I see a group of students that seems like they are unable to light up their fire."

    menu:
        "Help them.":   # Extraverted
            "I bring some fire starters and walk towards their camp."
            "I slowly approach them."
            me "You guys look troubled. Is there any problem?"
            $ introversion -= 1

        "Observe them":   # Introverted
            "I continue my observation from afar."
            
            ".   .   ."

            "I avert my eyes quickly."
            "But one of them apparently saw me looking at them, and came to me."
            may "Sorry for disturbing, can I ask something?"
            me "Yes you can, is there any problem?"
            $ introversion += 1

    may "Our fire won't start, and we have used all of our firestarters."
    me "Let me see."

    # Information gathering
    if judging:
        menu:
            "From experience.":    # Si
                "From what I remember, wood is hard to burn when it is wet."
                "And right now, it is off-season."
                me "So, the wood might be wet."
                $ Si = True
            
            "Make a guess.":    # Ni
                me "I'm guessing that the wood could be wet as it is off-season right now."
                $ Ni = True

    else:
        menu:
            "Look at the wood.":    # Se
                "I take a log from a bundle that they have collected to inspect it."
                me "It looks like the log is kinda wet."
                $ Se = True
            
            "Think possible reasons.":    # Ne
                "I think about a few reasons."
                "Maybe the wood is wet?"
                "Or that wood type is hard to catch on fire?"
                "I take a closer look at the wood."
                me "It's wet."
                $ Ne = True

    me "Did you pick the wood yourself?"
    may "Yes we did."
    may "Do we need to collect some wood now?"
    "She sounds worried."

    # Decision making
    if judging:
        menu:
            "Share some wood.":    # Fe
                "The right thing to do for now is to help them."
                me "Wait here."
                "I go back to my camp and take a few woods."
                me "This should be enough."
                "I hurry back to the group."
                me "Here take this."
                "I hold out the wood that I was carrying."
                may "Thank you, but don't you need it also?"
                me "Don't worry, I still have plenty at camp."
                $ Fe = True
            "Find some wood.":    # Te
                me "The sun is still up, should be enough time to search for more wood."
                may "Could you tell us how to tell the wood is dry or not?"
                "I give them a bit of advice on finding the dry wood."
                may "Ok got it."
                $ Te = True
    
    else:
        menu:
            "Share some wood.":    # Fi
                "After considering the options that I have, I've decided to share some of my wood."
                me "Wait here."
                "I go back to my camp and take a few woods."
                me "This should be enough."
                "I hurry back to the group."
                me "Here take this."
                "I hold out the wood that I was carrying."
                may "Thank you, but don't you need it also?"
                me "Don't worry, I still have plenty at camp."
                $ Fi = True
            "Find some wood.":    # Ti
                me "The sun is still up, should be enough time to search for more wood."
                may "Could you tell us how to tell the wood is dry or not?"
                "I give them a bit of advice on finding the dry wood."
                $ Ti = True


    "It looks like the fire problem was solved."
    "I continue working on my dinner."

    # =========== At Camping Ground (Night) ========== #

    nvl clear

    scene black with dissolve
    show text "Camping Ground (Night)" with Pause(3)
    scene black with dissolve

    scene green with dissolve

    "The moon shines bright, as it is full moon tonight."
    "Siting at my chair I begin eating my simple dinner."

    if not missing:
        "Tonight's dinner is a fancy one."
        "I manage to make a simple spaghetti, with the ingredients that I brought from home."
    else:
        "Tonight's dinner is a simple one."
        "I bought some cup noodles from a store on my way here earlier."
        "Although simple, it is satisfying enough."

    "A female student from the group earlier came with a plate in her hand."
    may "Thank you for your help earlier."
    may "Here take this food as an appreciation gift."
    "In her hands there are some grilled meat."
    me "It's not a big deal, but thank you."
    may "You're welcome."
    "She bowed as she said that."
    "And leave while waving her hands."

    # Should probably add more.

    "When I've finished my dinner. I sit back against my chair and look towards the mountain laying right in front of me."

    # Note: Can create a situation about self-reflection. Focus on intutive.

    "After a while, my eyelids became heavy, signaling that it is time for some shut-eye."
    "I get up from my chair, enter my tent, slide into my sleeping bag and close my eyes."
    
    # =========== At Camping Ground (Morning) ========== #

    nvl clear

    scene black with dissolve
    show text "Camping Ground (Morning)" with Pause(3)
    scene black with dissolve

    scene green with dissolve

    "I wake up early, with the help of my phone's alarm."
    "I want to watch the sunrise today."
    "And also get some breakfast ready."
    "The sun starts peeking out behind the hill at around six in the morning."

    ".   .   ."

    # Insert moments of awe here, LOL

    "After having breakfast I start packing my stuff and cleaning the camping area."

    ".   .   ."

    "Finish packing around noon. Visit the lodge for checkout and went back to civilization."

    # Add after story?

    ".:. The END"

    # End of Story

    jump end

    return

#========== Camping Trip End ==========#
# Use all information to determine the four letter personality of the player.
label end:

    nvl clear

    call .primary
    call .secondary
    call .conclude

    me "Result: [Result]"
    me "Dominant: [Dominant]"
    me "Auxiliary: [Auxiliary]"

    return

label .primary:

    # ===== Dominant Function ===== #
    # Determining the Dominant Cognitive Function of the player
    if Dominant == "":
        if judging:
            if introversion > 3:         # Introvert Judging
                if Si:
                    $ Dominant = "Si"
                elif Ni:
                    $ Dominant = "Ni"
            else:                        # Extravert Judging
                if Fe:
                    $ Dominant = "Fe"
                elif Te:
                    $ Dominant = "Te"
        else:
            if introversion > 3:         # Introvert Perceiving
                if Fi:
                    $ Dominant = "Fi"
                elif Ti:
                    $ Dominant = "Ti"
            else:                        # Extravert Perceiving
                if Se:
                    $ Dominant = "Se"
                elif Ne:
                    $ Dominant = "Ne"

    return

label .secondary:
    # ===== Secondary Function ===== #
    # Check Dominant Cognitive Function then direct to next situation to determine Auxiliary Function
    if Dominant != "" and Auxiliary == "":
        if Si or Ni:
            if Fe:
                $ Auxiliary = "Fe"
            elif Te:
                $ Auxiliary = "Te"
        
        elif Fe or Te:
            if Si:
                $ Auxiliary = "Si"
            elif Ni:
                $ Auxiliary = "Ni"

        elif Fi or Ti:
            if Se:
                $ Auxiliary = "Se"
            elif Ne:
                $ Auxiliary = "Ne" 

        elif Se or Ne:
            if Fi:
                $ Auxiliary = "Fi"
            elif Ti:
                $ Auxiliary = "Ti"

    return

label .conclude:

    if not judging:

        if (Dominant == "Fi") and (Auxiliary == "Ne"):
            $ Result = "INFP"
        
        elif (Dominant == "Fi") and (Auxiliary == "Se"):
            $ Result = "ISFP"

        elif (Dominant == "Se") and (Auxiliary == "Fi"):
            $ Result = "ESFP"
        
        elif (Dominant == "Se") and (Auxiliary == "Ti"):
            $ Result = "ESTP"

        elif (Dominant == "Ti") and (Auxiliary == "Se"):
            $ Result is "ISTP"

        elif (Dominant == "Ti") and (Auxiliary == "Ne"):
            $ Result = "INTP"

        elif (Dominant == "Ne") and (Auxiliary == "Ti"):
            $ Result = "ENTP"

        elif (Dominant == "Ne") and (Auxiliary == "Fi"):
            $ Result = "ENFP"

    else:

        if (Dominant == "Fe") and (Auxiliary == "Ni"):
            $ Result = "ENFJ"
        
        elif (Dominant == "Fe") and (Auxiliary == "Si"):
            $ Result = "ESFJ"

        elif (Dominant == "Si") and (Auxiliary == "Fe"):
            $ Result = "ISFJ"

        elif (Dominant == "Si") and (Auxiliary == "Te"):
            $ Result = "ISTJ"

        elif (Dominant == "Te") and (Auxiliary == "Si"):
            $ Result = "ESTJ"

        elif (Dominant == "Te") and (Auxiliary == "Ni"):
            $ Result = "ENTJ"

        elif (Dominant == "Te") and (Auxiliary == "Te"):
            $ Result = "INTJ"

        elif (Dominant == "Ni") and (Auxiliary == "Fe"):
            $ Result = "INFJ"

    return