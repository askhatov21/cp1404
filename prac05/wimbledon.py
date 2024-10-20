def read_wimbledon_data(filename):
    """Read the Wimbledon data from a CSV file."""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            parts = line.strip().split(',')
            champions.append(parts)
    return champions


def count_champion_wins(champions):
    """Count the number of wins for each champion."""
    champion_wins = {}
    for champion in champions:
        name = champion[2]
        champion_wins[name] = champion_wins.get(name, 0) + 1
    return champion_wins


def get_unique_countries(champions):
    """Get a set of unique countries from the champions list."""
    countries = set()
    for champion in champions:
        country = champion[1]
        countries.add(country)
    return countries


def display_results(champion_wins, countries):
    """Display the results for champions and their win counts, and the list of countries."""
    print("Wimbledon Champions:")
    for name, wins in champion_wins.items():
        print(f"{name} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def main():
    filename = "wimbledon.csv"
    champions = read_wimbledon_data(filename)
    champion_wins = count_champion_wins(champions)
    countries = get_unique_countries(champions)
    display_results(champion_wins, countries)


if __name__ == "__main__":
    main()
