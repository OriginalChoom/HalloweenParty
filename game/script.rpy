

'''
label splashscreen:
    scene black
    with Pause(1)

    play sound "audio/SoundEffects/Broken light bulb sound effect.mp3"

    show text "just some people\nPRESENTS" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1.5)

    stop sound
    return
'''

# The game starts here.

label start:
    $ renpy.music.set_volume(0.3, 0.5, channel="music")
    $ renpy.music.set_volume(0.6, 0.7, channel="sound")
    call act1_scene01

    call act2_scene01


