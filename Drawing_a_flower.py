import turtle

def draw_square() :
    window= turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    
    counter = 1
    while counter < 5:
    
        brad.forward(150)
        brad.right(90)
        counter = counter + 1
        
draw_square()
def draw_circle() :
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)
    
draw_circle()
def draw_triangle() :
    triangle_counter = 0
    james= turtle.Turtle()
    james.color("blue")
    
    while triangle_counter < 3:
        james.right(120)
        james.forward(100)
        
        triangle_counter = triangle_counter + 1
    
draw_triangle()
window.exitonclick()
