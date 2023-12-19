import turtle
import random

# global vars:
score = 0
attempts = 10
current_direction = 'stop'
dark_mode = False
paused = False
status = None
elements_speed = 0.3
last_speed_increase_score = 0
level = 0

# window :
main_window = turtle.Screen()
main_window.title("First Game")
main_window.bgpic('background.gif')
main_window.setup(width=300, height=300)
main_window.tracer(0)
main_window.register_shape('ice.gif')
main_window.register_shape('fire.gif')
main_window.register_shape('life.gif')
main_window.register_shape('man.gif')
main_window.register_shape('right.gif')

# pause label :
paused_label = turtle.Turtle()
paused_label.hideturtle()
paused_label.penup()
paused_label.color('red')
paused_label.goto(-260, 260)
# paused_label.write('{}'.format(status), align='left', font=('Courier', 20, 'normal'))

# score label:
pen = turtle.Turtle()
# pen.bgcolor('red')
pen.hideturtle()
pen.penup()
pen.color('purple')
font = ('Courier', 26, 'bold')
pen.goto(260, 260)
pen.write('Your Score: {}, Lives: {} ,Level: {} '.format(score, attempts, level), align='center', font=font)

# Player
actor = turtle.Turtle()
actor.shape('man.gif')
actor.speed(0)
actor.penup()
actor.goto(0, -270)

# Game elements
red_list = []
for i in range(10):
    red_element = turtle.Turtle()
    red_element.shape('ice.gif')
    red_element.penup()
    red_element.speed(random.randint(1, 4))
    red_element.goto(0, 250)
    red_list.append(red_element)

black_list = []
for i in range(10):
    black_element = turtle.Turtle()
    black_element.shape('fire.gif')
    black_element.penup()
    black_element.speed(random.randint(1, 4))
    black_element.goto(50, 270)
    black_list.append(black_element)

life_list = []
for i in range(2):
    life_element = turtle.Turtle()
    life_element.shape('life.gif')
    life_element.penup()
    life_element.speed(random.randint(1, 4))
    life_element.goto(50, 270)
    life_list.append(life_element)

# global functions:
def change_direction_left():
    global current_direction
    current_direction = 'left'


def change_direction_right():
    global current_direction
    current_direction = 'right'


def change_direction_stop():
    global current_direction
    current_direction = 'stop'


def darken_background():
    main_window.bgcolor('black')


def restore_background():
    main_window.bgcolor('white')


def change_direction_pause():
    global current_direction, paused
    if paused:
        paused = False
        current_direction = 'stop'
        paused_label.clear()
        # paused_label.write('Status: Running', align='left', font=('Courier', 20, 'normal'))

    else:
        paused = True
        current_direction = 'pause'
        paused_label.clear()
        paused_label.write('Paused', align='left', font=('Courier', 20, 'normal'))



main_window.listen()
main_window.onkeypress(change_direction_left, 'Left')
main_window.onkeypress(change_direction_right, 'Right')
main_window.onkeypress(change_direction_stop, 'Down')
main_window.onkey(change_direction_pause, 'space')

while True:
    main_window.update()

    if current_direction == 'pause':
        status = 'paused'
        continue

    if current_direction == 'left':
        x = actor.xcor()
        x -= 0.7
        if x < -270:
            x = -270
        actor.setx(x)
    if current_direction == 'right':
        x = actor.xcor()
        x += 0.7
        if x > 270:
            x = 270
        actor.setx(x)

    for red_element in red_list:
        y = red_element.ycor()
        y -= elements_speed * red_element.speed()
        red_element.sety(y)

        if y < -300:
            x = random.randint(-270, 270)
            red_element.goto(x, 270)

        if red_element.distance(actor) < 40:
            x = random.randint(-270, 270)
            red_element.goto(x, 270)
            score += 10
            pen.clear()
            pen.write('Your Score: {}, Lives: {} ,Level: {} '.format(score, attempts, level), align='center', font=font)

            # Check if the score increased by 200
            if score - last_speed_increase_score >= 200:
                level+=1
                elements_speed += 0.5
                last_speed_increase_score = score

    for black_element in black_list:
        y = black_element.ycor()
        y -= elements_speed * black_element.speed()
        black_element.sety(y)

        if y < -300:
            x = random.randint(-270, 270)
            black_element.goto(x, 270)

        if black_element.distance(actor) < 40:
            darken_background()
            restore_background()
            x = random.randint(-270, 270)
            black_element.goto(x, 270)
            score -= 10
            attempts -= 1
            if attempts < 1:
                main_window.bye()
                exit(0)
            pen.clear()
            pen.write('Your Score: {}, Lives: {} ,Level: {} '.format(score, attempts, level), align='center', font=font)

    for life_element in life_list:
        y = life_element.ycor()
        y -= 0.5 * life_element.speed()
        life_element.sety(y)

        if y < -300:
            x = random.randint(-270, 270)
            life_element.goto(x, 270)

        if life_element.distance(actor) < 40:
            x = random.randint(-270, 270)
            life_element.goto(x, 270)
            attempts += 1
            pen.clear()
            pen.write('Your Score: {}, Lives: {}'.format(score, attempts), align='center', font=font)
