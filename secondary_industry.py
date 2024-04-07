import time


class Secondary():
    def __init__(self, product, ingredients, recipes):
        self.state = False
        self.product = product
        self.production_rate = 1
        self.request_pending = 0
        self.temp_store = {n: 0 for n in ingredients}
        self.recipes = recipes

    def prod_setup(self, pending):
        required = []
        self.request_pending = pending
        for key, value in self.temp_store.items():
            if value < self.recipes[key] * pending:
                required.append([key, value - self.recipes[key] * pending])
        return required

    def prod(self, pending):
        self.state = True
        self.request_pending = pending
        for i in range(pending):
            time.sleep(0.1)
            for key, val in self.recipes.items():
                self.temp_store[key] -= val
            yield [self.product, self.production_rate]
            self.request_pending -= 1
        self.state = False
        self.request_pending = 0

    def __str__(self):
        return self.product


copper_wires = Secondary("copper_wires", ["copper", "energy"], {"copper": 1, "energy": 1})
fuel = Secondary("fuel", ["oil"], {"oil": 1})
plastic = Secondary("plastic", ["oil", "energy"], {"oil": 1, "energy": 1})
circuitry = Secondary("circuitry", ["rem", "plastic","energy"], {"rem": 1, "plastic": 1, "energy": 1})
steel = Secondary("steel", ["fuel", "iron", "energy"], {"fuel": 1, "iron": 1, "energy": 1})
