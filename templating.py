from string import Template
import os.path 

photoFiles=["/tmp/img_1074.jpg","~/poc/python/img_1076.jpg","img_1077.png"]

#By default Template uses ${} to mark a variable.
#we can override it by creating a subclass
class CustomTemplate(Template):
    delimiter = "%"        #This is a joke of OOP. You directly access data. Python does not deserve to implement OOP

fmt=input("Enter a file rename format You can use %n for seq # and %f for fileType")
myTemplate = CustomTemplate(fmt)

for i,file in enumerate(photoFiles):
    base,ext = os.path.splitext(file)
    renamedFile = myTemplate.substitute(n=i,f=ext)
    print(f"i={i}, file={file}, base={base}, ext={ext}, renamedFile={renamedFile}")