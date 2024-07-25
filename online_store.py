from management import Management


# Multi level importation

class OnlineStore(Management):
    def __init__(self):
        super().__init__()
        self.inventory = self.load_from_file('store/mobiles.json')
        self.purchases = []

    def display_cars(self):
        if len(self.inventory) == 0:
            print("No cars available in the store.")
        else:
            for car in self.inventory:
                print(
                    "==" * 8,
                    f"name: {car['car_name']}",
                    f"model: {car['model']}",
                    f"color: {car['color']}",
                    f"price: {car['price_per_car']}",
                    "==" * 8,
                    sep="\n"
                )
    def update_inventory(self, car_name):
        for car in self.inventory:
            if car['car_name'] == car_name:
                str(int(car['quantity']) - 1)

    def purchase_car(self, car_name):
        for car in self.inventory:
            if car['car_name'] == car_name:
                username = input("Enter your name: ")
                confirmation = input(f"Are you sure you want to buy the {car_name} for {car['price_per_car']}? (yes/no): ")
                if confirmation.lower() == 'yes':
                    if car['quantity'] == "0":
                        self.inventory.remove(car)
                    purchase = {
                        'username': username,
                        'car_name': car_name,
                        'model': car['model'],
                        'color': car['color'],
                        'price': car['price_per_car']
                    }
                    self.purchases.append(purchase)
                    self.save_to_file(self.inventory, 'store/mobiles.json')
                    self.save_to_file(self.purchases, f'store/purchases.json')
                    print(f"Purchase successful! {car_name} has been bought by {username}.")
                    return
                else:
                    print("Purchase canceled.")
                    return
        print(f"{car_name} not found in the store.")

    def run_store(self):
        while True:
            command = input("\nEnter 'view' to see available cars\nEnter 'buy' to purchase a car\nEnter 'quit' to exit: ")
            if command == "view":
                self.display_cars()
            elif command == "buy":
                car_name = input("Enter the name of the car you want to buy: ")
                self.purchase_car(car_name)
            elif command == 'quit':
                print("Exiting the online store.")
                break
            else:
                print("Invalid command")

# Run the online store
online_store = OnlineStore()
online_store.run_store()