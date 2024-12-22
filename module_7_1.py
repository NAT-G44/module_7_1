class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {line.split(', ')[0] for line in existing_products}

        for product in products:
            if product.name in existing_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\\n')
                print(f'Добавлен продукт: {product}')


if __name__ == '__main__':
    potato = Product('Potato', 50.0, 'Vegetables')
    tomato = Product('Tomato', 30.0, 'Vegetables')

    shop = Shop()

    shop.add(potato, tomato)

    shop.add(potato)

    print(shop.get_products())