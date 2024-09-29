#string name --> ne moze se defineat al da znam da postoji -- koristi se jednom na pocetku igre.

define flash = Fade(0.1, 1.5, 0.5, color="#fff")

#keys
default study_room_key = False

default upstairs_room_key = False
default upstairs_bedroom_key = False

default have_wc_key = False



#have beens
default been_up_stairs = False
default downstairs_hall_never_been = True
default have_talked_front_door_tried = False


#talk points
default have_talked_to_ghost = False          #da ne greeta stalno


#things tried act1
default front_door_tried = False              #jel se probo front door ako je kasnije ce drugi dialog bit kad se dobije opcija za izac u free roamu
default front_door_gone_throught = False      #za novi dialog s duhom
default front_door_pushed_throught = False    #jel zenska usrala charatera da padne kroz vrata - ugl za transition u act 2
default seen_ghost_girl = False               #za kasnije da duh zna jesi ju video vec ili ne jos

#counters and stuff
default times_been_to_living_room = 0
default seen_outside = 0

#picked up things
default stick_picked_up = False
default paper_picked_up = False