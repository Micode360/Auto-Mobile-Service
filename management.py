from file import File


class Management(File):
    def __init__(self):
        super().__init__()

    def load_net_worth(self):
        total_networth = 0
        cars = self.load_from_file('store/mobiles.json')
        for car in cars:
           price_per_quantity = int(car['price_per_car']) * int(car['quantity'])
           total_networth += price_per_quantity
        return f"Car Added. Your net worth is {total_networth}"
