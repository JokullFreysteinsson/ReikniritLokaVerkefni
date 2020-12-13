#Hjólabúð
class Node:
    # Smiður, frumstillir d og núllstillir bendana prv og nxt
    def __init__(self, d, g):
        self.data = d
        self.girar = g
        self.prv = None
        self.nxt = None

    #Endurkvæmt fall sem bætir aftast á listann.
    def printList(self):
        if self.nxt is None:
            print(self.data, self.girar, end=" ")
        else:
            print(self.data, self.girar, end=" ")
            self.nxt.printList()

    #Endurkvæmt fall sem athugar hvort stak d er í listanum

    def findhjol(self, d):
        if self.nxt is None:
            if self.nxt == d:
                print(d)
            else:
                print("villa")
        else:
            self.nxt.find(d)

    def findgirar(self, g):
        if self.nxt is None:
            if self.nxt == g:
                print(g)
            else:
                print("villa")
        else:
            self.nxt.find(g)


class keyrsla:
    #smiður, núllstillir Haus listans
    def __init__(self):
        self.head = None

    #Bætir við fremst á listann, hnúturinn verður Head - förum ekki í Node klasann.
    def push(self, d, g):
        if self.head is None:       #Ef listinn er tómur
           self.head = Node(d, g)
        else:                       #Ef Listinn er ekki tómur
            n = Node(d, g)             #Býr til nýja node
            n.nxt = self.head
            self.head.prv = n
            self.head = n

    # Prentar listann allan á skjá - kallar á endurkvæmt fall í Node.
    def printList(self):
        if self.head is None:
            print("Listin er tómur ")
        else:
            self.head.printList()

    # Finnur stak d í ef til - kalla á endurknæmt fall í Node
    def findhjol(self, d):
        if self.head is None:
            print("Listinn er tómur ekker finnst")
        else:
            self.head.findhjol

    def findgirar(self, d):
        if self.head is None:
            print("Listinn er tómur ekker finnst")
        else:
            self.head.findgirar


# Keyrslurútína
dll = keyrsla()
dll.push("blát hjól", 10)
dll.push("grænt hjól", 8)
dll.push("rautt hjól", 5)
dll.push("gult hjól", 3)


dll.printList()
print(dll.findhjol("blát hjól"))
print(dll.findgirar(10))
