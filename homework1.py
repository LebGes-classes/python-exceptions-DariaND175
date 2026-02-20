import random

class Product:

    """Класс для карточки товара"""

    all_article = set()

    def __init__(
            self,
            name: str = 'Нет названия',
            count: int = 0,
            manufacturer: str = None,
            cost: int = 0,
            region: int = 0,
            category: str = None,
            description: str = None,
            characteristic: str = None,
            weight: int = 0,
            article_number: int = 0,
            color: str = None
    ) -> None:
        
        """Инициализатор класса.

        Args:
            name: Наименование товара
            count: Количество товара
            manufacturer: Производитель товара
            cost: Стоимость товара
            region: Регион, из которого доставляется товар
            category: Категория товара
            description: Описание товара
            characteristic: Характеристика товара
            weight: Вес товара(в кг)
            article_number: Артикул товара
            color: Цвет товара
        """

        self.__name = name
        self.__count = count
        self.__manufacturer = manufacturer
        self.__cost = cost
        self.__region = region
        self.__category = category
        self.__description = description
        self.__characteristic = characteristic
        self.__weight = weight
        self.__article_number = article_number
        self.__color = color

    def set_name(self, name: str) -> None:
        """ Сеттер для названия товара

        Args:
            name: Наименование товара
        """

        if len(name) == 0:
            print('Введите название товара.')

            self.__name = None
        else:
            self.__name = name

    def set_count(self,count) -> None:
        """ Сеттер для количества товара

        Args:
            count: Количество товара
        """

        try:
            count = int(count)
            if count <= 0:
                print('Введите положительное число.')

                self.__count = 0
            elif count > 10 ** 4:
                print('Введено слишком большое число.')

                self.__count = 0
            else:
                self.__count = count
        except ValueError:
            print('Ошибка. Введите корректное количество товара')

            self.__count = 0
        except TypeError:
            print('Ошибка типа данных.')

            self.__count = None

    def set_manufacturer(self, manufacturer: str) -> None:
        """ Сеттер для информации о производителе товара.

        Args:
            manufacturer: Производитель товара
        """

        if len(manufacturer) > 15:
            print('Имя производителя не должно превышать 14 символов.')

            self.__manufacturer = None
        else:
            self.__manufacturer = manufacturer

            print(f'Имя производителя изменено на {self.__manufacturer}')

    def set_cost(self, cost) -> None:
        """ Сеттер для информации о стоимости товара.

        Args:
            cost: Стоимость товара
        """

        try:
            num = float(cost)

            if num != int(num):
                print('Цена должна быть целым числом.')

                self.__cost = 0
                return

            cost = int(cost)

            if cost <= 0:
                print('Пожалуйста, введите положительное число.')

                self.__cost = 0
            elif cost >10**7:
                print('Введена слишком большая цена.')

                self.__cost = 0
            else:
                self.__cost = cost
        except ValueError:
            print('Ошибка.Можно использовать только цифры.')

            self.__cost = 0
        except TypeError:
            print('Ошибка типа данных.')

            self.__cost = 0


    def set_region(self,region) -> None:
        """Сеттер для региона доставки товара

        Args:
            region: Регион, из которого доставляется товар
        """

        try:
            region = int(region)
            if  1 <= region <= 99 or region == 100:
                self.__region = region
            else:
                print('Ошибка! Код региона должен быть от 1 до 99 (или 100- зарубежная доставка)')

                self.__region = 0
        except ValueError:
            print('Введите корректное число.')
            self.__region = 0
        except TypeError:
            print('Ошибка типа данных.')
            self.__region = 0

    def set_category(self, category: str) -> None:
        """Сеттер для региона доставки товара

        Args:
            category: Категория товара
        """

        try:
            if category and category.replace(' ','').isalpha():
             self.__category = category
            else:
                print('Категория не добавлена. Можно использовать только буквы.')

                self.__category = None
        except AttributeError:
            print('Объект не имеет метода replace/isalpha.')

            self.__category = None
        except TypeError:
            print('Ошибка типа данных.')

            self.__category = None


    def set_description(self,description: str) -> None:
        """Сеттер для описания товара.

        Args:
            description: Описание товара.
        """

        try:
            if description is None or len(description.strip()) == 0:
                print('У товара отсутствует описание.')

                self.__description = None
            elif len(description) <= 10**4:
                self.__description = description
            else:
                print('Описание не должно содержать больше 10.000 символов.')

                self.__description = None
        except TypeError:
            print('Ошибка! Можно вводить только текст.')

            self.__description = None

    def set_characteristic(self, characteristic: str) -> None:
        """Сеттер для региона доставки товара.

        Args:
            characteristic: Характеристика товара.
        """

        try:
            if characteristic is None or len(characteristic.strip()) == 0:
                print('У товара отсутствует характеристика.')

                self.__characteristic = None
            elif len(characteristic) <= 10**4:
                self.__characteristic = characteristic
            else:
                print('Характеристика не должна содержать больше 10.000 символов.')

                self.__characteristic = None
        except TypeError:
            print('Ошибка! Можно вводить только текст.')
            self.__characteristic = None

    def set_weight(self, weight) -> None:
        """Сеттер для региона доставки товара.

        Args:
            weight: Вес товара(в кг).
        """

        try:
            weight = float(weight)

            if weight > 1000:
                print('Введен слишком большой вес.')

                self.__weight = 0
            elif weight < 0:
                print('Вес не может быть отрицательным.')

                self.__weight = 0
            else:
                self.__weight = weight
        except TypeError:
            print('Ошибка типа данных.')

            self.__weight = 0
        except ValueError:
            print('Вводить можно только числа.')

            self.__weight = 0

    def set_article_number(self, article_number) -> None:
        """Сеттер для региона доставки товара.

        Args:
            article_number: Артикул товара.
        """

        if article_number is None:
            random_art = random.randint(10000000, 99999999)

            while random_art in Product.all_article:

                random_art += 1

                if random_art > 99999999:
                        random_art = 10000000

            self.__article_number = random_art

            Product.all_article.add(random_art)

            return

        else:
            try:
                article_number = int(article_number)
                if article_number in Product.all_article:
                    print('Такой артикул уже существует.')

                    self.__article_number = None
                elif len(str(article_number)) == 8:
                    self.__article_number = article_number

                    Product.all_article.add(article_number)
                else:
                    print('Артикул должен состоять из 8 цифр!')

                    self.__article_number = None
            except TypeError:
                print('Ошибка типа данных.')

                self.__article_number = None
            except ValueError:
                print('Некорректное значение.')

                self.__article_number = None

    def set_color(self,color):
        """Сеттер для региона доставки товара

        Args:
            color: Цвет товара."""

        colors = ('Красный', 'Жёлтый','Зелёный','Оранжевый','Синий','Голубой','Фиолетовый')

        if color.capitalize() in colors:
            self.__color = color.capitalize()
        else:
            self.__color = 'Другое'

    def get_name(self) -> str:
        """Геттер для наименования товара.

        Returns:
                name: Наименование товара
        """

        return self.__name

    def get_count(self) -> int:
        """Геттер для количества товара.

        Returns:
                count: Количество товара
        """

        return self.__count

    def get_manufacturer(self) -> str:
        """Геттер для производителя товара.

        Returns:
                manufacturer: Производитель товара
        """

        return self.__manufacturer

    def get_cost(self) -> int:
        """Геттер для стоимости товара.

        Returns:
                manufacturer: Стоимость товара
        """

        return self.__cost

    def get_region(self) -> int:
        """Геттер для региона, из которого доставляется товар.

        Returns:
                region: Регион, из которого доставляется товар.
        """

        return self.__region

    def get_category(self) -> str:
        """Геттер для категории товара.

        Returns:
                category: Категория товара.
        """

        return self.__category

    def get_description(self) -> str:
        """Геттер для описания товара.

        Returns:
                description: Описание товара.
        """

        return self.__description

    def get_characteristic(self) -> str:
        """Геттер для характеристики товара.

        Returns:
                characteristic: Характеристика товара.
        """

        return self.__characteristic

    def get_weight(self) -> float:
        """Геттер для веса товара.

        Returns:
                weight: Вес товара(в кг).
        """

        return self.__weight

    def get_article_number(self) -> int:
        """Геттер для веса товара.

        Returns:
                weight: Вес товара(в кг).
        """

        return self.__article_number

    def get_color(self) -> str:
        """Геттер для веса товара.

        Returns:
                color: Цвет товара.
        """

        return self.__color

    def condition_product(self) -> None:
        """Состояние товара."""

        if self.get_count() == 0:
            print(f'Товара {self.get_name()} нет в наличии.')
        elif self.get_count() <= 10:
            print(f'Внимание! Товара {self.get_name()} осталось в наличии {self.get_count()} штук.')
        else:
            print(f'Товар {self.get_name()} есть в наличии (осталось {self.get_count()} штук) ')

    def delete_product(self):
        """Удаление карточки товара."""

        self.__name = None
        self.__count = 0
        self.__manufacturer = None
        self.__cost = 0
        self.__region = 0
        self.__category = None
        self.__description = None
        self.__characteristic = None
        self.__weight = 0
        self.__article_number = 0
        self.__color = None


    def reduce_count(self,number_reduction) -> None:
        """Уменьшить количество товара.

        Args:
             number_reduction: число, на которое нужно уменьшить количество товара.
        """

        try:
            number_reduction = int(number_reduction)

            if number_reduction <= 0 or number_reduction > self.get_count():
                print('Ошибка. Количество товара не может быть уменьшено на это число.')
            else:
                new_count = self.get_count() - number_reduction

                self.set_count(new_count)
        except ValueError:
            print('Введите корректное число.')
        except TypeError:
            print('Ошибка типа данных.')

        finally:
            print(f'Текущее количество товара: {self.get_count()}')

    def increase_count(self,number_increase) -> None:
        """Увеличить количество товара.

        Args:
             number_increase: число, на которое нужно увеличить количество товара.
        """

        try:
            number_increase = int(number_increase)

            if number_increase <= 0:
                print('Ошибка. Количество товара может быть увеличено только на положительное число.')
            elif number_increase > 10 ** 5:
                print('Ошибка. Слишком большое значение.')
            else:
                new_count = self.get_count() + number_increase
                self.set_count(new_count)
        except ValueError:
            print('Введите корректное число.')
        except TypeError:
            print('Ошибка типа данных.')

        finally:
            print(f'Текущее количество товара: {self.get_count()}')


    def type_of_delivery(self) -> None:
        """Тип доставки."""

        if self.get_region() == 100:
            print('Зарубежная доставка.')
        elif self.get_region() is None:
            print('Тип доставки не указан.')
        elif 0 < self.get_region() < 100:
            print('Доставка по России.')
        else:
            print(f'Неизвестный код региона: {self.get_region()}')

    def display_information(self) -> None:
        """Вывод информации о товаре."""

        print(f' Наименование товара: {self.get_name()}')
        print(f' Количество товара: {self.get_count()}')
        print(f' Производитель товара: {self.get_manufacturer()}')
        print(f' Стоимость товара: {self.get_cost()}')
        print(f' Регион, из которого доставляется товар: {self.get_region()}')
        print(f' Категория товара: {self.get_category()}')
        print(f' Описание товара: {self.get_description()}')
        print(f' Характеристика товара: {self.get_characteristic()}')
        print(f' Вес товара(в кг) товара: {self.get_weight()}')
        print(f' Артикул товара: {self.get_article_number()}')
        print(f' Цвет товара: {self.get_color()}')

    def menu(self):
        """Меню программы."""

        job = True

        while job:

            print("=" * 30)
            print("""
                        MENU
            1. Показать информацию по товару.
            2. Увеличить количество товара.
            3. Уменьшить количество товара.
            4. Проверить наличие товара.
            5. Удалить информацию о товаре.
            6. Тип доставки.
            7. Выход из программы.
            8. Изменить информацию о товаре.
            """)

            try:
                choice = int(input("Выберите задачу..."))

                match choice:
                    case 1:
                        self.display_information()

                        input("\nНажмите Enter для продолжения...")
                    case 2:
                        number_increase = input("Введите число, на которое нужно увеличить товар.")

                        self.increase_count(number_increase)

                        input("\nНажмите Enter для продолжения...")
                    case 3:
                        number_reduction = input("Введите число, на которое нужно уменьшить товар.")

                        self.reduce_count(number_reduction)

                        input("\nНажмите Enter для продолжения...")
                    case 4:
                        self.condition_product()

                        input("\nНажмите Enter для продолжения...")
                    case 5:
                        self.delete_product()

                        input("\nНажмите Enter для продолжения...")
                    case 6:
                        self.type_of_delivery()

                        input("\nНажмите Enter для продолжения...")
                    case 7:
                        job = False
                    case 8:
                        try:
                            parameter = int(input("""Выберите параметр, который вы хотите изменить:
                            1. Имя товара
                            2. Количество товара
                            3. Производитель товара
                            4. Стоимость товара
                            5. Регион, из которого доставляется товар
                            6. Категория товара
                            7. Описание товара
                            8. Характеристика товара
                            9. Вес товара(в кг)
                            10.Артикул товара
                            11.Цвет товара
                            
                            """ ))

                            if parameter == 1:
                                name = input("Введите новое имя товара")

                                self.set_name(name)

                                print(f"Имя товара изменено на {self.get_name()}" )
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 2:
                                count = int(input("Введите новое количество товара"))

                                self.set_count(count)

                                print(f"Количество товара изменено на {self.get_count()}" )
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 3:
                                manufacturer = input("Введите нового производителя товара")

                                self.set_manufacturer(manufacturer)

                                print(f"Имя производителя товара изменено на {self.get_manufacturer()}" )
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 4:
                                cost = int(input("Введите новую стоимость товара"))

                                self.set_cost(cost)

                                print(f"Стоимость товара изменена на {self.get_cost()}" )
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 5:
                                region = int(input("Введите новое регион, из которого доставляется товар."))

                                self.set_region(region)

                                print(f"Регион, из которого доставляется товар изменен на {self.get_region()}" )
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 6:
                                category = input("Введите новую категорию товара")

                                self.set_category(category)

                                print(f"Категория товара изменена на {self.get_category()}")
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 7:
                                description = input("Введите новое описание товара")

                                self.set_description(description)

                                print(f"Описание товара изменено на {self.get_description()}")
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 8:
                                characteristic = input("Введите новую характеристику товара")

                                self.set_characteristic(characteristic)

                                print(f"Характеристика товара изменена на {self.get_characteristic()}")
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 9:
                                weight = input("Введите новый вес товара (в кг)")

                                self.set_weight(weight)

                                print(f"Вес товара изменен на {self.get_weight()}")
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 10:
                                article_number = int(input("Введите новый артикул товара."))

                                self.set_article_number(article_number)

                                print(f"Артикул товара изменен на {self.get_article_number()}")
                                input("\nНажмите Enter для продолжения...")
                            elif parameter == 11:
                                color = input("Введите новый цвет товара.")

                                self.set_color(color)

                                print(f"Цвет товара изменен на {self.get_color()}")
                                input("\nНажмите Enter для продолжения...")
                            else:
                                print('Введено неверное число.')
                        except ValueError:
                            print('Ошибка!Вводить можно только числа.')
                        except TypeError:
                            print('Ошибка типа данных.')

            except ValueError:
                print('Ошибка!Вводить можно только числа.')
            except TypeError:
                print('Ошибка типа данных.')

product = Product(
    name = 'Шоколад',
    manufacturer = "Milka"
)

product.menu()


