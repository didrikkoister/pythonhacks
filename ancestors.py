class person:
    def __init__(self):
        self.type = "unknown"
        self.myname = "unknown"
        self.myfather = None
        self.mymother = None

    def setName(self,n):
        self.myname=n

    def name(self):
        return self.myname

    def setFather(self,f):
        self.myfather=f

    def printancestory(self):
        if self.myfather != None:
            self.myfather.printancestory()
        print self.myname



didrik = person()

print didrik.name()

didrik.setName("Didrik")

print didrik.name()

dad=person()
dad.setName("skigod")
didrik.setFather(dad)
print "ANCESTRY"
didrik.printancestory()
