print("CASHIER V1.0")

# Bundling the cashier system logic into a function
def start_cashier():
    cart = []

    while True: # Main loop
        items = input("Welcome! Enter an item to buy, or type 'Checkout' to finish: ")
        if items.lower() == "checkout":
            break
        elif items.isdigit(): # Precaution to prevent user from inputting a number
            print("Is there an item named after numbers?")
        else: # Appending together all the inputted items into the variable "cart"
            cart.append(items)

    print("Here's all of the items that you've bought!")
    for total in cart:
        print(total)

start_cashier()

