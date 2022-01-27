import json
from typing import Sequence
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Sequence:
        with open(self.filename) as f:
            return [int(line) for line in f]

    def write(self, data: Sequence) -> None:
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value))
                f.write('\n')

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


class JsonFileDriver(IStructureDriver):
<<<<<<< HEAD
    def __init__(self, name):
        self.file = name

    def read(self):
        with open(self.file) as file:
            return [json.loads(s) for s in file]

    def write(self, data):
        with open(self.file, "wt") as file:
            file.write(json.dumps(file, indent=4))

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.file}\")"
=======

    def __init__(self, name):
        self.file_name = name

    def read(self):
        """
        Чтение содержимого из json файла
        """
        with open(self.FILE) as file:
            for line in file:
                json.loads(line)

    def write(self, data):
        """
        Запись содержимого в json файл
        """
        with open(self.FILE, "wt") as fi:
            for item in data:
                fi.write(str(item))

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.file_name}\")"
>>>>>>> a64aa4b10334e8b24517aa7b2eef563505be7b28


if __name__ == '__main__':
    write_data = [1, 2, 3]
    driver = SimpleFileDriver('tmp.txt')
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
