#Create a sample collection - It is a key value pair
users = {
            "Hans" : "active", 
            "Éléonore" : "inactive", 
            "太郎" : "active"
        }

print("Original:\n",users)

#iterate over copy of the collection and modify the original collection
#create new collection with only inactive users
inactive_users = {}
for user,status in users.copy().items():
    if (status == "inactive"):
        inactive_users[user] = status
        del users[user]
        

print("Active users:\n",users)
print("Inactive users:\n", inactive_users)

