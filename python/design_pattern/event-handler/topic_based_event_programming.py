import itertools
from blinker import signal


class SelfWatch:
    _new_id = itertools.count(1)

    def __init__(self):
        self._id = next(self._new_id)
        init_signal = signal(f"SelfWatch.init")
        init_signal.send(self)
        init_signal.connect(self.receiver)
        self.init_signal = init_signal
    
    def receiver(self, sender):
        print(f"{self}: received event from {sender}")
    
    def __str__(self):
        return f"{self.__class__.__name__}({self._id})"


if __name__ == "__main__":
    sw = SelfWatch()
    sw2 = SelfWatch()
    sw3 = SelfWatch()
