from pathlib import Path


class BaseDay:
    def __init__(self, data: tuple[Path | None, Path | None]):
        self.data: list[str] = self.read_data(data[0])
        self.test_data: list[str] = self.read_data(data[1])

    @staticmethod
    def read_data(data_path: Path | str) -> list[str]:
        with open(data_path, "r") as file:
            data = file.readlines()

        return [line.strip() for line in data]

    def part1(self, data: list[str]) -> int:
        pass

    def part2(self, data: list[str]) -> int:
        pass
