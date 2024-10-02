define player = Character("[name]", color = "#59e73c")
define mike = Character("Mike", color = "#2d3bbe")
define ghost_girl = Character("Ghost girl", color = "#94fbff")
define ghost_man = Character("Ghost man", color = "#c2bfbf")

image detective idle = "images/Characters/Detective/detective_idle.png"
image detective hands over = "images/Characters/Detective/detective_hands_over.png" 
image woman idle = "images/Characters/Woman/woman_idle.png"
image woman hands over = "images/Characters/Woman/woman_hands_over.png"

image zenkagoredolje = Movie(channel="movie_dp", loop = False, image = "images/Scene2/bg_act1scene2shot05char.png", play = "videos/zenskaGoreDoljeCoverted.webm")

# $ renpy.movie_cutscene("videos/zenskaGoreDoljeCoverted.webm") --> za cutscene al se vraca na prosli scene ne ide dalje