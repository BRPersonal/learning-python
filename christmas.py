def center_text(text:str,column_width:int) -> str:

    result = text
    length = len(text)

    if (column_width > length):
        filler_length = (column_width - length) // 2  #integer division
        result = "".ljust(filler_length) + text + "".rjust(filler_length)

    return result

def print_christmas_tree(height:int) -> None:
    column_width = 2 * height + 1
    for i in range(height):
        print(center_text("*" * (2 * i + 1), column_width))

    #display trunk    
    print(center_text("*",column_width))
    print(center_text("*",column_width))
    print(center_text("*",column_width))

#If this check is not there, then this code will execute even when
#this module is only imported in another module or imported in python shell
if (__name__ == "__main__"):    
    height = int(input("Enter height: "))
    print_christmas_tree(height)


    

