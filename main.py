import random
class Student:

    def __init__(self, name):
        self.name = name
        self.age = 5
        self.profession = 0
        self.alive = True
        self.gladness = 52
    def to_study(self):
        print("Time to study")
        self.profession += 0.16
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.profession > -0.5:
            print("За це життя ти не став Кріштіану Роналду:(")
            self.alive = False

        elif self.gladness < 0 :
            print("Вась, ти депресія , Вась ти не крутий .")
            self.alive = False

        elif self.profession > 3.0:
            print("Вась, ти не крутий ")

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Profession = {round(self.profession,2)}")

    def live(self, day):
        day = 'day' + str(day) + "of" + self.name + "live"
        print(day)

        live_cube = random.randint(a=1, b=3)

        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)