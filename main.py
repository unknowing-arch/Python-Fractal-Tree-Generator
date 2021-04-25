import turtle

WIDTH = float(input("tree width, defalt is 15: ")) #defalt is 15
BRANCH_LENGTH = float(input("Branch length, defalt is 120: ")) #defalt is 120
ROTATION_LENGTH = float(input("rotation length, defalt is 27: ")) #defalt is 27
tree_level = float(input("tree level, defalt is 5: ")) #deflat is 5

class Tree_Fractal(turtle.Turtle):
    def __init__(self, level):
        super(Tree_Fractal, self).__init__()
        self.level = level
        self.hideturtle()
        self.speed('fastest')
        self.left(90)
        self.width(WIDTH)
        self.penup()
        self.back(BRANCH_LENGTH * 1.5)
        self.pendown()
        self.forward(BRANCH_LENGTH)
        self.draw_tree(BRANCH_LENGTH, level)

    def draw_tree(self, branch_length, level):
        width = self.width()
        self.width(width * 3 / 4)
        branch_length *= 3 / 4
        self.left(ROTATION_LENGTH)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.right(2 * ROTATION_LENGTH)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.left(ROTATION_LENGTH)

        self.width(width)


if __name__ == '__main__':
    tree = Tree_Fractal(tree_level)
    turtle.done()