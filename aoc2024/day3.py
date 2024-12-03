import re
from pathlib import Path

from base.day import BaseDay

DATA_DIR = Path(__file__).parent / "data"


class Day(BaseDay):
    __data_path__ = DATA_DIR / "day3.txt"

    def merge_lines(self) -> str:
        return "".join(self.data)

    def part1(self) -> int:
        regex: str = "mul\((?P<n1>\d+),(?P<n2>\d+)\)"
        return self._part(regex, switch=False)

    def part2(self) -> int:
        regex: str = "mul\((?P<n1>\d+),(?P<n2>\d+)\)|(?P<on>do\(\))|(?P<off>don't\(\))"
        return self._part(regex, switch=True)

    def _part(self, regex: str, switch: bool = False) -> int:
        pattern: re.Pattern = re.compile(regex)
        data: str = self.merge_lines()

        result: int = 0
        mul_on: bool = True
        for match in pattern.finditer(data):
            if switch and match.group("off") is not None:
                mul_on = False
                continue

            if switch and match.group("on") is not None:
                mul_on = True
                continue

            if mul_on:
                a, b = match.group("n1"), match.group("n2")
                result += int(a) * int(b)

        return result

    def part1_no_regex(self):
        return self._part_no_regex(switch=False)

    def part2_no_regex(self):
        return self._part_no_regex(switch=True)

    def _part_no_regex(self, switch: bool = False):
        data: str = self.merge_lines()
        start: str = "mul("
        do: str = "do()"
        dont: str = "don't()"

        result: int = 0
        i: int = 0
        mul_on: bool = True
        while i < len(data):
            if data[i] == "m" and data[i : i + 4] == start:
                shift: int = 4
                j: int = i + 4
                q: list[str] = []
                pair: list[int] = []

                while True:
                    char = data[j]
                    if char == ")":
                        pair.append(int("".join(q)))

                        if len(pair) == 2:
                            if mul_on:
                                result += pair[0] * pair[1]
                            i += shift + 1
                            break

                    elif char == ",":
                        if len(pair):
                            i += shift
                            break

                        pair.append(int("".join(q)))
                        q = []
                        shift += 1

                    elif char.isnumeric():
                        q.append(char)
                        shift += 1

                    else:
                        i += shift
                        break

                    j += 1

            elif switch and data[i] == "d":
                if data[i : i + 4] == do:
                    mul_on = True
                elif data[i : i + 7] == dont:
                    mul_on = False
                i += 1

            else:
                i += 1

        return result


class TestDay(Day):
    __data_path__ = DATA_DIR / "day3-test.txt"


if __name__ == "__main__":
    day = Day()
    test_day = TestDay()

    part1_test_result = test_day.part1()
    print(f"{part1_test_result=}")

    part2_test_result = test_day.part2()
    print(f"{part2_test_result=}")

    part1_result = day.part1()
    print(f"{part1_result=}")

    part2_result = day.part2()
    print(f"{part2_result=}")

    part1_test_result_no_regex = test_day.part1_no_regex()
    print(f"{part1_test_result_no_regex=}")

    part2_test_result_no_regex = test_day.part2_no_regex()
    print(f"{part2_test_result_no_regex=}")

    part1_result_no_regex = day.part1_no_regex()
    print(f"{part1_result_no_regex=}")

    part2_result_no_regex = day.part2_no_regex()
    print(f"{part2_result_no_regex=}")
