label act1_scene01:
    "hello"
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

label scene3:
    window hide
    scene act1scene3shot01 with dissolve
    pause
    detective_name "There it is..." with dissolve
    detective_name "Time to go inside."

    return

label scene4:
    window hide
    scene act1scene4shot01 with dissolve
    pause
    detective_name "There it is..." with dissolve
    detective_name "Time to go inside."

    return