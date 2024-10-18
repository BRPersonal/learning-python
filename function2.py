def ask_ok(prompt,retries=4,exhaustMessage="Please Try again later"):
    while True:
        reply = input(prompt)
        if reply in {'y','yes','ye','yup'}:
            return True
        elif reply in {'n','no','nope'}:
            return False
        retries = retries - 1
        if (retries <= 0):
            print("Invalid user response")
            return False
        print(exhaustMessage)

ask_ok("Do you really want to quit?")


