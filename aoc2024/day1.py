from collections import Counter
from pathlib import Path

from base.day import BaseDay

DATA_DIR = Path(__file__).parent / "data"


class Day(BaseDay):
    __data_path__ = DATA_DIR / "day1.txt"

    def part1(self):
        left, right = self.split_columns()

        result = 0
        for n1, n2 in zip(sorted(left), sorted(right)):
            _abs = abs(n1 - n2)
            result += _abs

        return result

    def part2(self):
        left, right = self.split_columns()

        result = 0
        counter = Counter(right)
        for number in left:
            result += number * counter.get(number, 0)

        return result

    def split_columns(self):
        left, right = [], []
        for line in self.data:
            n1, n2 = map(int, line.split())
            left.append(n1)
            right.append(n2)

        return left, right


class TestDay(Day):
    __data_path__ = DATA_DIR / "day1-test.txt"
