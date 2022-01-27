from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver, SimpleFileDriver, JsonFileDriver
from factory_method import JsonFileFactoryMethod


class LinkedListWithDriver(LinkedList):
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, item):
        if not isinstance(item, (IStructureDriver, type(None))):
            raise TypeError
        self._driver = item

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        data_from_driver = self.driver.read()

        for value in data_from_driver:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)


if __name__ == '__main__':
    ll = LinkedListWithDriver([1, 2, 3])
    driver = JsonFileFactoryMethod.get_driver()
    ll.driver = driver
    print(ll)
    ll.write()
    print(ll.read())
