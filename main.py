from management import Management


class Automobile(Management):
    def __init__(self, name, founded, ceo):
        super().__init__()
        self.store = self.load_from_file('store/mobiles.json')
        self.net_worth = self.load_net_worth()
        self.name = name
        self.founded = founded
        self.ceo = ceo

    def add_a_car(self, car_name, model, color, price_per_car="0", quantity="0"):
        self.store.append({
            "car_name": car_name,
            "model": model,
            "color": color,
            "price_per_car": price_per_car,
            "quantity": quantity
        })

    def view_cars(self):
        if len(self.store) == 0:
            print("No cars in the store")
        else:
            for car in self.store:
                print(
                    "==" * 8,
                    f"name: {car['car_name']}",
                    f"model: {car['model']}",
                    f"color: {car['color']}",
                    f"price_per_car: {car['price_per_car']}",
                    f"quantity: {car['quantity']}",
                    "==" * 8,
                    sep="\n"
                )

    def show_net_worth(self):
        self.load_net_worth()

    def delete_car(self, name):
        for car in self.store:
            if car['car_name'] == name:
                self.store.remove(car)
                self.save_to_file(self.store, 'store/mobiles.json')
                print(f"{name} has been deleted.")
                return
        print(f"{name} not found.")

    def company_info(self):
        print(
                    "==" * 8,
                    f"Name of company: {self.name}",
                    f"Description: An auto mobile company.",
                    f"Founded: {self.founded}",
                    f"CEO: {self.ceo}",
                    "==" * 8,
                    sep="\n"
        )
    
    def run_company(self):
        while True:
            command = input("\nEnter 'add' to add a car\nEnter'view' to see cars\nEnter 'delete' to delete a car\nEnter 'quit' to exit: ")
            if command == "add":
                car_name = input("What is the name of the car: ")
                model = input("What is the model: ")
                color = input("What is the color of the car: ")
                price_per_car = input("What is the price for one car: ")
                quantity = input("How many cars are coming in?: ")

                # Add car to list
                self.add_a_car(car_name, model, color, price_per_car, quantity)

                # Save car to dictionary
                self.save_to_file(self.store, 'store/mobiles.json')
                
                print(self.load_net_worth())

            elif command == "view":
                view_command = input("Type (1) to view cars.\nType (2) to view net worth\nType (3) to view company information: ")
                if view_command == "1":
                    self.view_cars()
                elif view_command == "2":
                    print(self.load_net_worth())
                elif view_command == "3":
                    self.company_info()
                else:
                    print("Invalid command")
            elif command == "delete":
                car_name = input("Enter the name of the car to delete: ")
                self.delete_car(car_name)
            elif command == 'quit':
                print(f"Your net worth is {self.net_worth}. Thank you for your services")
                break
            else:
                print("Invalid command")

uni_global = Automobile("Uni Global", "2005", "Mr. Kayode")

uni_global.run_company()