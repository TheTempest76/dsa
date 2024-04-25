import turtle as tu
import random as r
tu.speed(0)


def tree(branch_len , levels):
    randsub = r.randrange(10,25)
    if levels<1 :
        return
    if levels <=3 :
        tu.color("green")
        tu.width(2)
    
    tu.forward(branch_len)
    tu.right(20)
    tree(branch_len-randsub, levels-1)
    tu.left(40)
    tree(branch_len-randsub, levels-1)
    tu.right(20)
    tu.backward(branch_len)
    if levels >2:
        tu.color("brown")
        tu.width(4)


def draw():
    
    tu.left(90)
    tu.up()
    tu.backward(500)
    tu.down()
    my_win = tu.Screen()
    tree(150 , 9)
    my_win.exitonclick()
    
draw()