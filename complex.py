class Complex:
    #constructor First argument must be this pointer (self in python)
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def __str__(self):
        return str(self.r) + ("+" if self.i >= 0 else "") + str(self.i) + "i"

