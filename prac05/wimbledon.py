FILENAME = "wimbledon.txt"

def main():
    champions_data = read_data(FILENAME)
    champions_dict, countries_set = process_champions_data(champions_data)
    display_results(champions_dict, countries_set)

def read_data(filename):
    """Reading data from a file and processing it into a list of lists."""
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            champions_data.append(line.strip().split(","))
    return champions_data

def process_champions_data(champions_data):
    """Processes the data and returns a dictionary of champions and win counts, as well as a variety of countries"""
    champions_dict = {}
    countries_set = set()

    for row in champions_data:
        champion = row[2]
        country = row[1]

        countries_set.add(country)


        if champion in champions_dict:
            champions_dict[champion] += 1
        else:
            champions_dict[champion] = 1

    return champions_dict, countries_set

def display_results(champions_dict, countries_set):
    """Output the champions countries."""
    print("Wimbledon Champions:")
    for champion, wins in champions_dict.items():
        print(f"{champion} {wins}")

    countries_list = sorted(countries_set)
    print(f"\nThese {len(countries_list)} countries have won Wimbledon:")
    print(", ".join(countries_list))

if __name__ == "__main__":
    main()
