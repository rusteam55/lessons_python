import time
from turtle import *


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        start_time = time.time()
        stop_time = time.time() + 60  # установили срок работы светофора в сек.
        light = 0
        t = Turtle()
        t.screen.setup(600, 600)
        t.hideturtle()
        t.speed(5)
        t.setheading(0)

        t.circle(50, 360)
        t.circle(-50, 540)
        t.circle(50, 360)
        t.up()
        t.home()
        t.down()

        # t.screen.mainloop()

        while stop_time > start_time:
            print(f'Светофор - {TrafficLight.__color[light]}')
            if light == 0:
                t.begin_fill()
                t.fillcolor('red')
                t.circle(50, 360)
                t.end_fill()
                time.sleep(7)
                t.begin_fill()
                t.fillcolor('white')
                t.circle(50, 360)
                t.end_fill()
                light += 1
            elif light == 1:
                t.begin_fill()
                t.fillcolor('yellow')
                t.circle(-50, 360)
                t.end_fill()
                time.sleep(2)
                t.begin_fill()
                t.fillcolor('white')
                t.circle(-50, 540)
                t.end_fill()
                light += 1
            elif light == 2:
                t.begin_fill()
                t.fillcolor('green')
                t.circle(50, 360)
                t.end_fill()
                time.sleep(7)
                t.begin_fill()
                t.fillcolor('white')
                t.circle(50, 360)
                t.end_fill()
                light += 1
            elif light == 3:
                t.begin_fill()
                t.fillcolor('yellow')
                t.circle(-50, 360)
                t.end_fill()
                time.sleep(2)
                t.begin_fill()
                t.fillcolor('white')
                t.circle(-50, 540)
                t.end_fill()
                light -= 3

            start_time = time.time()


t = TrafficLight()
t.running()
