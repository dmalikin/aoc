from pathlib import Path


class BaseDay:
    __data_path__: Path | str = ...

    def __init__(self):
        self.data: list[str] = self.read_data()

    def read_data(self) -> list[str]:
        with open(self.__data_path__, "r") as file:
            data = file.readlines()

        return [line.strip() for line in data]

    def part1(self) -> int:
        pass

    def part2(self) -> int:
        pass
