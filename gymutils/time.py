import time

class Timer:
    def __init__(self):
        self.reset()
    def reset(self):
        self.start = time.time()
    def get(self):
        return time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start))
