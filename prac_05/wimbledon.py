"""
Wimbledon
Load CSV and sort champions
Display champion and number of times won
Countries in alphabetical order
"""
# Column 2 is where champion of each wimbledon are stored
CSV_CHAMP_COLUMN = 2


def main():
    """Read csv and print details about Wimbledon champions and countries."""
    players_data = get_champions_data("wimbledon.csv")

    champion_to_count, countries = process_records(players_data)

    display_results(champion_to_count, countries)


def get_champions_data(filename):
    """Get champions data each line from csv file and put into list"""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()

        # read all lines, strip and split at ","
        for line in in_file:
            parts = line.strip().split(",")
            champions.append(parts)

    return champions


def process_records(records):
    """Create dictionary of champions and count number of wins
        set of countries from records (list of lists)."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[CSV_CHAMP_COLUMN]] += 1
        except KeyError:
            champion_to_count[record[CSV_CHAMP_COLUMN]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions with number of wins and countries that won"""
    print("Wimbledon Champions:")
    for champ_name, count in champion_to_count.items():
        print(champ_name, count)

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()
