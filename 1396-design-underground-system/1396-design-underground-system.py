class UndergroundSystem:

    def __init__(self):
        self.travelling = {}
        self.travels = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if not(id in self.travelling):
            self.travelling[id] = {}
        self.travelling[id][stationName] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for station in self.travelling[id]:
            if not(station in self.travels):
                self.travels[station] = {}
            if not(stationName in self.travels[station]):
                self.travels[station][stationName] = []
            self.travels[station][stationName].append(t-self.travelling[id][station])
        self.travelling[id] = {}
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        L = self.travels[startStation][endStation]
        return (sum(L) / len(L))


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)