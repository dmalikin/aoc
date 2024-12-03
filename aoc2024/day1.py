from collections import Counter

from base.day import BaseDay


class Day(BaseDay):
    def part1(self, data: list[str]) -> int:
        left, right = self.split_columns(data)

        result: int = 0
        for n1, n2 in zip(sorted(left), sorted(right)):
            _abs = abs(n1 - n2)
            result += _abs

        return result

    def part2(self, data: list[str]) -> int:
        left, right = self.split_columns(data)

        result: int = 0
        counter = Counter(right)
        for number in left:
            result += number * counter.get(number, 0)

        return result

    @staticmethod
    def split_columns(data: list[str]) -> tuple[list[int], list[int]]:
        left, right = [], []
        for line in data:
            n1, n2 = map(int, line.split())
            left.append(n1)
            right.append(n2)

        return left, right
