import math
import random
import time
import turtle as t


def heart_coordinates(angle, scale):
    x = 16 * (math.sin(angle) ** 3) * scale
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale
    return x, y


def draw_heart_art():
    screen = t.Screen()
    screen.setup(700, 700)
    screen.bgcolor("black")
    screen.title("Pixel Heart")
    screen.tracer(0)

    pen = t.Turtle()
    pen.hideturtle()
    pen.speed(0)

    for i in range(10000):
        angle = random.uniform(0, 2 * math.pi)
        scale = random.uniform(0.5, 15.5)
        x, y = heart_coordinates(angle, scale)

        direction = math.atan2(y, x) + random.uniform(-0.5, 0.5)
        length = random.uniform(4, 14)

        pen.pencolor(1.0, random.uniform(0.25, 0.55), random.uniform(0.65, 0.85))
        pen.width(random.uniform(0.5, 1.2))
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.goto(x + length * math.cos(direction), y + length * math.sin(direction))

        if i % 200 == 0:
            screen.update()
            time.sleep(0.002)

    for j in range(3500):
        angle = random.uniform(0, 2 * math.pi)
        x, y = heart_coordinates(angle, 16.0)

        direction = math.atan2(y, x) + random.uniform(-0.35, 0.35)
        length = random.uniform(10, 32)

        pen.pencolor(1.0, random.uniform(0.45, 0.75), random.uniform(0.75, 0.95))
        pen.width(random.uniform(0.4, 0.9))
        pen.penup()
        pen.goto(x + random.uniform(-2, 2), y + random.uniform(-2, 2))
        pen.pendown()
        pen.goto(x + length * math.cos(direction), y + length * math.sin(direction))

        if j % 150 == 0:
            screen.update()
            time.sleep(0.002)

    pen.penup()
    pen.goto(0, -20)
    pen.pencolor("white")
    pen.write("I love you", align="center", font=("Arial", 28, "bold"))

    screen.update()
    t.done()


if __name__ == "__main__":
    draw_heart_art()