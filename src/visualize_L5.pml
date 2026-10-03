bg_color white
show cartoon, 6BGT
color grey80, 6BGT
set cartoon_transparency, 0.4, 6BGT

show sticks, L5_vs_6BGT
color cyan, L5_vs_6BGT and elem C
util.cnc L5_vs_6BGT

select pocket, 6BGT within 5 of L5_vs_6BGT
zoom pocket, buffer=8
show sticks, pocket
color yellow, pocket and elem C
util.cnc pocket
set stick_radius, 0.35

delete hbonds
distance hbonds, L5_vs_6BGT, 6BGT, 3.5, mode=2
color red, hbonds
set dash_radius, 0.05
set dash_width, 2.5
