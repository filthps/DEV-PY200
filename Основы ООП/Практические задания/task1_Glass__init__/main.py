from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError()
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError()
        if capacity_volume <= 0:
            raise ValueError()
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass
    glass1 = Glass(200, 100)
    glass2 = Glass(100, 200)
    print(glass1, glass2, sep="\n")
    # TODO попробовать инициализировать не корректные объекты

