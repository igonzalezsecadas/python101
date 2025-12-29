products = {"Table": 300, "Chair": 150, "Computer": 800, "Mouse": 30, "Keyboard": 40, "Router": 100}
cart = []

def main():
    print("--------------------------------\nAvailable products: ")
    for product in products.keys():
        print(f"{product} -> {products.get(product)}€")
    print("--------------------------------")

    option = 0
    while option != 4:
        option = int(input("""Select an option:
    1 - Add product to cart
    2 - Remove product from cart
    3 - Get total price from cart
    4 - Exit program
--------------------------------
"""))

        match option:
            case 1:
                add_product()
            case 2:
                remove_product()
            case 3:
                get_total()
            case 4:
                break
            case _:
                print("Invalid operation")


def add_product():
    product = input("Input the name of the product you want to add: ")
    if product in products.keys():
        cart.append(product)
        print(f"{product} added to cart")
    else:
        print("Invalid product")

def remove_product():
    product = input("Input the product you want to remove from the cart: ")
    if product in cart:
        cart.remove(product)
        print(f"{product} succesfully removed")
    else:
        print(f"{product} isn't in the cart")

def get_total():
    total = 0
    for product in cart:
        total += products.get(product)
    print(f"The total price of the cart is: {total}€")


main()