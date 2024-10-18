def parrot(voltage, state='a stiff', action='survive'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "live"}
parrot(**d) #unpack a dictionary and pass as argument list