screen front_enterance_movement:
    add "front_enterance"

    #ulaz u dnevnu sobu
    imagebutton:
        xpos 1585
        ypos 0
        idle "front_enterance_idle"
        hover "front_enterance_hover"
        action Jump("act2_living_room")

    #gore stepenicama
    imagebutton:
        xpos 1096
        ypos 372
        idle "front_to_upstairs_idle"
        hover "front_to_upstairs_hover"
        action Jump("act2_up_stairs_hall")

    #study room
    imagebutton:
        xpos 561
        ypos 82
        idle "front_to_study_room_idle"
        hover "front_to_study_room_hover"
        action Jump("act2_study_room")
    
    #hodnik dolje
    imagebutton:
        xpos 986
        ypos 412
        idle "front_to_downstairs_hall_idle"
        hover "front_to_downstairs_hall_hover"
        action Jump("act2_downstairs_hall")

    #ako se nisu probala vrata u act1
    if front_door_tried == False:
        imagebutton:
            xpos 958
            ypos 919
            idle "front_door_to_outside_idle"
            hover "front_door_to_outside_hover"
            action SetVariable("have_talked_front_door_tried",True), SetVariable("front_door_tried",True), Jump("act2_front_enterance")


screen living_room_movement:
    #vracanje na front enterance
    imagebutton:
        xpos 317
        ypos 919
        idle "living_room_to_front_idle"
        hover "living_room_to_front_hover"
        action Jump("act2_front_enterance")

    #to kitchen
    imagebutton:
        xpos 86
        ypos 253
        idle "living_room_to_kitchen_idle"
        hover "living_room_to_kitchen_hover"
        action Jump("act2_kitchen_room")

    #ghost show up
    if times_been_to_living_room > 3 and stick_picked_up == True:
        imagebutton:
            pass

    #stick pick up
    if stick_picked_up == False:
        imagebutton:
            xpos 1075
            ypos 842
            idle "stick_pick_up_idle"
            hover "stick_pick_up_hover"
            action SetVariable("stick_picked_up", True), Jump("act2_living_room")


screen kitchen_room_movement:
    #to living room
    imagebutton:
        xpos 614
        ypos 933
        idle "kitchen_room_to_living_idle"
        hover "kitchen_room_to_living_hover"
        action Jump("act2_living_room")

    #to outdoors
    imagebutton:
        xpos 302
        ypos 348
        idle "kitchen_room_to_outdoors_idle"
        hover "kitchen_room_to_outdoors_hover"
        action Jump("act2_outdoors_window")

    #to downstairs hall
    imagebutton:
        xpos 0 
        ypos 275
        idle "kitchen_room_to_downstairs_hall_idle"
        hover "kitchen_room_to_downstairs_hall_hover"
        action Jump("act2_downstairs_hall")

    #paper pick up
    if paper_picked_up == False:
        imagebutton:
            xpos 926
            ypos 533
            idle "paper_pick_up_idle"
            hover "paper_pick_up_hover"
            action SetVariable("paper_picked_up", True), Jump("act2_kitchen_room")
    


screen downstairs_hall_movement:
    #to front
    imagebutton:
        xpos 233
        ypos 44
        idle "downstairs_hall_to_front_idle"
        hover "downstairs_hall_to_front_hover"
        action Jump("act2_front_enterance")

    #to kitchen
    imagebutton:
        xpos 984
        ypos 932
        idle "downstairs_hall_to_kitchen_idle"
        hover "downstairs_hall_to_kitchen_hover"
        action Jump("act2_kitchen_room")

    #to wc
    imagebutton:
        xpos 1350
        ypos 160
        idle "downstairs_hall_to_wc_idle"
        hover "downstairs_hall_to_wc_hover"
        action Jump("act2_wc")


screen up_stairs_hall_movement:
    #nazad dolje
    imagebutton:
        xpos 0 
        ypos 740
        idle "up_stairs_to_front_idle"
        hover "up_stairs_to_front_hover"
        action Jump("act2_front_enterance")

    #zakljucana soba - nez sta ce bit tamo
    imagebutton:
        xpos 510
        ypos 405
        idle "upstairs_to_room_idle"
        hover "upstairs_to_room_hover"
        action Jump("act2_up_stairs_hall_room")

    #spavaca soba
    imagebutton:
        xpos 1111
        ypos 335
        idle "upstairs_to_bedroom_idle"
        hover "upstairs_to_bedroom_hover"
        action Jump("act2_up_stairs_hall_bedroom")


screen outside_window_movement:
    #vracanje nazad u kuhinju
    imagebutton:
        xpos 1625
        ypos 689
        idle "outside_yard_to_kitchen_idle"
        hover "outside_yard_to_kitchen_hover"
        action SetVariable("seen_outside", 1), Jump("act2_kitchen_room")


