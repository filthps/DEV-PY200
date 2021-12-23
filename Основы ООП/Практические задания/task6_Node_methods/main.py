from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value  # TODO добавить атрибуты
        self.next = next_

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        return self.value  # TODO вернуть значение узла

    def get_next(self) -> Optional["Node"]:
        return self.next


if __name__ == '__main__':
    first_node = Node(1)  # первый узел
    second_node = Node(2)  # второй узел

    # TODO с помощью метода распечатать значение первого узла
    # TODO  с помощью метода распечатать следующий узел второго узла
    print(first_node.get_value())
    print(second_node.get_next())
