class Category:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = (name, price)
        self.items.append(item)

    def get_items(self):
        return self.items

    def get_harga_item(self, nama_item):
        return daftar_harga.get(nama_item)


food_category = Category("Food")
food_category.add_item("Mie", 5000)
food_category.add_item("Tempe", 3000)
food_category.add_item("Tahu", 2000)
food_category.add_item("Telur", 2500)
food_category.add_item("Oncom", 3000)

toys_category = Category("Toys")
toys_category.add_item("Mobil", 100000)
toys_category.add_item("Motor", 50000)
toys_category.add_item("Pesawat", 150000)

toiletries_category = Category("Toileteries")
toiletries_category.add_item("Pasta Gigi", 15000)
toiletries_category.add_item("Sabun", 4000)
toiletries_category.add_item("Shampoo", 10000)
toiletries_category.add_item("Pelembab", 8000)

beverages_category = Category("Beverages")
beverages_category.add_item("Air Mineral", 3000)
beverages_category.add_item("Jus", 5000)
beverages_category.add_item("Kopi", 7000)
beverages_category.add_item("Teh", 4000)

electricals_category = Category("Electricals")
electricals_category.add_item("Charger", 50000)
electricals_category.add_item("Bohlam", 10000)
electricals_category.add_item("Kipas Angin", 100000)

clothing_category = Category("Clothing")
clothing_category.add_item("Kaos", 30000)
clothing_category.add_item("Jeans", 150000)
clothing_category.add_item("Mukena", 200000)
clothing_category.add_item("Sepatu", 100000)