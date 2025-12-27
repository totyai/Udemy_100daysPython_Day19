from turtle import Turtle, Screen
import random


def main():
    is_race_on = False
    # Screen setup
    screen = Screen()
    # Enables the config of the screen
    screen.setup(width=500, height=400)
    # Input on the screen, and it returns that
    user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
    names = ["contender1", "contender2","contender3", "contender4", "contender5", "contender6" ]
    t_colors = ["red", "green", "purple", "blue", "brown","orange"]

    i = -100
    # Creating Turtles
    for u in range(6):
        names[u] = Turtle(shape="turtle")
        names[u].color(t_colors[u])
        names[u].penup()
        names[u].goto(x=-230, y=i)
        i += 30

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in names:
            if turtle.xcor() > 230:
                is_race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've won. The winner: {winner}")
                else:
                    print(f"You've lost. The winner: {winner}")
            rand_dist = random.randint(0,10)
            turtle.fd(rand_dist)

    screen.exitonclick()

if __name__ == "__main__":
    main()