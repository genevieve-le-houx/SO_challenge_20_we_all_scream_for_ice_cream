import csv
import math
from pathlib import Path

SCOOP_PER_TUB = 9
SCOOP_PER_PERSON = 1.5

def read_file(filepath: Path) -> dict[str, int]:
    people_per_ice_cream_flavor = {}
    with open(filepath, encoding="utf-8", newline="\n") as f:
        csv_reader = csv.reader(f, delimiter=":")
        for line in csv_reader:
            supporter_name, additional_guests, flavor = [x.strip() for x in line]

            if flavor not in people_per_ice_cream_flavor:
                people_per_ice_cream_flavor[flavor] = 1 + int(additional_guests)
            else:
                people_per_ice_cream_flavor[flavor] += 1 + int(additional_guests)

    return people_per_ice_cream_flavor


def compute_tubs_needed(people_per_ice_cream_flavor: dict[str, int]) -> dict[str, int]:
    return {
        flavor: int(math.ceil(count * SCOOP_PER_PERSON / SCOOP_PER_TUB))
        for flavor, count in people_per_ice_cream_flavor.items()
    }


def main():
    data_s1 = read_file(Path("challenge_20_s1.txt"))
    tubs_s1 = compute_tubs_needed(data_s1)
    print("Scenario 1")
    print(tubs_s1)

    data_s2 = read_file(Path("challenge_20_s2.txt"))
    tubs_s2 = compute_tubs_needed(data_s2)
    print()
    print("Scenario 2")
    print(tubs_s2)

    data_s3 = read_file(Path("challenge_20_s3.txt"))
    tubs_s3 = compute_tubs_needed(data_s3)
    print()
    print("Scenario 3")
    print(tubs_s3)


if __name__ == "__main__":
    main()
