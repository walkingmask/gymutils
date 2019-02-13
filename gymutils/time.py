from datetime import datetime
import time


class Timer:
    def __init__(self):
        self.reset()
    def reset(self):
        self.start = time.time()
    def get(self):
        return time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start))


def get_now_str(year=True, month=True, day=True,
        hour=True, minute=True, second=False, micro=False):
    want = "%Y" if year else ""
    want += "%m" if month else ""
    want += "%d" if day else ""
    want += "%H" if hour else ""
    want += "%M" if minute else ""
    want += "%S" if second else ""
    want += "%f" if micro else ""
    return datetime.now().strftime(want)
