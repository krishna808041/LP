# Elementary Food Ordering Chatbot

cart = []
total = 0

menu = {
    "1": ("Pizza", 200),
    "2": ("Burger", 120),
    "3": ("Juice", 70)
}

print("Welcome to FoodieBot")
name = input("Enter your name: ")

while True:
    print("\n1.Menu  2.Order  3.Cart  4.Help  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        print("\n--- MENU ---")
        for key in menu:
            print(key, menu[key][0], "Rs.", menu[key][1])

    elif ch == "2":
        print("\n--- MENU ---")
        for key in menu:
            print(key, menu[key][0], "Rs.", menu[key][1])

        item_no = input("Enter item number: ")

        if item_no in menu:
            qty = int(input("Enter quantity: "))
            item, price = menu[item_no]
            amount = price * qty

            cart.append([item, qty, amount])
            total = total + amount

            print(item, "added to cart")
        else:
            print("Invalid item")

    elif ch == "3":
        if len(cart) == 0:
            print("Cart is empty")
        else:
            print("\n--- CART ---")
            for item in cart:
                print(item[0], "Qty:", item[1], "Amount:", item[2])
            print("Total Bill: Rs.", total)

            confirm = input("Confirm order? yes/no: ")

            if confirm == "yes":
                address = input("Enter address: ")
                print("Order placed successfully!")
                print("Delivery address:", address)
                print("Total Amount: Rs.", total)
            else:
                print("Order not confirmed")

    elif ch == "4":
        print("We provide food ordering service.")
        print("Payment: Cash/UPI")
        print("Delivery time: 30 minutes")

    elif ch == "5":
        print("Thank you", name)
        break

    else:
        print("Invalid choice")