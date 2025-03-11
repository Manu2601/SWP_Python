class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.next = None
    
    def setNextElement(self, nextElement):
        self.next = nextElement
    
    def getNextElement(self):
        return self.next
    
    def getObj(self):
        return self.obj