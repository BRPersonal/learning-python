def cheeseShop(kind,*args, **keywordArgs):
    print("--Do you have any ",kind,"?")
    print("--I am sorry we ran out of ",kind)
    for arg in args:
        print(arg)
    print("-" * 40) #print 40 dashes
    for kw in keywordArgs:
        print(kw,":",keywordArgs[kw])

#we can call the function like this
cheeseShop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
