from faker import Faker
from faker.providers import BaseProvider
import random
import csv


# class CategoryProvider(BaseProvider):
#    def product_category(self):
#        cates = []
#        with open("D:/Codes/python/random_faker/faker_provider/product_category.csv", "r") as file:
#            reader = csv.reader(file, delimiter=',')
#            line_count = 0
#            for row in reader:
#                if line_count == 0:
#                    line_count += 1
#                else:
#                    cates.append(row[0])
#                    line_count += 1

#        return random.choice(cates)


class ColorProvider(BaseProvider):
    def color(self):
        return random.choice(["red", "white", "orange", "black", "green", "blue"])


class MaterialProvider(BaseProvider):
    def material(self):
        return random.choice(['plastic', 'inox', 'aluminum', 'gold', 'silver'])


fake = Faker()
fake.add_provider(ColorProvider)
fake.add_provider(MaterialProvider)


def random_int(a, b):
    return int(random.uniform(a, b))

# ONLY NEED 1-200


def create_uom():
    name = fake.name()
    seller_id = int(random.uniform(1, 200))

    return [name, seller_id]


def create_seller():
    name = fake.name()
    description = fake.text()
    phone = fake.phone_number()
    address = fake.street_address()

    return [name, description, phone, address]


def create_template():
    name = fake.name()
    description = fake.text()
    default_price = round(random.uniform(100, 1000), 2)
    remain_quantity = random_int(1, 100)
    sold_quantity = random_int(1, 100)
    rating = random_int(1, 5)
    number_rating = random_int(1, 1000)

    return [name, description, default_price, remain_quantity, sold_quantity, rating, number_rating]


def create_product():
    name = fake.name()
    template_id = random_int(1, 200)
    ori_price = round(random.uniform(100, 1000), 2)
    sale_price = round(random.uniform(100, 2000), 2)
    variants = fake.json(
        data_columns=[('Color', 'color'), ('Material', 'material')], num_rows=1)

    return [name, template_id, ori_price, sale_price, variants]


if __name__ == "__main__":
    # seller
    with open("seller_seed.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "description", "phone", "address"])
        seller_rows = []
        for i in range(0, 200):
            seller_rows.append(create_seller())

        writer.writerows(seller_rows)

    # template
    with open("template_seed.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "description", "default_price",
                        "remain_quantity", "sold_quantity", "rating", "number_rating"])
        for i in range(0, 200):
            writer.writerow(create_template())

    # products
    with open("product_seed.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["name", "template_id", "original_price", "sale_price", "variants"])
        for i in range(0, 200):
            writer.writerow(create_product())
