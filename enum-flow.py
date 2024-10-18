from enum import Enum

#enum constants can only be strings and it should exactly match
class Color(Enum):
    RED =  "1"  #"red"
    GREEN = "2" # "green"
    BLUE =  "3" #"blue"

color = Color(input("enter you favourite color: 'red' 'green',blue': "))

match color:
    case Color.RED:
        print("I am Red")
    case Color.BLUE:
        print("I am Blue")
    case Color.GREEN:
        print("Iam green")



