import importlib

from base.day import BaseDay


def main(year: int, day: int, test: bool = False):
    package_name = f"aoc{year}"
    module_name = f"d{day}"
    module = importlib.import_module(f"{package_name}.{module_name}")

    day: BaseDay

    if test:
        print(f"Initializing Year {year}, Day {day} [TEST] ...")
        day = module.TestDay()
    else:
        print(f"Initializing Year {year}, Day {day} ...")
        day = module.Day()

    part1_result = day.part1()
    print(f"Part 1 result: {part1_result}")

    part2_result = day.part2()
    print(f"Part 2 result: {part2_result}")


if __name__ == "__main__":
    main(2024, 1, test=True)
    main(2024, 1, test=False)
