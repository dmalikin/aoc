from pathlib import Path

from base.day import BaseDay

DATA_DIR = Path(__file__).parent / "data"


class Day(BaseDay):
    """
    1: 591
    2: 621
    """

    __data_path__ = DATA_DIR / "day2.txt"

    def part1(self) -> int:
        return self._run_part(no_faults=False)

    def part2(self) -> int:
        reports = self.split_lines()

        result = 0
        for report in reports:
            result += self._process_report_fault(report)

        return result

    def split_lines(self) -> list[list[int]]:
        result = []
        for line in self.data:
            result.append(list(map(int, line.split())))
        return result

    def _run_part(self, no_faults: bool = False) -> int:
        reports = self.split_lines()

        result = 0
        for report in reports:
            r = self._process_report(report, no_faults=no_faults)
            result += r

        return result

    def _process_report(self, report: list[int], no_faults: bool = False) -> bool:
        previous = report[0]
        increase = None

        for current in report[1:]:
            difference = current - previous
            abs_difference = abs(difference)

            if abs_difference > 3 or abs_difference < 1:
                return False

            if increase is not None:
                if (increase > 0 and difference < 0) or (increase < 0 and difference > 0):
                    return False

            increase = difference
            previous = current

        return True

    def _compare(self, left: int, right: int) -> bool:
        difference = right - left
        abs_difference = abs(difference)
        return 1 < abs_difference < 3

    def _process_report_fault(self, report: list[int]) -> bool:
        reports = [report]

        for i in range(len(report)):
            reports.append([*report[:i], *report[i + 1 :]])

        for subreport in reports:
            if self._process_report(subreport, no_faults=False):
                return True
        return False


class TestDay(Day):
    """
    1: 2
    2: 4
    """

    __data_path__ = DATA_DIR / "day2-test.txt"
