# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []  # list of nested iterator
        self.i = -1
        non_empty_nested_list = []  # filter empty lists and cases such that [[]] ...
        for ni in nestedList:
            if ni.isInteger() or not(self.is_empty(ni.getList())):
                non_empty_nested_list.append(ni)
        self.nestedList = non_empty_nested_list
        self.lenNestedList = len(self.nestedList)
    
    def is_empty(self, nestedList):
        if nestedList:
            for x in nestedList:
                if x.isInteger() or not(self.is_empty(x.getList())):
                    return False
        return True

    def next(self) -> int:
        while self.stack:  # if an iterator is in the stack, get the next element
            if self.stack[-1].hasNext():
                return self.stack[-1].next()
            self.stack.pop()  # iterator done, remove it
        self.i += 1  # else, increase the pointer and search for an integer or then, a nested list
        if self.nestedList[self.i].isInteger():
            return self.nestedList[self.i].getInteger()
        while True:  # continue these step until we have a non empty nested list or an integer
            if self.nestedList[self.i].getList():
                self.stack.append(NestedIterator(self.nestedList[self.i].getList()))
                return self.stack[-1].next()
            # else it is an empty nested list
            self.i += 1
            if self.nestedList[self.i].isInteger():
                return self.nestedList[self.i].getInteger()

    def hasNext(self) -> bool:
        for j in range(len(self.stack)-1, -1, -1):
            if self.stack[j].hasNext():  # one of the iterator still has an item
                return True
        return (self.i < (self.lenNestedList - 1))


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())