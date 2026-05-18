# ============================================================
# Elementary Chatbot for Food Ordering Customer Interaction
# ============================================================

name = ""
cart = []
total = 0

menu = {
    "1": ("Pizza", 200),
    "2": ("Burger", 120),
    "3": ("Sandwich", 100),
    "4": ("Mango Juice", 70),
    "5": ("Apple Juice", 80)
}


def welcome():
    print("====================================")
    print("     Welcome to FoodieBot")
    print("====================================")
    print("Bot: I can help you order food.")
    print("Bot: You can ask about menu, order, cart, payment, delivery or support.")
    print("Bot: Type 'bye' to exit.\n")


def get_info():
    global name
    name = input("Bot: May I know your name?\nYou: ")
    print("Bot: Hello", name + "! Nice to meet you.\n")


def show_menu():
    print("\n---------- MENU ----------")
    for key, value in menu.items():
        print(key + ".", value[0], "- Rs.", value[1])
    print("--------------------------\n")


def add_order():
    global total

    show_menu()

    while True:
        choice = input("Bot: Enter item number or type 'done':\nYou: ")

        if choice.lower() == "done":
            break

        if choice in menu:
            item, price = menu[choice]
            qty = int(input("Bot: Enter quantity:\nYou: "))

            amount = price * qty
            cart.append([item, price, qty, amount])
            total += amount

            print("Bot:", item, "added to cart. Amount = Rs.", amount)
        else:
            print("Bot: Invalid item number.")

    if len(cart) > 0:
        confirm_order()
    else:
        print("Bot: Cart is empty.")


def view_cart():
    if len(cart) == 0:
        print("Bot: Your cart is empty.")
        return

    print("\n---------- CART ----------")
    for item in cart:
        print("Item:", item[0])
        print("Price: Rs.", item[1])
        print("Quantity:", item[2])
        print("Amount: Rs.", item[3])
        print("--------------------------")

    print("Total Bill: Rs.", total)


def confirm_order():
    view_cart()

    address = input("\nBot: Enter delivery address:\nYou: ")
    mobile = input("Bot: Enter mobile number:\nYou: ")

    print("\nPayment Modes:")
    print("1. Cash on Delivery")
    print("2. UPI")
    print("3. Card")

    pay = input("Bot: Choose payment mode:\nYou: ")

    if pay == "1":
        payment = "Cash on Delivery"
    elif pay == "2":
        payment = "UPI"
    elif pay == "3":
        payment = "Card"
    else:
        payment = "Cash on Delivery"

    print("\n---------- ORDER SUMMARY ----------")
    print("Customer Name:", name)
    print("Mobile Number:", mobile)
    print("Address:", address)
    print("Payment Mode:", payment)
    print("Total Amount: Rs.", total)
    print("-----------------------------------")

    confirm = input("Bot: Press 1 to confirm order or 0 to cancel:\nYou: ")

    if confirm == "1":
        print("Bot: Your order is placed successfully!")
        print("Bot: Delivery will take 30 to 45 minutes.")
    else:
        print("Bot: Your order is cancelled.")


def payment_info():
    print("Bot: We accept Cash on Delivery, UPI and Card payments.")


def delivery_info():
    print("Bot: Delivery usually takes 30 to 45 minutes.")


def support_info():
    print("Bot: Contact support at support@foodiebot.com or call 9876543210.")


def chatbot():
    welcome()
    get_info()

    while True:
        print("\nWhat do you want to do?")
        print("1. Menu")
        print("2. Order")
        print("3. Cart")
        print("4. Payment Info")
        print("5. Delivery Info")
        print("6. Support")
        print("7. Exit")

        user = input("You: ").lower()

        if user == "1" or "menu" in user:
            show_menu()

        elif user == "2" or "order" in user:
            add_order()

        elif user == "3" or "cart" in user:
            view_cart()

        elif user == "4" or "payment" in user:
            payment_info()

        elif user == "5" or "delivery" in user:
            delivery_info()

        elif user == "6" or "support" in user or "help" in user:
            support_info()

        elif user == "7" or "bye" in user or "exit" in user:
            print("Bot: Thank you for visiting FoodieBot. Have a nice day,", name + "!")
            break

        else:
            print("Bot: Sorry, I did not understand.")


chatbot()