from pathlib import Path

from base.day import BaseDay


XMAS_DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1),
]
XMAS_SEARCH = ["M", "A", "S"]


class Day(BaseDay):
    @staticmethod
    def to_matrix(data: list[str]) -> list[list[str]]:
        return [list(line) for line in data]

    def part1(self, data: list[str]) -> int:
        data = self.to_matrix(data)
        result = 0

        for row_index, row in enumerate(data):
            for column_index, letter in enumerate(row):
                if letter == "X":
                    for direction in XMAS_DIRECTIONS:
                        result += self._check_direction(
                            data,
                            (row_index, column_index),
                            direction,
                        )

        return result

    def _check_direction(
        self,
        data: list[list[str]],
        coordinates: tuple[int, int],
        direction: tuple[int, int],
    ) -> bool:
        row_index, column_index = coordinates
        for letter in XMAS_SEARCH:
            row_index += direction[0]
            column_index += direction[1]

            if not self._validate_coordinates(data, (row_index, column_index)):
                return False

            if data[row_index][column_index] != letter:
                return False

        return True

    def part2(self, data: list[str]) -> int:
        data = self.to_matrix(data)
        result = 0

        for row_index, row in enumerate(data):
            for column_index, letter in enumerate(row):
                if letter == "A":
                    x = True

                    for n1, n2 in (
                        (
                            (row_index + 1, column_index + 1),
                            (row_index - 1, column_index - 1),
                        ),
                        (
                            (row_index - 1, column_index + 1),
                            (row_index + 1, column_index - 1),
                        ),
                    ):
                        if not self._validate_coordinates(
                            data, n1
                        ) or not self._validate_coordinates(data, n2):
                            x = False
                            break

                        if {data[n1[0]][n1[1]], data[n2[0]][n2[1]]} != {"M", "S"}:
                            x = False
                            break

                    if x:
                        result += 1

        return result

    @staticmethod
    def _validate_coordinates(data: list[list[str]], coordinates: tuple[int, int]):
        row_len, column_len = len(data[0]), len(data)
        return 0 <= coordinates[0] < row_len and 0 <= coordinates[1] < column_len
