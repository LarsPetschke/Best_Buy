import products
import store

def start(best_buy: store.Store):
    while True:
        print("\n   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            # aktive Produkte anzeigen
            for p in best_buy.get_all_products():
                p.show()

        elif choice == "2":
            print(f"Total amount in store: {best_buy.get_total_quantity()}")

        elif choice == "3":
            make_order(best_buy)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


def make_order(best_buy: store.Store):
    print("------")
    products_active = best_buy.get_all_products()

    for i, p in enumerate(products_active, start=1):
        print(f"{i}. ", end="")
        p.show()

    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        product_number = input("Which product # do you want? ")

        if product_number == "":
            break

        try:
            index = int(product_number) - 1
            product = products_active[index]
        except:
            print("Invalid product number.")
            continue

        amount = int(input("What amount do you want? "))

        shopping_list.append((product, amount))
        print("Product added to list!")

    total_price = best_buy.order(shopping_list)
    print(f"Order completed! Total cost: {total_price}")


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
