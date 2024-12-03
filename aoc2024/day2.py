from base.day import BaseDay


class Day(BaseDay):
    @staticmethod
    def split_lines(data: list[str]) -> list[list[int]]:
        result = []
        for line in data:
            result.append(list(map(int, line.split())))
        return result

    def part1(self, data: list[str]) -> int:
        return self._run_part(data=data)

    def _run_part(self, data: list[str]) -> int:
        reports = self.split_lines(data)

        result = 0
        for report in reports:
            r = self._process_report(report)
            result += r

        return result

    def part2(self, data: list[str]) -> int:
        reports = self.split_lines(data)

        result = 0
        for report in reports:
            result += self._process_report_fault(report)

        return result

    def _process_report(self, report: list[int]) -> bool:
        previous = report[0]
        increase = None

        for current in report[1:]:
            difference = current - previous
            abs_difference = abs(difference)

            if abs_difference > 3 or abs_difference < 1:
                return False

            if increase is not None:
                if (increase > 0 > difference) or (increase < 0 < difference):
                    return False

            increase = difference
            previous = current

        return True

    @staticmethod
    def _compare(left: int, right: int) -> bool:
        difference = right - left
        abs_difference = abs(difference)
        return 1 < abs_difference < 3

    def _process_report_fault(self, report: list[int]) -> bool:
        if self._process_report(report):
            return True

        for i in range(len(report)):
            if self._process_report([*report[:i], *report[i + 1 :]]):
                return True

        return False
