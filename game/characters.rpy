define detective = Character("Detective", color = "#42f5da")
define detective_name = Character("[name]", color = "#42f5da")
define femaleChar = Character("Lady", color = "#b94292")

image detective idle = "images/Characters/Detective/detective_idle.png"
image detective hands over = "images/Characters/Detective/detective_hands_over.png" 
image woman idle = "images/Characters/Woman/woman_idle.png"
image woman hands over = "images/Characters/Woman/woman_hands_over.png"

image zenkagoredolje = Movie(channel="movie_dp", loop = False, image = "images/Scene2/bg_act1scene2shot05char.png", play = "videos/zenskaGoreDoljeCoverted.webm")

# $ renpy.movie_cutscene("videos/zenskaGoreDoljeCoverted.webm") --> za cutscene al se vraca na prosli scene ne ide dalje