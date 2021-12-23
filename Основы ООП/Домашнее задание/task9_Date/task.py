class Date:
    def __init__(self, day: int, month: int, year: int):
        if not isinstance(year, int):
            raise TypeError
        if not isinstance(month, int):
            raise TypeError
        if not isinstance(day, int):
            raise TypeError
        if month > 31:
            raise ValueError
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date({self.day}, {self.month} ,{self.year})"

    def __str__(self):
        month = self.month
        if month < 10:
            month = f"0{month}"
        day = self.day
        if day < 10:
            day = f"0{day}"
        return f"{day}/{month}{self.year}"
