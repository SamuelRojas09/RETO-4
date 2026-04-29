from typing import List


# ===================== CLASE BASE =====================
# Representa cualquier producto del menú
class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self._name = name    # Nombre del producto
        self._price = price  # Precio del producto

    # -------- GETTERS --------
    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    # -------- SETTERS --------
    def set_name(self, name: str) -> None:
        self._name = name

    def set_price(self, price: float) -> None:
        self._price = price

    # Método base que retorna el precio
    def calculate_total(self) -> float:
        return self._price


# ===================== SUBCLASSES =====================
class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str) -> None:
        super().__init__(name, price)
        self._size = size

    def get_size(self) -> str:
        return self._size

    def set_size(self, size: str) -> None:
        self._size = size


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, shareable: bool) -> None:
        super().__init__(name, price)
        self._shareable = shareable

    def get_shareable(self) -> bool:
        return self._shareable

    def set_shareable(self, value: bool) -> None:
        self._shareable = value


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, calories: int) -> None:
        super().__init__(name, price)
        self._calories = calories

    def get_calories(self) -> int:
        return self._calories

    def set_calories(self, calories: int) -> None:
        self._calories = calories


# ===================== ORDER =====================
class Order:
    def __init__(self) -> None:
        self._items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self._items.append(item)

    def show_order(self) -> None:
        print("\n--- ORDER ---")
        for item in self._items:
            print(f"{item.get_name()} -> ${item.get_price():.3f}")

    def calculate_subtotal(self) -> float:
        total = 0.0
        for item in self._items:
            total += item.calculate_total()
        return total

    def calculate_total(self) -> float:
        subtotal = self.calculate_subtotal()
        total = subtotal

        count = len(self._items)

        print("\n--- APPLYING DISCOUNTS ---")

        main_count = 0
        for item in self._items:
            if isinstance(item, MainCourse):
                main_count += 1

        if main_count >= 2:
            print("12% discount (2 or more main courses)")
            total = total * 0.88

        if count > 5:
            print("20% discount (more than 5 items)")
            total = total * 0.80

        elif count > 3:
            print("10% discount (more than 3 items)")
            total = total * 0.90

        if subtotal > 40:
            print("Extra 5% discount (subtotal > 40)")
            total = total * 0.95

        return total


# ===================== PAYMENT =====================
class Payment:
    def pay(self, amount: float) -> None:
        raise NotImplementedError


class Card(Payment):
    def __init__(self, number: str) -> None:
        self._number = number

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount:.3f} with card ****{self._number[-4:]}")


class Cash(Payment):
    def __init__(self, given: float) -> None:
        self._given = given

    def pay(self, amount: float) -> None:
        if self._given >= amount:
            change = self._given - amount
            print(f"Cash payment successful. Change: ${change:.3f}")
        else:
            print("Not enough money")


# ===================== MENU =====================
menu: List[MenuItem] = [
    Beverage("Water", 2.0, "Medium"),
    Beverage("Soda", 3.0, "Big"),
    Beverage("Juice", 4.0, "Medium"),
    Appetizer("Fries", 5.0, True),
    Appetizer("Nachos", 6.0, True),
    Appetizer("Onion rings", 5.5, True),
    MainCourse("Burger", 10.0, 800),
    MainCourse("Pizza", 12.0, 900),
    MainCourse("Pasta", 11.0, 700),
    MainCourse("Salad", 8.0, 400),
]


# ===================== TESTS =====================
if __name__ == "__main__":

    print("\n==============================")
    print("      TESTING RESTAURANT")
    print("==============================")

    # =====================
    # TEST 1: SMALL ORDER
    # =====================
    print("\n=== TEST 1: SMALL ORDER ===")
    order1 = Order()
    order1.add_item(menu[0])  # Water
    order1.add_item(menu[3])  # Fries

    order1.show_order()
    print("Subtotal:", f"{order1.calculate_subtotal():.3f}")
    total1 = order1.calculate_total()
    print("Total:", f"{total1:.3f}")

    # =====================
    # TEST 2: MEDIUM ORDER
    # =====================
    print("\n=== TEST 2: MEDIUM ORDER ===")
    order2 = Order()
    order2.add_item(menu[0])  # Water
    order2.add_item(menu[1])  # Soda
    order2.add_item(menu[3])  # Fries
    order2.add_item(menu[6])  # Burger

    order2.show_order()
    print("Subtotal:", f"{order2.calculate_subtotal():.3f}")
    total2 = order2.calculate_total()
    print("Total:", f"{total2:.3f}")


    # =====================
    # TEST 3: LARGE ORDER
    # =====================
    print("\n=== TEST 3: LARGE ORDER ===")
    order3 = Order()
    order3.add_item(menu[0])  # Water
    order3.add_item(menu[1])  # Soda
    order3.add_item(menu[3])  # Fries
    order3.add_item(menu[6])  # Burger
    order3.add_item(menu[7])  # Pizza
    order3.add_item(menu[4])  # Nachos

    order3.show_order()
    print("Subtotal:", f"{order3.calculate_subtotal():.3f}")
    total3 = order3.calculate_total()
    print("Total:", f"{total3:.3f}")


    # =====================
    # TEST 4: EXPENSIVE ORDER
    # =====================
    print("\n=== TEST 4: EXPENSIVE ORDER ===")
    order4 = Order()
    order4.add_item(menu[7])  # Pizza
    order4.add_item(menu[7])  # Pizza
    order4.add_item(menu[7])  # Pizza
    order4.add_item(menu[7])  # Pizza

    order4.show_order()
    print("Subtotal:", f"{order4.calculate_subtotal():.3f}")
    total4 = order4.calculate_total()
    print("Total:", f"{total4:.3f}")

    
    # =====================
    # TEST 5: PAYMENT
    # =====================
    print("\n=== TEST 5: PAYMENT ===")

    # Pago con tarjeta usando total de una orden
    payment1 = Card("1234567812345678")
    payment1.pay(total3)

    # Pago en efectivo suficiente
    payment2 = Cash(50)
    payment2.pay(total3)

    # Pago en efectivo
    payment3 = Cash(100)
    payment3.pay(total3)
    
    # =====================
    # TEST: SETTERS
    # =====================
    print("\n=== TEST 6: SETTERS ===")

    drink = Beverage("Soda", 3.0, "Small")
    print("Original :", drink.get_name(), f"{drink.get_price():.3f}", drink.get_size())

    # Cambios usando setters
    drink.set_size("Large")
    drink.set_price(4.5)
    drink.set_name("Big Soda")

    print("Updated :", drink.get_name(), f"{drink.get_price():.3f}", drink.get_size())

    print("\n==============================")
    print("        END OF TESTS")
    print("==============================")
