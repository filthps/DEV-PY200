import json
from typing import Iterable
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, driver_name=""):
        self.name = driver_name

    def read(self):
        with open(self.name) as f:
            return [i for i in f]

    def write(self, data):
        with open(self.name, "wt") as file:
            for i in data:
                file.write(i)


class JsonFileDriver(IStructureDriver):
    def __init__(self, driver_name=""):
        self.name = driver_name

    def read(self):
        with open(self.name) as f:
            return [json.loads(i) for i in f]

    def write(self, data):
        with open(self.name, "wt") as file:
            for i in data:
                file.write(json.dumps(i) + "\n")


if __name__ == '__main__':
    write_data = [1, 2, 3]
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
