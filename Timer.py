import time

class Timer:
    def __init__(self, interval):
        self.interval = interval
        self.start_time = time.time()

    def elapsed(self):
        elapsed = time.time() - self.start_time
        return elapsed > self.interval

    def reset(self):
        self.start_time = time.time()

timer_3_min = Timer(180)
timer_12_min = Timer(720)

while True:
    if timer_3_min.elapsed():
        print("3-minute timer has expired!")
        timer_3_min.reset()

    if timer_12_min.elapsed():
        print("12-minute timer has expired!")
        timer_12_min.reset()

