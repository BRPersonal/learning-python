#Create a set. A set will keep only unique items
basket={"apple","orange","banana","apple","pear","orange"}
print(basket)
print("lenth=",len(basket))
print("orange" in basket)

#create a set from unique letters
a = set("abracadabra")
b = set("alacazam")

print("a=",a)
print("b=",b)
print("letters in a but not in b:",a - b)
print("letters in a or b or both", a | b)
print("letters in both a and b", a & b)
print("letters in a or b but not both", a ^ b)

#set comprehensions are also supported
a = {x for x in "abracadabra" if x not in "abc"}
print(a)


