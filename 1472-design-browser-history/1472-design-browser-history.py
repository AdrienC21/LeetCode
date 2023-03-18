class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.id = 0  # where we are in the history

    def visit(self, url: str) -> None:
        self.history[self.id+1:] = [url]  # clear forward history and add url
        self.id += 1

    def back(self, steps: int) -> str:
        self.id = max(0, self.id - steps)
        return self.history[self.id]

    def forward(self, steps: int) -> str:
        self.id = min(len(self.history) - 1, self.id + steps)
        return self.history[self.id]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)