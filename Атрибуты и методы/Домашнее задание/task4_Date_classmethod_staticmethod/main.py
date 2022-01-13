class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @classmethod
    def is_leap_year(cl, year: int):
        """Проверяет, является ли год високосным"""
        return year % 4 == 1

    @classmethod
    def get_max_day(class_items, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        return class_items.DAY_OF_MONTH[class_items.is_leap_year(year)][month]

    @staticmethod
    def is_valid_date(day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int):
            raise TypeError()
        if not isinstance(month, int):
            raise TypeError()
        if not isinstance(year, int):
            raise TypeError()
        if not 0 < day < 31:
            raise ValueError()
        if not 0 < month < 12:
            raise ValueError()

if __name__ == "__main__":
    # Write your solution here
    date = Date(10, 1, 2001)
    print(f"Год {date.year} високосный? - {date.is_leap_year(date.year)}")
    print(f"Максимальное количество дней в месяце {date.month} для указанного года: "
          f"{date.get_max_day(date.month, date.year)}")
