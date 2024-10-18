#A function definition
def http_error(status):
    match status:
        case "400":
            return "Bad request"
        case "401" | "403" | "404":
            return "Not Allowed"
        case "418":
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
status = input("enter http status:")
error=http_error(status)
print(error)


