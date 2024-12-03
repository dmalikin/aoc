import re

from base.day import BaseDay


class Day(BaseDay):
    @staticmethod
    def merge_lines(data: list[str]) -> str:
        return "".join(data)

    def part1(self, data: list[str]) -> int:
        regex: str = "mul\((?P<n1>\d+),(?P<n2>\d+)\)"
        return self._part(data, regex, switch=False)

    def part2(self, data: list[str]) -> int:
        regex: str = "mul\((?P<n1>\d+),(?P<n2>\d+)\)|(?P<on>do\(\))|(?P<off>don't\(\))"
        return self._part(data, regex, switch=True)

    def _part(self, data: list[str], regex: str, switch: bool = False) -> int:
        pattern: re.Pattern = re.compile(regex)
        data: str = self.merge_lines(data)

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

    def part1_no_regex(self, data: list[str]):
        return self._part_no_regex(data, switch=False)

    def part2_no_regex(self, data: list[str]):
        return self._part_no_regex(data, switch=True)

    def _part_no_regex(self, data: list[str], switch: bool = False):
        data: str = self.merge_lines(data)
        start: str = "mul("
        do: str = "do()"
        dont: str = "don't()"

        result: int = 0
        i: int = 0
        mul_on: bool = True
        while i < len(data):
            if mul_on and data[i] == "m" and data[i : i + 4] == start:
                shift: int = 4
                j: int = i + 4
                q: list[str] = []
                pair: list[int] = []

                while True:
                    char = data[j]
                    if char == ")":
                        pair.append(int("".join(q)))

                        if len(pair) == 2:
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
