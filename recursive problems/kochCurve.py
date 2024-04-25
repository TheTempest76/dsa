import turtle as t

tu = t.Turtle()
wn = t.Screen()
tu.penup()
tu.setpos(-500,0)
tu.pendown()

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
       for angle in [60, -120, 60, 0]:
            koch(t,order-1,size//3)
            t.left(angle)
        

order , size = 3 , 1000 
koch(tu,order,size)
wn.exitonclick()