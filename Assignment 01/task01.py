

def main():

    def checking(message="Too short"):
        print(message)

    while True:
        user_input = input("Write something (quit ends): ").strip()

        if user_input.lower() == "quit":
            break

        if len(user_input) < 10:
            checking() 
        else:
            checking(user_input)


    main()
