import turtle

t = turtle.Turtle(visible=False) #initiates turtle and removes pointer
t.speed('fastest')

t.lt(90)    #makes tree vertical #####

lv = 25
l = 120      #Values
r = 23.5

t.width(13)     #Creates the trunk
t.bk(l)         #Makes it look better
t.fd(l)

def draw_tree(l, level):
    width = t.width()  # save current width

    t.width(width * 3 / 4)  # narrow width

    l = 3.0 / 4.0 * l

    t.lt(r) #chooses with direction the fractle starts #####
    t.fd(l)

    if level < lv: #If level is more than the specified level then back up rotate and foward
        draw_tree(l, level + 1)
    t.bk(l) # Moves turtle back by l (Length)
    t.rt(2 * r)  #Rotates turtle right by 2r (Rotation)
    t.fd(l) #moves turtle forward by l (Length)

    if level < lv:  #if level is less that the specified level then add one to level and draw tree
        draw_tree(l, level + 1)
    t.bk(l)
    t.lt(r) #####

    t.width(width)  # restore the previous width

draw_tree(l, 2)
turtle.done()