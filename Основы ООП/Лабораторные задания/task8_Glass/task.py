from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.occupied_volume = None
        self.init_capacity_volume(capacity_volume)
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume):
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume):
        self.occupied_volume = occupied_volume

    def add_water(self, size):
        if not isinstance(size, (int, float)):
            raise TypeError
        if size > self.capacity_volume:
            raise ValueError

    def remove_water(self, size):
        if not isinstance(size, (int, float)):
            raise TypeError
        if size > self.occupied_volume:
            raise ValueError


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)