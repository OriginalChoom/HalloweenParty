#izvan kuce
label act1_scene01:
    "This game is created for the Spooktober Game Jam"

    $ name = renpy.input("Enter your name: ", length=32)
    $ name = name.strip()
    if not name:
        $ name = "John"
    play music "audio/Music/Surface of the Moon - John Patitucci.mp3" fadein 2 fadeout 2
    scene act1_scene01 with dissolve
    mike "I think it's only a couple more minutes to the house. "
    player "I thought you've been to his place before."
    mike "Nah, this is the first time the party is at his house. "
    scene act1_scene02 with dissolve
    player "Aha, cool. Nice of him to finally do that. By the way, what's with the costume. Are you a ninja turtle or just a normal turtle."
    mike "Shut up [name]. You have no right to speak. I don't see you wearing a costume. And yeah, I'm an alien. They look exactly like this. I know, I've seen it. "
    player "Yeah sure, of course......"
    player "I'm not really feeling the party vibe right now. "
    mike "To be honest, me neither right now. Every time that happens, not really anything new. "
    player "Yeah, true. "
    scene act1_scene03 with dissolve
    mike "So, you think there will be girls at the party."
    player "Well, it better. We didn't come all the way over here to a sausage party. I don’t even know where we are. "
    #scene act1_scene04 with dissolve
    mike "Yeah, my thoughts exactly... We should be here in a sec. House 160, 162, 164, 16-6--- 169 " 
    mike "Hmm, weird, I guess they had a little mix up when they marked the building. "
    player "Just call the guy and ask."
    mike "I don’t know let’s not bother him, he’ll probably not even hear the phone ringing. "
    player "Well true. Hmmm, OK so... What was the address. "
    mike "something, something, street 169. We are at the right place. "
    menu:
        "Go into the house":
            $ not_go_intro_house = 1
        "Go to the party across the street":
            $ not_go_intro_house = 0

    if not_go_intro_house == 1:
        player "Yeah, that’s the right place. Let’s go inside. The party is probably in the back."
        scene act1_scene05
        mike "Yeah, you’re probably right. I don’t know why they didn’t put anything up or something. "
        menu:
            "Go in, let's check it out.":
                player "Let’s go in. What is the worst that can happen. "
                mike "Whatever you say [name]. Let’s check it out. Maybe the people are out back. "
                player "Yeah, if no one is there we just go back and call the guy or something. "
                jump act1_scene02


            "Turn back, no party here actually":
                player "I changed my mind. This looks like something out of a horror movie. Maybe we should not go in. "
                mike "Yeah, I don’t know. Doesn’t look like there are people here. "
                player "Let’s check the house across the street. Maybe that is where we need to be. "
                jump end_party

    elif not_go_intro_house == 0:
        player "Nah man, that is definitely not the right place. Just look at the other side od the street. You see the light and everything. "
        mike "Yeah, that looks like a party. Has ballons and everything. Let’s go there. "
        jump end_party 

#Ulazak u kucu
label act1_scene02:
    stop music
    play music "audio/Music/Sloppy Clav - Godmode.mp3" fadein 1 loop
    scene front_enterance with dissolve
    #play sound "door closing"
    player "Holy shit. "
    mike "Looks like nobody is here. Shit's kind of creepy"
    player "Yeah. They are probably in the back. Do you hear anything."
    mike "No. "
    player "Exacly, no music, who knows what kind of party for halloween is this. "
    mike "I don't know, but let's go see if they are in the back."
    player "Yep, let's go. "
    player "Or maybe you go left I go right?"
    mike "Whatever you want. Let's just hurry up. "
    menu:
        "Go together":
            player "Let's go together. Who knows what's in here. "
            mike "Ok great, let's go right, looks like a living room... "
            jump act1_scene02_together
        "Split up":
            player "I think it's best for us to split. We'll find people faster or we'll just find each other."
            mike "Ok cool, I'll go left you go right and we'll meet up here if we don't run into each other first. "
            jump act1_scene02_split
    return 

#kuca odvojeno
label act1_scene02_split:
    scene living_room_with_stick with dissolve
    player "{i}This looks like a living room. I guess nobody was here fore a long time. {/i}"
    player "{i}Definitaly no party here. Let's check out the other room. {/i}"
    scene kitchen_room_with_paper with dissolve
    player "{i}This is the kithcen. Again looks like it hasn't been used in a long time. Maybe we are at the wrong house.  {/i}"
    player "{i}I don't think anybody is here. Definitaly not in the house. There is a door here. Leading into the yard I bet.{/i}"
    player "{i}Let's have a look since we are already here. {/i}"
    scene yard_with_window with dissolve
    player "{i}Nobody is here. We are at the wrong house.{/i}"
    player "{i}And this yard hasn't been touched for a long time too.{/i}"
    scene kitchen_room_with_paper with dissolve
    player "{i}This is enough of this house I would say.{/i}"
    player "{i}Let's meet up with Mike and get out of here. {/i}"
    scene front_enterance with dissolve
    player "{i}Ok I'm ready to get out of here now. {/i}"
    player "{i}Now where is Mike. The house is not that big, he should be here by now.{/i}"
    player "MIKE!!! {w}MIKE!!!{w} "
    player "{i}This shit creepy me out now. {/i}"
    player "{i}Should I wait for Mike or just go.{/i}"
    menu:
        "Wait for Mike":
            player "{i}I should wait for Mike. What kind of a friend would I be if I left him at a creepy house.{/i}"
            "..."
            "Some time passes"
            player "{i}He should have been back already. {/i}"
            player "{i}I should search for him. {/i}"
            $ front_door_tried = False
            return 

        "Leave Mike, get out of the house":
            player "Eh, screw this. I don't know where he is, but I'm not styling here for a second longer. "
            player "{i}Let's get out of here. {/i}"
            "You try the door"
            play sound "Locked Doorknob Jiggle.mp3"
            player "{i}What is this. {w}The door won't open.{w}{/i}"
            player "{i}What is going on...{/i}"
            player "{i}This is crazy. It just locked itself. {w}I got to find a way out of here. {w}{/i}"
            $ front_door_tried = True
            return

    return

#kuca zajedno
label act1_scene02_together:
    scene living_room_with_stick with dissolve
    mike "Yeah, definitely a room, just not sure someone is living here. "
    player "It has all the furnature, but looks like it hasn't been used for a long time. "
    mike "I don't hear any music, but they may be in the back. "
    player "Let's check it out. "
    scene kitchen_room_with_paper with dissolve
    player "Again, empty, dirty, unsued for over a 100 years. "
    mike "Yep. {w}I'm starting to think we are at the wrong house. {w}"
    mike "There is the back door. "
    scene yard_with_window with dissolve
    mike "What do you see [name]?"
    player "Empty. {w}Nobody's home. {w}{w}They gave us the wrong adress or something else happned in the meantime. {w}"
    mike "I don't know what's happening. I just don't like it. {w}Let's just get our of here. {w} {w}There is still time we can make it to the party at the club. {w}"
    player "Yeah, let's go. This place creeps me out. "
    scene front_enterance with dissolve
    mike "Ok, let's get out of here. "
    "Mike tries to open the door"
    play sound "Locked Doorknob Jiggle.mp3"
    mike "The door won't open. "
    scene front_enterance_door with dissolve
    player "Wait... Let me try. "
    play sound "Locked Doorknob Jiggle.mp3"
    player "Yeah, completely shut. "
    mike "What are we going to do now. "
    player "I don't know... "
    player "Wait... {w}What is... {w} {w}happening.{w}"
    scene front_enterance_door_open01 with Dissolve(1)
    scene front_enterance_door_open02 with Dissolve(1)
    scene front_enterance_door_open03 with Dissolve(1)
    scene front_enterance_door_open04 with Dissolve(1)
    pause
    mike "Holy shit. {w}It... {w} {w}Opened?{w}"
    player "Are you seeing what I am seeing?"
    scene front_enterance_door_open05 with dissolve
    mike "We didn't take anything before coming here... {w}Did we?{w}"
    player "I don't think we did. {w}But... {w} {w}How is this possible. {w}"
    mike "I don't know... {w}But the door did open. {w} {w}Do you want to go in?{w}"
    player "I'm not sure, but what can we lose. "
    menu:
        "Go through the door":
            $ front_door_gone_throught = True
            player "Let's go through. "
            mike "Right behind you. "
            return 

        "Don't go through the door":
            $ front_door_pushed_throught = True
            $ seen_ghost_girl = True
            player "Let's not go through. "
            mike "Yo, [name]. "
            player "Yeah?"
            mike "Who is that?"
            scene front_enterance_girl with dissolve
            pause
            player "I don't know. "
            mike "Hee... Helloo..."
            scene front_enterance with Dissolve(1)
            player "What is that..."
            scene front_enterance_girl_closeup
            pause
            scene black
            pause
            scene front_enterance_falling_in 
            pause
            scene black
            pause
            return 

    return

label scene1:
    play music "audio/SoundTrack/Film Noir Ambient Jazz  Rainy  Dark Jazz to Study or Work To.mp3" fadein 2 fadeout 2
    play sound "audio/Rain and Thunder Sounds for Sleeping  30 Minutes of Thunder and Rain  Black Screen.mp3" fadein 2 fadeout 2
    scene bg_shot01 with Dissolve(2)
    detective "It was a quite night..."
    detective "It rained so hard it could make a flood..."
    scene bg_shot02 with dissolve
    detective "I hasn't stopped for a couple of hours... Just as I am preparing for the inevitable"
    detective "The time will come..." 
    scene bg_shot03 with dissolve
    detective "and it will come very soon"
    detective "I have to prepear myself no matter the outcome"
    scene bg_shot04 with dissolve
    detective "I'm begginig to think there will be no positive outcome"
    scene bg_shot05char with dissolve
    detective "What is my next move that is the big quieston. "
    scene bg_shot06 with dissolve
    pause
    scene bg_shot07 with dissolve
    pause
    scene bg_shot08 with dissolve
    detective "It all started a couple of days ago."
    detective "I was sitting in the office..."
    detective "Wiskey in one hand, cigar in the other."
    scene bg_shot09char with dissolve
    detective "Was going over some papers from the last job... When..."
    detective "I heard a knock on my door. "
    window hide
    play sound "audio/SoundEffects/knock Sound Effect.mp3"
    pause
    scene bg_shot10 with dissolve
    pause
    stop sound
    stop music
    return

label scene2:
    play music "audio/SoundTrack/Jazz Noir Detective Music - Perfect for Studying, Relaxing, General Listening.mp3" fadein 2 fadeout 2
    scene bg_act1scene2shot01 with Dissolve(2)
    pause
    play sound "audio/SoundEffects/Sound Effects - Footsteps.mp3"
    scene bg_act1scene2shot01acharlegs01 with dissolve
    pause
    scene bg_act1scene2shot01acharlegs02 with dissolve
    pause
    scene bg_act1scene2shot01acharlegs01 with dissolve
    pause
    scene bg_act1scene2shot02 with dissolve
    pause
    scene bg_act1scene2shot01acharlegs02 with dissolve
    pause
    scene bg_act1scene2shot01acharlegs01 with dissolve
    pause
    scene bg_act1scene2shot01acharlegs02 with dissolve
    pause
    scene bg_act1scene2shot02a with dissolve
    pause

    $ name = renpy.input("Enter the name: ", length=32)
    $ name = name.strip()
    if not name:
        $ name = "John"
    
    scene bg_act1scene2shot03 with dissolve
    pause
    scene bg_act1scene2shot03a with dissolve
    pause
    scene bg_act1scene2shot03b with dissolve
    pause
    scene bg_act1scene2shot03c with dissolve
    pause
    scene bg_act1scene2shot03anim-01 with Dissolve(1)
    scene bg_act1scene2shot03anim-03 with Dissolve(1)
    scene bg_act1scene2shot03anim-04 with Dissolve(1)
    scene bg_act1scene2shot03anim-05 with Dissolve(1)
    scene bg_act1scene2shot03anim-06 with Dissolve(1)
    scene bg_act1scene2shot03anim-07 with Dissolve(1)
    pause
    detective_name "I was sitting in the chair, when some lady walked in." with dissolve
    window hide
    show zenkagoredolje with Pause(5)
    scene bg_act1scene2shot05char with dissolve
    femaleChar "hello there" with dissolve
    scene bg_act1scene2shot04 with dissolve
    show detective idle at right with moveinright
    window show
    detective_name "Hello..."
    detective_name "What can I do for you?"
    show woman idle at left with moveinleft
    femaleChar "I am in need of a private detective..."
    show detective hands over at right with dissolve
    detective_name "Yes, what do you need."
    show detective idle at right with dissolve
    femaleChar "I need you to investigate something."
    show woman hands over at left with dissolve
    femaleChar "I need to find somebody."
    show woman idle at left with dissolve
    femaleChar "Last I heard he was at the hotel."
    femaleChar "Also he might be at this bar he likes to hand around. "
    detective_name "Ok I'll take a look."
    femaleChar "Thank you very much..."
    femaleChar "Goodbye"
    window hide
    hide woman idle with dissolve 
    pause
    window show
    detective_name "Hmmmm. Might as well start now. "
    detective_name "What is the best place to start? "
    menu:
        "Hotel":
            $ broj = 1
        "Bar":
            $ broj = 0
    if broj == 1:
        detective_name "Time to go to the Hotel."
    elif broj == 0:
        detective_name "Time go to to the Bar."

    stop music
    return
