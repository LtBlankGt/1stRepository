import doctest


class table:
    def __init__(self, material: str, weight: int):

        """
            :param material (str): Материал стола
            :param weight(int, float): масса мебели
        """

        if not isinstance(material, str):
            raise TypeError("Название материала должно быть типа string")
        if not isinstance(weight, (int, float)):
            raise TypeError("масса стола должена быть типа int или float")
        if not weight >= 0:
            raise ValueError("масса должна быть больше 0")

        self.material = material
        self.weight = weight

    def assemble(self) -> str:
        """
        Сборка стола

        :raise: ValueError если масса стола указана некорректно

        :return: Строка с информацией о сборке.
        """
        ...

    def disassemble(self) -> str:
        """
        Разборка стола

        :raise: ValueError если масса стола указана некорректно

        :return: Строка с информацией о разборке.
        """
        ...



class tree:
    def __init__(self, species: str, height: float):
        if not isinstance(species, str):
            raise TypeError("название вида должно быть типа str")
        if height <= 0:
            raise ValueError("высота должна быть больше нуля")

        self.species = species
        self.height = height

    def grow(self, amount: float) -> str:
        """
        Рост дерева

        :param amount: Сколько метров вырастет дерево
        :return: Строка с информацией о росте.
        """
        ...

    def shed_leaves(self) -> str:
        """
        Сброс листьев

        :return: Строка с информацией о сбросе листьев.
        """
        ...

class car:
    def __init__(self, cost: int, top_speed: int, country_manufacturer: str):
        if not isinstance(country_manufacturer, (str)):
            raise TypeError
        if top_speed < 0:
            raise ValueError
        if not country_manufacturer.istitle() == True:
            raise ValueError

        self.top_speed = top_speed
        self.cost = cost
        self.country_manufacturer = country_manufacturer

    def get_top_speed(self) -> int:
            """
            :raise: ValueError если скорость автомобиля указана некорректно
            :return: макс. скорость авто

            Примеры:
            >>> speed = car(100)
            """
            ...

    def get_cost(self) -> int:
            """
            :raise: ValueError если стоимость автомобиля указана некорректно
            :return: стоимость авто

            Примеры:
            >>> cost = car(10000)
            """
            ...

    def get_country_manufacturer(self) -> str:
        """
        :raise: TypeError если страна указана в типе не str
        raise: ValueError если название страны не с заглавной буквы
         :return: страна производитель авто

        Примеры:
         >>> country = car("Germany")
        """
        ...




if __name__ == "__main__":
    doctest.testmod()


