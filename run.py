import argparse
import importlib
from types import ModuleType

from base.day import BaseDay


class Error(Exception):
    def __init__(self, message: str):
        self.message = message


def _import_day(year: int, day: int) -> ModuleType:
    package_name = f"aoc{year}"
    module_name = f"day{day}"

    try:
        module = importlib.import_module(f"{package_name}.{module_name}")
    except ModuleNotFoundError:
        raise Error(f"Could not find {module_name} module in {package_name} package.")

    return module


def _get_day(module: ModuleType, test: bool) -> BaseDay:
    if test:
        day = module.TestDay()
    else:
        day = module.Day()

    return day


def run(year: int, day: int, test: bool = False):
    module = _import_day(year=year, day=day)

    print(f"Initializing Year {year}, Day {day} {'[TEST]' if test else ''} ...")
    day = _get_day(module, test=test)

    part1_result = day.part1()
    print(f"Part 1 result: {part1_result}")

    part2_result = day.part2()
    print(f"Part 2 result: {part2_result}")


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Process some options.")

    parser.add_argument(
        "-y",
        "--year",
        type=int,
        help="Specify the year",
        default=2024,
    )
    parser.add_argument("-d", "--day", type=int, help="Specify the day")
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="Enable the test flag (True/False)",
        default=False,
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        run(year=args.year, day=args.day, test=args.test)
    except Error as e:
        print(e.message)


if __name__ == "__main__":
    main()
