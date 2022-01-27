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
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Iterable:
        with open(self.filename) as f:
            return [int(line) for line in f]

    def write(self, data: Iterable) -> None:
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value))
                f.write('\n')

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


class JsonFileDriver(IStructureDriver):
    def __init__(self, name):
<<<<<<< HEAD
        self.file = name

    @abstractmethod
    def read(self):
        with open(self.file) as file:
            return [json.loads(s) for s in file]

    @abstractmethod
    def write(self, data):
        with open(self.file, "wt") as file:
            file.write(json.dumps(file, indent=4))
=======
        self.file_name = name

    def read(self):
        """
        Чтение содержимого из json файла
        """
        with open(self.file_name) as file:
            json.loads(file)

    def write(self, data):
        """
        Запись содержимого в json файл
        """
        with open(self.file_name, "wt") as fi:
            json.dumps(fi, indent=4)
>>>>>>> a64aa4b10334e8b24517aa7b2eef563505be7b28

if __name__ == "__main__":
    # Write your solution here
    pass
