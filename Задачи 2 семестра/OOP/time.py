class Time:
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def show(self):
        if self.minute < 10 and self.hour < 10:
            return f"0{self.hour}:0{self.minute}"
        if self.minute > 10 and self.hour < 10:
            return f"0{self.hour}:{self.minute}"
        if self.minute > 10 and self.hour > 10:
            return f"{self.hour}:{self.minute}"

    def isDay(self):
        if self.hour >= 12 and self.hour < 18:
            return True
        else:
            return False

    def isMorning(self):
        if self.hour >= 6 and self.hour < 12:
            return True
        else:
            return False

    def isEvening(self):
        if self.hour >= 18 and self.hour < 24:
            return True
        else:
            return False

    def isNight(self):
        if self.hour < 6:
            return True
        else:
            return False

    def sayHello(self):
        if self.isDay():
            print("Добрый день!")
        if self.isMorning():
            print("Доброе утро!")
        if self.isEvening():
            print("Добрый вечер :)")
        if self.isNight():
            print("Доброй ночи~")

    def add(self, a):
        self.minute = self.minute + a
        remainder = self.minute // 60
        if remainder > 0:
            self.hour = self.hour + remainder
            self.minute = self.minute - remainder * 60


t1 = Time("06", 45)
t2 = Time(3, "24")
print(t1.show())
print(t1.isDay())
print(t1.isNight())
print(t2.isNight())
print(t1.isMorning())
t2.sayHello()
t1.add(122)
print(t1.show())
