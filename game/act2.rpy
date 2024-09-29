label act2_scene01:
    if front_door_gone_throught == True:
        scene front_enterance with flash
        pause
        player "Oh... {w}That was weird. {w}"
        player "Mike. You good?"
        "Silence dawns the room"
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
    player "{i}I should look around, see if I can find something to open the door with. {/i}"
    #free roam unlocked

    return


label act2_front_enterance:
    scene front_enterance
    if have_talked_front_door_tried == True:
        #play sound
        player "Can't open the door. It doesn't move at all. "
        $ have_talked_front_door_tried = False
        scene
        call screen front_enterance_movement
    else:
        scene
        call screen front_enterance_movement



    return



label act2_living_room:

    if times_been_to_living_room > 3 and stick_picked_up == True:
        scene living_room_ghost

        if have_talked_to_ghost == False:
            "awodawowdk"

        else:
            "dwadawmadwlk"

        call screen living_room_movement

    else:
        pass

    if stick_picked_up == False:
        scene living_room_with_stick

    elif stick_picked_up == True:
        $ times_been_to_living_room += 1
        scene living_room

    call screen living_room_movement


    
    return 


label act2_kitchen_room:
    if paper_picked_up == False:
        scene kitchen_room_with_paper
    
    elif paper_picked_up == True:
        scene kitchen_room
    
    call screen kitchen_room_movement

label act2_study_room:
    scene front_enterance
    if study_room_key == False:
        player "Can't open the door. It seems to be locked. "
        call screen front_enterance_movement
    else:
        #udi u sobu
        pass
    
    return



label act2_downstairs_hall:
    scene downstairs_hall
    if downstairs_hall_never_been == True:
        player "hmm never been here"
        $ downstairs_hall_never_been = False
        call screen downstairs_hall_movement
    else:
        call screen downstairs_hall_movement

    return



label act2_up_stairs_hall:
    scene upstairs_hall

    if been_up_stairs == False:
        $ been_up_stairs = True
        player "holy shit"
    else:
        pass
    
    call screen up_stairs_hall_movement

    return


label act2_up_stairs_hall_room:
    if upstairs_room_key == False:
        player "Can't get in. No key. "

    else:
        pass
    
    call screen up_stairs_hall_movement

    return

label act2_up_stairs_hall_bedroom:
    if upstairs_bedroom_key == False and (stick_picked_up == False or paper_picked_up == False):
        player "No way in. Have to find a way to open the door. "
        player "It seems the key is in the lock from the other side of the door. "
    
    elif stick_picked_up == True and paper_picked_up == True and upstairs_bedroom_key == False:
        player "Ok this should work. "
        player "Just need to put the paper under the door first. "
        player "Give it a little push with the stick. "
        player "And..."
        player "Volia. {w}I have the key{w}"
        $ upstairs_bedroom_key = True

    elif upstairs_bedroom_key == True:
        player "Ok, I have the key. I can go in. "
        return

    call screen up_stairs_hall_movement

    return


label act2_wc:
    if have_wc_key == False:
        player "Can't open the door. I wonder where it leads. "
        
    else:
        return

    call screen downstairs_hall_movement
    
    return


label act2_outdoors_window:
    if seen_outside == 0:
        scene yard_with_window

    elif seen_outside == 1:
        scene yard_with_window_ghost

    call screen outside_window_movement

    return