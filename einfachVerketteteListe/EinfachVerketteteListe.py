from ListElement import ListElement

class EinfachVerketteteListe:
    def __init__(self):
        self.startElement = None
        self.length = 0

    def addLast(self, obj):
        newElement = ListElement(obj)
        if not self.startElement:
            self.startElement = newElement
        else:
            lastElement = self.startElement
            while lastElement.getNextElement():
                lastElement = lastElement.getNextElement()
            lastElement.setNextElement(newElement)
        self.length += 1
    
    def getLength(self):
        return self.length

    def deleteElement(self, obj):
        currentElement = self.startElement
        previousElement = None
        while currentElement:
            if currentElement.getObj() == obj:
                if previousElement:
                    previousElement.setNextElement(currentElement.getNextElement())
                else:
                    self.startElement = currentElement.getNextElement()
                self.length -= 1
                return
            previousElement = currentElement
            currentElement = currentElement.getNextElement()
    
    def getAllElements(self):
        elements = []
        currentElement = self.startElement
        while currentElement:
            elements.append(currentElement.getObj())
            currentElement = currentElement.getNextElement()
        return elements
    
    def findElement(self, obj):
        currentElement = self.startElement
        while currentElement:
            if currentElement.getObj() == obj:
                return currentElement
            currentElement = currentElement.getNextElement()
        return None
    
    
    def __iter__(self):
        self.iterNode = self.startElement # Startet die Iteration beim ersten Element
        return self  # Initialisiert den Iterator und gibt das Iterator-Objekt zurück

    def __next__(self):
        if self.iterNode is None:
            raise StopIteration  # Stoppt die Iteration, wenn keine weiteren Elemente vorhanden sind
        obj = self.iterNode.getObj()
        self.iterNode = self.iterNode.getNextElement()
        return obj  # Gibt das aktuelle Element zurück und geht zum nächsten über