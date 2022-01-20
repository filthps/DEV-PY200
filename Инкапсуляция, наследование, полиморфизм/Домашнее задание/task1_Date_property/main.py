class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        return year % 4 == 0

    @classmethod
    def get_max_day(cls, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        return cls.DAY_OF_MONTH[cls.is_leap_year(year)][month]

    @staticmethod
    def is_valid_date(day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        #if 0 > day >

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            raise TypeError

        if value > self.get_max_day(value, self._year):
            raise ValueError
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, val):
        if not isinstance(val, int):
            raise TypeError
        if val > 12:
            raise ValueError
        self._month = val

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._year = value


if __name__ == "__main__":
    ...
