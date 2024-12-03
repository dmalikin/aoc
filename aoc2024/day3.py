import re
from pathlib import Path

from base.day import BaseDay

DATA_DIR = Path(__file__).parent / "data"


class Day(BaseDay):
    __data_path__ = DATA_DIR / "day3.txt"

    def part1(self) -> int:
        regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

        result = 0

        for line in self.data:
            r = re.findall(regex, line)

            for a, b in r:
                result += int(a) * int(b)

        return result

    def part2(self) -> int:
        pass


class TestDay(Day):
    __data_path__ = DATA_DIR / "day3-test.txt"


if __name__ == "__main__":
    part1_test_result = TestDay().part1()
    print(f"{part1_test_result=}")

    # part2_test_result = TestDay().part2()
    # print(f"{part1_test_result=}")

    part1_result = Day().part1()
    print(f"{part1_result=}")

    # part2_result = Day().part2()
    # print(f"{part2_result=}")
