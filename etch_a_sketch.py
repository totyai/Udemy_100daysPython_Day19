"""
Requirements:
- Useing the keyboard to controll movement of the turtle
w = Forwards with draw
S = Backwards with draw
A = Turn counter Clockwise
D = Turn Clockwise
C = Clear and back to center
"""
import turtle as t

sketch = t.Turtle()
screen = t.Screen()

def forward():
    sketch.fd(20)

def backward():
    sketch.bk(20)

def turn_right():
    sketch.right(10)

def turn_left():
    sketch.left(10)

def clear():
    sketch.reset()



def main():
    screen.listen()
    screen.onkey(key="w",fun=forward)
    screen.onkey(key="s", fun=backward)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="c", fun=clear)
    screen.exitonclick()



if __name__ == "__main__":
    main()