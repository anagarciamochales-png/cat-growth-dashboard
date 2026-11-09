####

#Project development history.

#These functions were used while learning and are not meant to be executed.

#See main.py for the final version. 


# - Read CSV file
# - Count measurements
# - Find averages
# - Calculate age
# - Create growth graph

#Used while learning:
#- file reading
#- dictionaries
#- averages
#- age calculations

#Kept for future reference.

####

def count_measurements():
    cat_count = {}

    with open('cat_data.csv', 'r') as file:
        next(file)

        for line in file:
            row = line.strip().split(",")
            name = row[0]

            if name in cat_count:
                cat_count[name] += 1
            else:
                cat_count[name] = 1

           
       
    print("\n==== Cat Summary ====")
    for cat, count in cat_count.items():
        print(f"{cat}: {count} measurements")
    

count_measurements()


def average_weight():
    total_weight = 0
    measurement_count = 0

    with open("cat_data.csv", "r") as file:
        next(file)

        for line in file:
            row = line.strip().split(",")
            weight = float(row[2])
            total_weight += weight
            measurement_count += 1
    average = total_weight / measurement_count
    print(f"\nAverage weight of cats: {average:.2f} kg")

average_weight()


def average_weight_per_cat():
    cat_weights = {}

    with open("cat_data.csv", "r") as file:
        next(file)

        for line in file:
            row = line.strip().split(",")
            name = row[0]
            weight = float(row[2])

            if name not in cat_weights:
                cat_weights[name] = []

            cat_weights[name].append(weight)

    print("\n==== Cat Averages ====")
    for cat, weights in cat_weights.items():
        average = sum(weights) / len(weights)

        lowest = min(weights)
        highest = max(weights)

        print(f"\n{cat}")
        print(f"Average weight: {average:.2f} kg")
        print(f"Lowest weight: {lowest:.2f} kg")
        print(f"Highest weight: {highest:.2f} kg")

average_weight_per_cat()


def current_weight():
    latest_weights = {}

    with open("cat_data.csv", "r") as file:
        next(file)

        for line in file:
            row = line.strip().split(",")

            name = row[0]
            weight = float(row[2])

            latest_weights[name] = weight

    print("\n==== Current Weights ====")
    for cat, weight in latest_weights.items():
        print(f"{cat}: {weight:.2f} kg")
current_weight()

def latest_measurement():
    latest_data = {}

    with open("cat_data.csv", "r") as file:
        next(file)

        for line in file:
            row = line.strip().split(",")

            name = row[0]
            date = row[1]
            weight = float(row[2])

            latest_data[name] = {
                "date": date,
                "weight": weight
            }

    print("\n==== Latest Measurements ====")
    for cat, data in latest_data.items():
        print(f"\n{cat}")
        print(f"Date: {data['date']}")
        print(f"Weight: {data['weight']:.2f} kg")      

latest_measurement()

def growth_summary():
    cat_data = {}

    with open("cat_data.csv", "r") as file:
        next(file)

        for line in file:
            row = line.strip().split(",")

            name = row[0]
            date = row[1]
            weight = float(row[2])

            if name not in cat_data:
                cat_data[name] = []

            cat_data[name].append((date, weight))

    print("\n==== Growth Summary ====")
    for cat, measurements in cat_data.items():
        first_date = measurements[0][0]
        first_weight = measurements[0][1]

        last_date = measurements[-1][0]
        last_weight = measurements[-1][1]

        gained = last_weight - first_weight

        print(f"\n{cat}")
        print(f"First measurement: {first_date} - {first_weight:.2f} kg")
        print(f"Last measurement: {last_date} - {last_weight:.2f} kg")
        print(f"Weight gained: {gained:.2f} kg")

growth_summary()



def first_measurement_age():
    with open("cat_data.csv", "r") as file:
        next(file)

        first_seen = {}

        for line in file:
            row = line.strip().split(",")

            name = row[0]
            date = row[1]

            if name not in first_seen:
                first_seen[name] = date

    for cat, date in first_seen.items():

        birth = datetime.strptime(birth_dates[cat], "%Y-%m-%d")
        measurement = datetime.strptime(date, "%Y-%m-%d")

        age_days = (measurement - birth).days
        age_months = age_days / 30.44

        print(f"{cat}: {age_months:.1f} months")

first_measurement_age()

def create_growth_graph(cat_name):
    dates = []
    weights = []

    with open("cat_data.csv", "r") as file:
        next(file)

        for line in file:
            row = line.strip().split(",")

            name = row[0]
            date = row[1]
            weight = float(row[2])

            if name == cat_name:
                dates.append(date)
                weights.append(weight)

    plt.plot(dates, weights, marker="o")

    plt.title(f"{cat_name} Weight Growth")
    plt.xlabel("Date")
    plt.ylabel("Weight (kg)")

    plt.gca().set_xticks(plt.gca().get_xticks()[::10])
    plt.tight_layout()
    plt.show()

    plt.savefig(f"charts/{cat_name.lower()}_growth.png")

create_growth_graph("Misty")
create_growth_graph("Ash")
        
