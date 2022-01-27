from abc import ABC, abstractmethod

from drivers import IStructureDriver, SimpleFileDriver


class DriverFactoryMethod(ABC):
    """
    Абстрактная "фабрика"
    """
    @classmethod # Если тут classmethod
    @abstractmethod
    def get_driver(cl):
        pass


class SimpleFileFactoryMethod(DriverFactoryMethod):
    DEFAULT_NAME = 'untitled.txt'

    @classmethod  # то и здесь нужно сделать classmethod
    def get_driver(cls) -> IStructureDriver:
        filename = input('Введите название текстового файла: (.txt): ').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.txt'):
            filename = f'{filename}.txt'

        return SimpleFileDriver(filename)


if __name__ == '__main__':
    driver = SimpleFileFactoryMethod.get_driver()
    print(driver)
