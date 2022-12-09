from screeninfo import get_monitors
from turtle import Screen, Turtle

x = 5
y = 5
degree = 5


def bounce_x():
    global x, degree
    x *= -1
    degree *= -1


def bounce_y():
    global y, degree
    y *= -1
    degree *= -1


width = int(str(get_monitors()[0]).split()[2].split('=')[1][0:-1])
height = int(str(get_monitors()[0]).split()[3].split('=')[1][0:-1])
screen = Screen()
screen.setup(width, height)
screen.listen()
screen.onkey(screen.bye, key='space')


screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)


ball = Turtle()
ball.hideturtle()
ball.penup()
ball.speed(100)
ball.shape('turtle')
ball.shapesize(4)
ball.goto(width / -2 + 60, height / 2 - 120)
ball.speed(10)
ball.showturtle()


if __name__ == "__main__":
    while True:

        try:
            ball.setheading(ball.heading() + degree)
            if ball.xcor() > width / 2 - 55.5 or ball.xcor() < width / -2 + 55.5:
                bounce_x()
            if ball.ycor() > height / 2 - 55.5 or ball.ycor() < height / -2 + 55.5:
                bounce_y()
            ball.goto(int(ball.xcor() + x), int(ball.ycor() + y))

        except:
            break
