def tester(givenstring="Too short"):
    print(givenstring)

def main():
    while True:
        user_input = input("Write something (quit ends): ").strip()

        if user_input.lower() == "quit":
            break

        if len(user_input) < 10:
            tester()  # prints default "Too short"
        else:
            tester(user_input)  # prints the given input

    main()
