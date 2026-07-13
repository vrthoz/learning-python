print("CASHIER V3.0")

# Bundling the cashier system logic into a function
def start_cashier():
    cart = []
    item_dict = {
        "apple": 3000,
        "bread": 3500,
        "tea": 2500,
        "noodle": 1500,
        "detergent": 7500,
        "fried chicken": 5000,
        "chips": 7000
    }
    payment_total = 0

    while True: # Main loop
        items = input("Enter an item to buy, or type 'Checkout' to finish: ")
        if items.lower() in item_dict:
            cart.append(items)
            payment_total += item_dict[items.lower()]
        elif items.lower() == 'checkout':
            break
        else:
            print("Sorry, we don't sell those items!")

# Printing the receipt
    print("Here's all of the items that you've bought!")
    for total in cart:
        print(total)
    print(f"The total is: Rp {payment_total:,}")

    with open('receipt.txt', 'w') as file:
        file.write('Items:\n')
        for all_items in cart:
            file.write(f'{all_items}\n')
        file.write(f'Payment Total: {payment_total}')

start_cashier()

