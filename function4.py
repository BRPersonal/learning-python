def concat(*args,sep="/"):
    return sep.join(args)

result = concat("earth","mars","venus")
print(result)
result = concat("earth","mars","venus","jupiter",sep=".")
print(result)

       