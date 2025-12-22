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




def main():
    t.listen()
    screen.exitonclick()



if __name__ == "__main__":
    main()