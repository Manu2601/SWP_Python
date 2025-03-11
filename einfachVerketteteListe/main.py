import random
import sys
from EinfachVerketteteListe import EinfachVerketteteListe

if __name__ == "__main__":
    try:
        testListe = EinfachVerketteteListe()
        for _ in range(6):
            testListe.addLast(random.randint(1, 10))
        
        print(testListe.getAllElements())
        print(testListe.getLength())
        
        testZahl = random.randint(1, 5)
        print(f"Delete {testZahl}")
        testListe.deleteElement(testZahl)
        print(testListe.getAllElements())
        print(testListe.getLength())
        
        for testElement in testListe:
            print(testElement)
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)
