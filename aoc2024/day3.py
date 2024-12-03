import re
from pathlib import Path

from base.day import BaseDay

DATA_DIR = Path(__file__).parent / "data"


class Day(BaseDay):
    __data_path__ = DATA_DIR / "day3.txt"

    def part1(self) -> int:
        regex = "mul\((\d+),(\d+)\)"
        pattern = re.compile(regex)
        data = self.merge_lines()

        result = 0
        matches = pattern.findall(data)

        for a, b in matches:
            result += int(a) * int(b)

        return result

    def part2(self) -> int:
        regex = "mul\((?P<n1>\d+),(?P<n2>\d+)\)|(?P<on>do\(\))|(?P<off>don't\(\))"
        pattern = re.compile(regex)
        data = self.merge_lines()

        result = 0
        mul_on = True
        for match in pattern.finditer(data):
            if match.group("off") is not None:
                mul_on = False

            elif match.group("on") is not None:
                mul_on = True

            else:
                if mul_on:
                    a, b = match.group("n1"), match.group("n2")
                    result += int(a) * int(b)

        return result

    def merge_lines(self) -> str:
        return "".join(self.data)


class TestDay(Day):
    __data_path__ = DATA_DIR / "day3-test.txt"


if __name__ == "__main__":
    part1_test_result = TestDay().part1()
    print(f"{part1_test_result=}")

    part2_test_result = TestDay().part2()
    print(f"{part2_test_result=}")

    part1_result = Day().part1()
    print(f"{part1_result=}")

    part2_result = Day().part2()
    print(f"{part2_result=}")
