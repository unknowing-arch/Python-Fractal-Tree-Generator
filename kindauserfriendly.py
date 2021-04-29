import turtle
this = 'tha'
l = 120 #Defalt 120  # Length for branches over all
r = 23.5 #Defalt 23.5 #rotaton of branches
lv = 17 #Levels for tree
w = 15 #With of tree
print('\nheelo\n')
if this == 'that':
    c = input('Whant to customise it, or information? [Y] ')
    if c.lower() == 'y':
        lv = int(input('How many levels? Defalt 5: ')) # Levels for tree
        l = int(input('Length of branches? Defalt 120: ')) #defalt 120  # Length for branches over all
        r = float(input('What is the rotation? Defalt 23.5: ')) #defalt 23.5 #rotaton of branches
        w = int(input("tree width, defalt is 15: ")) # defalt is 15

class Tree_Fractal(turtle.Turtle):
    def __init__(self, level):
        super(Tree_Fractal, self).__init__()
        self.level = level
        self.hideturtle()
        self.speed(10)
        self.left(90)
        self.width(w)
        self.penup()
        self.back(l * 1.5)
        self.pendown()
        self.forward(l)
        self.draw_tree(l, level)
    def draw_tree(self, branch_length, level):
        w = self.width()
        self.width(w * 3 / 4)
        branch_length *= 3 / 4
        self.left(r)
        self.forward(branch_length)
        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.right(2 * r)
        self.forward(branch_length)
        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.left(r)
        self.width(w)
if __name__ == '__main__':
    tree = Tree_Fractal(lv)
    turtle.done()