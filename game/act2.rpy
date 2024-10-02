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
        play sound "Locked Doorknob Jiggle.mp3"
        player "Can't open the door. It doesn't move at all. "
        $ have_talked_front_door_tried = False
        scene
        call screen front_enterance_movement
    else:
        scene
        call screen front_enterance_movement



    return



label act2_living_room:

    if times_been_to_living_room >= 3 and stick_picked_up == True:
        scene living_room_ghost
        $ show_ghost_trigger = True

        if ghost_clicked == True and have_talked_to_ghost == False:
            ghost_man "Oh... Hello there. "
            ghost_man "I have never seen you before. "
            ghost_man "What are you doing here? "
            menu:
                "Just visiting":
                    $ lies_counter += 1
                    player "I'm just here visiting. "
                    ghost_man "Ahh, yes. Of course. How do you like it so far?"
                    player "Yeah, it's pretty good. I think I've seen everything. "
                    player "But... I do have a little problem. {w}I can't seem to open the door. {w}"
                    ghost_man "Hahahaha. I see. So you are a visitor that got lost. "
                    player "Yeah, sure. So do you have the key?"
                    ghost_man "Oh, hahaah... {w}No. {w}"
                    if seen_ghost_girl == True:
                        ghost_man "So I understand you saw the girl. {w}Yes?{w}"
                        menu:
                            "Yes":
                                player "Yes, I think i did. "
                                if front_door_pushed_throught == True:
                                    player "She pushed me throught the door. "
                                    ghost_man "Yes, I see. "
                                else:
                                    pass
                                ghost_man "Well, she is the one with the key. "
                                player "Ok, so I just have to ask her to give me the key. "
                                ghost_man "Oh, hahhhaa. She is a bit different then me. "
                                player "What do you mean. "
                                ghost_man "She is very into the role of a ghost, and not a very nice ghost.  "
                            "No":
                                $ lies_counter += 1
                                ghost_man "Well in any case... "
                                ghost_man "She is a ghost like me, but fairly different. "
                                player "How so?"
                                ghost_man "She is not very friendly. "
                                ghost_man "I would be carefull if I were you. "
                    else:
                        ghost_man "I should tell you something. "
                        ghost_man "There is a girl here, she has what you are looking for. "
                        player "Where is this girl?"
                        ghost_man "She is in the room on the second floor. "
                        player "Great, I'll talk to her. Thanks. "


                "Came for a party":
                    player "I came for the party, but I guess no party here. "
                    ghost_man "Yes, I see. "
                    ghost_man "There is no party here. "
                    ghost_man "There was... A long time ago. "
                    if front_door_tried == True:
                        player "So no party and the front door is locked. "
                        ghost_man "Ah, yes."
                        if seen_ghost_girl == True:
                            ghost_man "I belive you saw the girl. "
                            player "The ghost. "
                            ghost_man "Yes, the ghost. She has the key to the door. "
                    else:
                        player "So what should I do now?"
                        ghost_man "There is room upstairs and the key is in the room. "
                        player "Great I'll just go get it. "

                "Looking for a friend":
                    ghost_man "Looking for someone, eh?"
                    player "Yes, my friend is missing. "
                    if seen_ghost_girl == True:
                        player "I think some girl took him. "
                        ghost_man "I see you met the girl. "
                        player "Yeah, who is she?"
                        ghost_man "She is a ghost like me. "
                        ghost_man "She probably has your friend in the room upstairs. "
                        player "Great, I'll get him and get out of here. "
                        ghost_man "Good luck with that. "

                    else:
                        ghost_man "Your friend is missing... {w}I think I might now something about that. {w}"
                        player "Anything would help. Please. "
                        ghost_man "Well there is a girl living im this house. "
                        player "A girl?"
                        ghost_man "Yes, she is probably upstairs right now in her room. "
                        player "That's great, I'll go find her. "

            ghost_man "You might want to reconsider that. "
            player "I can't. I need to go. "
            player "Can you help me in anyway. "
            if lies_counter == 0:
                ghost_man "I might know something. "
                ghost_man "I could get you the key if you ask nicely. "
                player "You can. Really?"
                player "Can you please give me the key. "
                ghost_man "Just a moment. "
                "A moment passes"
                ghost_man "Here it is, she is in the room as we speak. "
                $ upstairs_bedroom_key = True
            else:
                ghost_man "Oh well. "
                ghost_man "A word of advice. "
                ghost_man "Don't mension that she is a ghost. "
                player "Ok great, thank you. "

            $ have_talked_to_ghost = True

            call screen living_room_movement

        elif ghost_clicked == True and have_talked_to_ghost == True:
            ghost_man "Nothing to talk about. "

    if stick_picked_up == False:
        scene living_room_with_stick

    if stick_picked_up == True and times_been_to_living_room < 3:
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
        player "This is just a hallway. It's like something should be... or was in that wall in the middle. "
        $ downstairs_hall_never_been = False
        call screen downstairs_hall_movement
    else:
        call screen downstairs_hall_movement

    return



label act2_up_stairs_hall:
    scene upstairs_hall

    if been_up_stairs == False:
        $ been_up_stairs = True
        player "Another floor, with two doors. I wonder..."
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