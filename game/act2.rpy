label act2_scene01:
    if front_door_gone_throught == True:
        scene front_enterance with flash
        pause
        player "Oh... {w}That was weird. {w}"
        player "Mike. You good?"
        "Silence dawn the room"
        player "Mike? {w}Where are you? {w}"
        player "Oh, shit. Mike's gone. What the hell did this door do to us. "
        player "Everything looks the same, but what happened to Mike. "
        player "We never should have come here, but we had to go to the party. "
        player "Anyway... "

    elif front_door_pushed_throught == True:
        scene black 
        scene front_enterance with Dissolve(2)
        player "What the hell happened!?"
        scene black with Dissolve(1)
        scene front_enterance with Dissolve(1)
        player "Ugh... My head. "
        player "{i}I think I've fallen into the door. {/i}"
        player "{i}Oh shit.  {/i}"

    else:
        scene front_enterance

    player "{i}I got to find a way out of here.{/i}"
    player "{i}I should look around, see if I can find something to open the door. {/i}"
    #free roam unlocked
    
    
    return 