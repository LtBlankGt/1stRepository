if __name__ == "__main__":
    class Phone:
        """Базовый класс для телефонов."""

        def __init__(self, brand: str, model: str, memory: int) -> None:
            """
            Инициализация базового класса Phone.

            :param brand: Марка телефона.
            :param model: Модель телефона.
            :param year: Объем памяти телефона.
            """
            self.__brand = brand  # Непубличный атрибут
            self.__model = model  # Непубличный атрибут
            self.__memory = memory  # Непубличный атрибут

        def get_info(self) -> str:
            """Возвращает информацию о телефоне."""
            return f"{self.__brand} {self.__model}, {self.__memory}"

        def __str__(self) -> str:
            """Возвращает строковое представление объекта Phone."""
            return f"Phone(brand={self.__brand}, model={self.__model}, memory={self.__memory})"

        def __repr__(self) -> str:
            """Возвращает официальное строковое представление объекта Phone."""
            return f"Phone('{self.__brand}', '{self.__model}', {self.__memory})"


    class FoldingPhone(Phone):
        """Класс для раскладных телефонов, наследует Phone."""

        def __init__(self, brand: str, model: str, memory: int, cost: int) -> None:
            """
            Инициализация раскладного телефона.

            :param brand: Марка раскладного телефона.
            :param model: Модель раскладного телефона.
            :param memory: Объем памяти раскладного телефона.
            :param cost: Стоимость раскладного телефона.
            """
            super().__init__(brand, model, memory)  # Вызов конструктора базового класса
            self.cost = cost  # Публичный атрибут

        def get_info(self) -> str:
            """Возвращает информацию о раскладном телефоне, включая стоимость."""
            return f"{super().get_info()}, cost={self.cost} "

        def __str__(self) -> str:
            """Возвращает строковое представление объекта FoldingPhone."""
            return f"FoldingPhone(brand={self._Phone__brand}, model={self._Phone__model}, memory={self._Phone__memory}, cost={self.cost})"

        def __repr__(self) -> str:
            """Возвращает официальное строковое представление объекта FoldingPhone."""
            return f"FoldingPhone('{self._Phone__brand}', '{self._Phone__model}', {self._Phone__memory}, {self.Folding_cost})"


    class LandlinePhone(Phone):
        """Класс для стационарных телефонов, наследует Phone."""

        def __init__(self, brand: str, model: str, memory: int, wire_length: float) -> None:
            """
            Инициализация стационарного телефона.

            :param brand: Марка стационарного телефона.
            :param model: Модель стационарного телефона.
            :param memory: Объем памяти стационарного телефона.
            :param wire_length: Длина провода стационарного телефона (в метрах).
            """
            super().__init__(brand, model, memory)  # Вызов конструктора базового класса
            self.wire_length = wire_length  # Публичный атрибут

        def get_info(self) -> str:
            """Возвращает информацию о стационарном телефоне, длину провода."""
            return f"{super().get_info()}, wire length={self.wire_length} meters"

        def __str__(self) -> str:
            """Возвращает строковое представление объекта LandlinePhone."""
            return f"LandlinePhone(brand={self._Phone__brand}, model={self._Phone__model}, memory={self._Phone__memory}, wire_length={self.wire_length})"

        def __repr__(self) -> str:
            """Возвращает официальное строковое представление объекта LandlinePhone."""
            return f"LandlinePhone('{self._Phone__brand}', '{self._Phone__model}', {self._Phone__memory}, {self.wire_length})"


    # Пример использования классов
    if __name__ == "__main__":
        folding_phone = FoldingPhone("Samsung", "Galaxy Z Fold 6", 512, 174508)
        landline_phone = LandlinePhone("Panasonic", "KX-TS2350", 1, 2)

        print(folding_phone.get_info())
        print(landline_phone.get_info())
        print(folding_phone)
        print(landline_phone)

    pass
