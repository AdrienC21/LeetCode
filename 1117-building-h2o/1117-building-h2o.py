import threading
class H2O:
    def __init__(self):
        self.lock = threading.Lock()  # lock
        # number oxygen and hydrogen
        self.nbH = 0
        self.nbO = 0
        # functions
        self.releaseHydrogen = None
        self.releaseOxygen = None


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.lock:
            self.releaseHydrogen = releaseHydrogen
            self.nbH += 1
            self.molecule()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.lock:
            self.releaseOxygen = releaseOxygen
            self.nbO += 1
            self.molecule()
    def molecule(self) -> None:
        while (self.nbH >= 2) and (self.nbO >= 1):
            self.nbH -= 2
            self.nbO -= 1
            # H20
            self.releaseHydrogen()
            self.releaseHydrogen()
            self.releaseOxygen()