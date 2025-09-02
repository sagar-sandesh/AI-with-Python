def main():
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_amount = 0

    print("Supermarket")
    print("===========")

    while True:
        try:
            choice = int(input("Please select product (1-10) 0 to Quit: "))
            if choice == 0:
                break
            elif 1 <= choice <= 10:
                price = prices[choice - 1]
                total_amount += price
                print(f"Product: {choice} Price: {price}")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

    print(f"Total: {total_amount}")
    payment = int(input("Payment: "))
    change = payment - total_amount
    print(f"Change: {change}")

    main()
