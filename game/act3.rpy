label act3_bedroom:
    scene bedroom_girl_room
    player "Ugh..."
    player "Holy shit. Mike!"
    player "You good bro. "
    ghost_girl "He is just fine..."
    if seen_ghost_girl == True:
        player "So we meet again. "
        player "What do you want with Mike. "
    else:
        player "So you are the one I have heard about. "
    ghost_girl "......."
    player "Why did you take him. "
    ghost_girl "I.... I needed someone to play with. "
    player "Mike, brother, are you good?"
    mike "...."
    ghost_girl "I said he is fine!"
    scene bedroom_girl_room_head_turned
    menu:
        "What does a ghost want with him":
            ghost_girl "A ghost!"
            ghost_girl "Who are you calling a ghost. "
            player "Ugm... You..."
            ghost_girl "NO!"
            ghost_girl "..."
            scene bedroom_girl_scare
            $ win_conditions = 1

        "I can play with you":
            ghost_girl "You want to play?"
            ghost_girl "...."
            player "Yes, but you have to let go of my friend first. "
            ghost_girl "I don't like that. "
            player "Well, you can't like everything. "
            player "I'm happy to stay and play with you. "
            ghost_girl "Oh, well.... {w}{w}"
            ghost_girl "I guess that is fine. "
            player "Ok, now let my boy go. "
            ghost_girl "Ok..."
            ghost_girl ".........."
            $ win_conditions = 2

        "We can come again.":
            player "We can come again. "
            player "But we got to go now. "
            ghost_girl "NO!"
            player "We got to get back to are other friends. "
            player "I'm sure you understand. "
            player "You want friend too. {w}Don't you?{w}"
            ghost_girl "Yes... But he is my friend. "
            player "I'm also your friend, but me and him need to go now. "
            ghost_girl "You promise you will come back. "
            player "Yes, I promise. "
            player "Can you unluck the door for us now, please. "
            ghost_girl "Ok, I will. " 
            $ win_conditions = 3
    
    return 

label ending:
    if win_conditions == 1:
        scene bedroom_girl_scare
        pause
        scene black
        "You died. Killed by a ghost. "
        "Mike is still in the house. "
        "Stupid Ending"

    elif win_conditions == 2:
        scene bedroom_no_mike
        pause
        scene black with dissolve
        pause
        "You took Mikes place. "
        "He is now out of the house and you are in."
        "You traided places with you friend. "
        "A Brave Ending"

    if win_conditions == 3:
        scene bedroom_girl_room with dissolve
        pause
        scene act1_scene03 with dissolve
        "You made it out of the house. "
        "Both you and Mike survived. "
        "The Good Ending"


    return 