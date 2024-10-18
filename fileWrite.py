#Create file in the current directory. File will be overwritten in w mode
#File will be appended in a mode
with open("pythonTest.txt",'a',encoding="utf-8") as f:
    f.write("Hare Krishna\n")
    f.write("Hare Rama")
